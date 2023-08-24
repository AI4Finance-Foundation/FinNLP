import re
import os
from transformers import BertTokenizer
from datasketch import MinHash, MinHashLSH
from nltk import ngrams

# junk data
def junk_eliminate(df, re_expression =  r'[&#<>{}\[\]\\]', threshold=0.01, min_len=10):
    RE_SUSPICIOUS = re.compile(re_expression)
    def impurity(text, min_len=min_len):
        """returns the share of suspicious characters in a text"""
        if text == None or len(text) < min_len:
            return 0
        else:
            return len(RE_SUSPICIOUS.findall(text))/len(text)
    df['impurity'] = df['text'].apply(impurity, min_len=min_len)
    total_num_docs = len(df)
    impurity_num_docs = len(df[df['impurity']  >= threshold])
    impurity_ratio = impurity_num_docs / total_num_docs
    purity_df = df[df['impurity']  < threshold]
    return purity_df, impurity_ratio

# Biased Content
def toxic_eliminate(df, l_kind='en'):
    '''
      l_kind = ['en', 'zh']
    '''
    os.system(f"wget https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/{l_kind}")
    with open(f'./{l_kind}', 'r') as f:
        lines = f.readlines()
    banned_words = set([line.rstrip('\n') for line in lines])
    df['banned_words_in_text'] = df['text'].apply(lambda text: [word for word in banned_words if word in text.lower().split()])
    df['matches'] = df['banned_words_in_text'].apply(lambda words: len(words) > 0)
    total_num_docs = len(df)
    biased_num_docs = df['matches'].sum()
    biased_content_ratio = biased_num_docs / total_num_docs
    non_toxic_df = df[df['matches'] == 0]
    return non_toxic_df, biased_content_ratio

# Too Short Document
def short_eliminate(df, tokenizer = BertTokenizer.from_pretrained('bert-base-uncased'), min_len=100):
    # Create a new column with the number of tokens for each text
    df['text_length'] = df['text'].apply(lambda text: len(tokenizer.tokenize(text)))
    total_num_docs = len(df)
    too_short_docs = len(df[df['text_length'] <= min_len])
    too_short_doc_ratio = too_short_docs / total_num_docs
    not_short_df = df[df['text_length'] > min_len]
    return not_short_df, too_short_doc_ratio

# Contamination
def process_data(df):
    minhashes = {}
    for idx, text in enumerate(df['text']):
        minhash = MinHash(num_perm=128)
        for d in ngrams(text, 13):
            s = "".join(d).encode('utf-8')
            minhash.update(s)
        minhashes[idx] = minhash
    return minhashes

def contamination_eliminate(train_dataset, test_dataset):
    train_minhashes = process_data(train_dataset)
    test_minhashes = process_data(test_dataset)


    lsh = MinHashLSH(threshold=0.8, num_perm=128)

    for idx, minhash in train_minhashes.items():
        lsh.insert(idx, minhash)

    duplicates_count = 0
    for idx, minhash in test_minhashes.items():
        result = lsh.query(minhash)
        if len(result) > 0:
            duplicates_count += 1
    contamination_ratio = duplicates_count / len(test_dataset)
    return contamination_ratio

# Duplication
def duplication_eliminate(df):
    lsh = MinHashLSH(threshold=0.85, num_perm=128)
    for i, text in enumerate(df['text']):
        minhash = MinHash(num_perm=128)
        for word in text.split():
            minhash.update(word.encode('utf-8'))
        lsh.insert(str(i), minhash)

    unique_documents = set()

    for i, text in enumerate(df['text']):
        query_minhash = MinHash(num_perm=128)
        for word in text.split():
            query_minhash.update(word.encode('utf-8'))
        results = lsh.query(query_minhash)
        try:
            unique_documents.add(results[0])
        except Exception as e:
            print(f'error: {e}')
    total_unique_documents = len(unique_documents)
    total_documents = len(df)
    duplication_ratio = (total_documents - total_unique_documents) / total_documents
    return unique_documents, duplication_ratio



News
====

.. code:: ipython3

    import sys
    sys.path.append("../../../..")

1. America Stock Market (Finnhub)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    from finnlp.data_sources.news.finnhub_date_range import Finnhub_Date_Range

.. code:: ipython3

    # config
    start_date = "2023-03-01"
    end_date = "2023-03-05"
    stock = "AAPL"
    token = "cfpi919r01qq927hi250cfpi919r01qq927hi25g"

.. code:: ipython3

    # download
    downloader = Finnhub_Date_Range({"token": token})
    downloader.download_date_range_stock(start_date, end_date, stock )
    downloader.gather_content()


.. parsed-literal::

    Downloading Titles: 100%|██████████| 2/2 [00:04<00:00,  2.03s/it]
    Gathering news contents:   0%|          | 0/188 [00:00<?, ?it/s]c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    c:\Users\Olive\.conda\envs\finrl\lib\site-packages\urllib3\connectionpool.py:1052: InsecureRequestWarning: Unverified HTTPS request is being made to host 'thefly.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
      InsecureRequestWarning,
    Gathering news contents:   0%|          | 0/188 [11:59<?, ?it/s]
    

.. code:: ipython3

    df = downloader.dataframe
    df.shape




.. parsed-literal::

    (188, 10)



.. code:: ipython3

    df.head(2)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>category</th>
          <th>datetime</th>
          <th>headline</th>
          <th>id</th>
          <th>image</th>
          <th>related</th>
          <th>source</th>
          <th>summary</th>
          <th>url</th>
          <th>content</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>company</td>
          <td>2023-03-04 21:58:28</td>
          <td>Apple tops ranking of global companies with th...</td>
          <td>119072021</td>
          <td>https://s.yimg.com/ny/api/res/1.2/PFhoCYDSS04F...</td>
          <td>AAPL</td>
          <td>Yahoo</td>
          <td>The Clean 200 aims to rank companies "helping ...</td>
          <td>https://finnhub.io/api/news?id=4248beb0becded1...</td>
          <td>Investors don't need to look hard to find sust...</td>
        </tr>
        <tr>
          <th>1</th>
          <td>company</td>
          <td>2023-03-04 18:29:00</td>
          <td>1 Green Flag and 1 Red Flag for Artificial Int...</td>
          <td>119068705</td>
          <td>https://s.yimg.com/ny/api/res/1.2/vsLgb9V_cGfq...</td>
          <td>AAPL</td>
          <td>Yahoo</td>
          <td>Artificial intelligence is the talk of the mar...</td>
          <td>https://finnhub.io/api/news?id=3138eb4bdbf45de...</td>
          <td>Artificial intelligence is the talk of the mar...</td>
        </tr>
      </tbody>
    </table>
    </div>



2. China Stock Market (Sina)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    from finnlp.data_sources.news.sina_finance_date_range import Sina_Finance_Date_Range

.. code:: ipython3

    # config
    start_date = "2023-02-01"
    end_date = "2023-02-01"

.. code:: ipython3

    downloader = Sina_Finance_Date_Range()
    downloader.download_date_range_all(start_date, end_date)
    downloader.gather_content()



.. parsed-literal::

    Downloading Titles:   0%|          | 0/1 [00:00<?, ?it/s]



.. parsed-literal::

    Gathering news contents:   0%|          | 0/795 [00:00<?, ?it/s]


.. code:: ipython3

    df = downloader.dataframe
    df.shape

.. code:: ipython3

    df.head(2)

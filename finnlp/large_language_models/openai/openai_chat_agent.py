import openai
import numpy as np

class Openai_Chat_Agent:
    def __init__(self,args):
        assert "token" in args.keys()
        openai.api_key = args["token"]
        
        self.temperature = args["temperature"] if "temperature" in args.keys() else 1
        self.top_p = args["top_p"] if "top_p" in args.keys() else 1
        self.n = args["n"] if "n" in args.keys() else 1
        self.max_tokens = args["max_tokens"] if "max_tokens" in args.keys() else None
        self.presence_penalty = args["presence_penalty"] if "presence_penalty" in args.keys() else 0
        self.frequency_penalty = args["frequency_penalty"] if "frequency_penalty" in args.keys() else 0
        
        self.conversation_list = []
        if "init_prompt" in args.keys():
            self.conversation_list.append(
                {"role":"system","content":args["init_prompt"]}
            )

    def get_single_response(self,prompt):
        self.conversation_list.append({"role":"user","content":prompt})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.conversation_list,
            temperature = self.temperature,
            top_p = self.top_p,
            n = self.n,
            max_tokens = self.max_tokens,
            presence_penalty = self.presence_penalty,
            frequency_penalty = self.frequency_penalty,
        )
        answer = response.choices[0].message['content']
        self.conversation_list.append({"role":"assistant","content":answer})
        return answer
    
    def show_conversation(self):
        conversation_list = self.conversation_list
        for msg in conversation_list:
            content = msg['content']
            content = content.replace(".",".\n")
            if msg['role'] == 'user':
                print(f"\U0001F47B: {content}\n")
            elif msg['role'] == 'system':
                print(f"\U0001F4BB: {content}\n")
            else:
                print(f"\U0001F916: {content}\n")

    def get_multiple_response(self,prompts):
        pass
    

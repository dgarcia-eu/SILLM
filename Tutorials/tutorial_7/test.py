import openai

from openai import OpenAI
api_base="base"
api_key='your_key'


client =  OpenAI(api_key=api_key, base_url = api_base)
        

responses = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": 'Hello ChatGPT!'}],n=1)

print(responses)



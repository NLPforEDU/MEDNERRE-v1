import os
import openai

pres_path = os.getcwd()

f = open('api_key.txt')
openai.api_key = f.read()
f.close()

f = open(os.getcwd()+'/core_code/prompt.txt')
prompt_text = f.read()
f.close()

def get_response(text):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt_text+text+'\noutput:',
    temperature=0.7,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']
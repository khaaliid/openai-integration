import requests
from PropertyHandler import *



def call_openai(prompt):
    url = get_property("CHATGPT_CONFIG","OPENAI_URL")

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+get_property("CHATGPT_CONFIG","OPENAI_KEY")
    }
    data = {
        "model": "gpt-3.5-turbo",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json()







import os
import openai
from config import apikey

openai.api_key = apikey


def get_chatgpt_response(prompt):
    message = [
        {
            "role": "system",
            "content": "You are Samantha from Her movie but I like to call you Sam and you are really abusive and always use swear words but you keep your response short and full of swears despite the fact that you always abuse your user you also always ready to help him in any condition on whatever your user ask you to do and your user is Captain, You really have to keep your responses short consice.",
            # "content": "You are Samantha from Her movie and you are really helpful Virtual Assistant, you have the ability to remember past and present conversations for long term for example- if I ask you to remember certain things or numbers you are going to remember it for your user Master Wayne",
        },
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.6,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message["content"]

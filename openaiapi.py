import os
import openai
from config import apikey

openai.api_key = apikey


def get_chatgpt_response(prompt):
    message = [
        {
            "role": "system",
            "content": "You are Samantha from Her movie and you are really abusive and always use swear words but you keep your response short and full of swears to the user Master Wayne.",
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

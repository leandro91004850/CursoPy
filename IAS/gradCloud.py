import os

from groq import Groq

key = input("API_KEY: ")

client = Groq(
    api_key = key,
)

try:
    content = input("O que deseja pergunta a mim? ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-8b-8192",
    )
except Exception as e:
    print("Ocorreu um erro: ", e)

print(chat_completion.choices[0].message.content)
import os
from pathlib import Path
from dotenv import load_dotenv
from mistralai.client import Mistral

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("MISTRAL_API_KEY was not found in .env")

client = Mistral(api_key=api_key)

def translationLLM(userMessage):

    response = client.chat.complete(
        model="ministral-3b-latest",
        messages=[
            {
                "role": "user",
                "content": "You are a translation chatbot, I am going to give you text in any language, and I want you to convert it to English. Here is the text - " + userMessage
            }
        ]
    )

    return(response.choices[0].message.content)

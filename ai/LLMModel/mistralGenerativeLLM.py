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

def translationLLM(usersQuestion, llmResponse):

    response = client.chat.complete(
        model="ministral-3b-latest",
        messages=[
            {
                "role": "user",
                "content": "Here is a question asked by a user" + usersQuestion + " And here are the most relevant pages"
            }
        ]
    )

    print(response.choices[0].message.content)

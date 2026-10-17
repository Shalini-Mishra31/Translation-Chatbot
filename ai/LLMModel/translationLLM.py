from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="CohereLabs/North-Small-Translate-1.0-fp8",
    task="translation",
)

model = ChatHuggingFace(llm = llm)

ans = model.invoke("")

print(ans)
from langchain_chroma import Chroma
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
)

model=ChatHuggingFace(llm=llm)

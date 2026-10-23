from langchain_huggingface  import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

load_dotenv()

@tool
def multiply(a:int,b:int)->int:
    """given 2 integers a,b, the function return the prodict of a and b"""
    return a*b

llm=HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="conversational",
        max_new_tokens=512,
        provider="novita"
    )

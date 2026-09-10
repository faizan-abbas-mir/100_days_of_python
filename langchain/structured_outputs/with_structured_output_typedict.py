from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

class Review(TypedDict):
    summary:str
    sentiment:str


model=ChatOpenAI(model="gpt-4.0")
structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""Eefefefe""")

print(result['summary'])
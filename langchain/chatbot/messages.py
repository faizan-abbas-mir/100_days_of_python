from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

messages=[
    SystemMessage(content="you are an ai expert"),
    HumanMessage(content="hello")
]


result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(result)
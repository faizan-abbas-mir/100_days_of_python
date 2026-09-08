from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
chat_history=[
    SystemMessage(content='you are a helpful chatbot')
]

model=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    provider="auto",
    max_new_tokens=512,
    )



llm=ChatHuggingFace(llm=model)

while True:
    user_input=input("you: ")
    if user_input=='exit':
        break
    chat_history.append(HumanMessage(content=user_input))

    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    
    print('AI: ',result.content)
    print(chat_history)
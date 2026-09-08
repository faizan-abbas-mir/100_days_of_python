from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
chat_history={}

model=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    provider="auto",
    max_new_tokens=512,
    )



llm=ChatHuggingFace(llm=model)

while True:
    user_input=input("you: ")
    chat_history["user"]=user_input
    if user_input=='exit':
        break
    result=llm.invoke(chat_history)
    chat_history["AI"]=result
    print('AI: ',result.content)
    print(chat_history)
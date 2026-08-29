from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model_name='gpt 3.5')

result=model.invoke('what is the capital of india?')
print(result)
print(result.content)
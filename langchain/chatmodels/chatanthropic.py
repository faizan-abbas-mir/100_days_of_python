from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model_name="claude-2", temperature=0.5)
result=model.invoke('what is the capital of india?')

print(result.content)


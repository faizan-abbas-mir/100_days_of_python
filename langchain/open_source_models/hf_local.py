from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv

llm=HuggingFacePipeline (
    repo_id="tinyllama",
    task="text_generation",
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens=100,
)
)
model=ChatHuggingFace(llm=llm)

result=model.invoke("what are you?")
print(result.content)
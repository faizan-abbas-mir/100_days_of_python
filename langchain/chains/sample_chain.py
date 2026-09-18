from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template=PromptTemplate(
    template="generate 3 interesting facts about {topic}",
    input_variables=['topic']
)
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
    
)
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

chain= template | model |parser

result=chain.invoke({'topic':'cricket'})

print(result)
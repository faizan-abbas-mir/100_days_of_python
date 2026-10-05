from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
)

model=ChatHuggingFace(llm=llm)
parser= StrOutputParser()

prompt=PromptTemplate(
    template="write a joke about the topic{topic}",
    input_variables=['topic']

)
chain= prompt | model | parser



prompt3=PromptTemplate(

    template="explain the joke \n {joke}",
    input_variables=['joke']
)

chain2= prompt3 | model | parser
final_chain=chain | chain2

result=final_chain.invoke({"topic":'domkey'})
print(result)
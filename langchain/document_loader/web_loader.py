from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
)

model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

url='https://www.flipkart.com'
loader=WebBaseLoader(url)
page=loader.load()

prompt=PromptTemplate(
    template='read the content of the html page \n{text}',
    input_variables=['text']
)

chain=prompt |model |parser

result=chain.invoke(page)
print(result)
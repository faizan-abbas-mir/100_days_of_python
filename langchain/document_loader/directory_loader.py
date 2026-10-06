from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
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
parser=StrOutputParser()


loader=DirectoryLoader(
    path="books",
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()
print(docs)

prompt=PromptTemplate(
    template='what is the name of the files given to you{text}',
    input_variables=['text']
)

chain= prompt | model |parser

result=chain.invoke(docs)
print(result)
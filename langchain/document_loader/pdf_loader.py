from langchain_community.document_loaders import PyPDFLoader
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

loader=PyPDFLoader('Faizan_Abass_Mir_Resume.pdf')

docs=loader.load()
#print(docs)

prompt1=PromptTemplate(
    template='what do you think about the candidate from his resume\n {text}',
    input_variables=['text']

)

chain=prompt1 | model |parser

result=chain.invoke(docs[0].page_content)

print(result)
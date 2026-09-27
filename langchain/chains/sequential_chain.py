from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt1=PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="generate a 3 pointer summary of the \n {text}",
    input_variables={'text'}
)

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
)

model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

chain=prompt1 | model | parser| prompt2 | model | parser

result=chain.invoke("tajmahal")

print(result)

chain.get_graph().print_ascii()
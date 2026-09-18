#string output parser: gives out string as output always. used over result.content 
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
model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()

template=PromptTemplate(
    template="Extract the name, age, pros and cons of the  from the following text: {text}",
    input_variables=["text"]

)
prompt1=template.invoke({"text": "hello this is very bad my name is john do not buy quality is bad i am 51 years old"})

result=model.invoke(prompt1)
print(result.content)
###################################################################################

template2=PromptTemplate(
    template="extract the tone of this text and tell if the user is happy or not :{text}",
    input_variables=['text']

)
parser=StrOutputParser()

chain= template | model | parser | template2 | model |parser

result= chain.invoke ({"text": "hello this is very bad my name is john do not buy quality is bad i am 51 years old"})

print(result)
#string output parser: gives out string as output always. used over result.content 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
)
model = ChatHuggingFace(llm=llm)
parser=JsonOutputParser()

template=PromptTemplate(
    template="give me the capitals of 5 counties \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

prompt=template.format()
print(prompt)
chain = template | model | parser 
result=chain.invoke({})
print(result)
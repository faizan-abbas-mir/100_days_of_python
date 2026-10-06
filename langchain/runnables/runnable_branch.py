from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableBranch,RunnablePassthrough
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

prompt1=PromptTemplate(
    template='write a detaled report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='summarise the report under 100 words \n {report}',
    input_variables=['report']
)

report_chain= prompt1 | model | parser
summarise_chain= report_chain |prompt2 |model | parser

length_check_chain= RunnableBranch(
    (lambda x:len(x.split())>100,summarise_chain),
    RunnablePassthrough()

)

final_chain=report_chain | length_check_chain

result=final_chain.invoke('donkey')
print(result)
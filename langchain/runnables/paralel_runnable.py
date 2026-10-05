from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence
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
    template='generate a linkedin post for the {topic}',
    input_variables=['topic']

)
prompt2=PromptTemplate(
    template='generate a twitter post for the {topic}',
    input_variables=['topic']

)

paralell_chain=RunnableParallel({
    'twitter':RunnableSequence(prompt2,model,parser),
    'linkedin':RunnableSequence(prompt1,model,parser)
}
)

result=paralell_chain.invoke({'topic':'ai'})
print(result)

paralell_chain.get_graph().print_ascii()
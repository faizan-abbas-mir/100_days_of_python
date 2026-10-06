from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda,RunnablePassthrough
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

def word_counter(text):
    return len(text.split())



prompt1=PromptTemplate(
     template='generate a jooke on the topic{topic}',
     input_variables=['topic']

 )

chain1= prompt1 | model |parser

paralell_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word length':RunnableLambda(word_counter)
    }
    
)
final_chain=chain1|paralell_chain

result=final_chain.invoke('donkey')
print(result)
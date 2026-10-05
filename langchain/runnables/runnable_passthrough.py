from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough
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
    template="generate a joke for the topic{topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="explain the joke \n{joke}",
    input_variables=['joke']
)

jokechain=prompt1 | model |parser
#print(result)

paralell_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(jokechain,prompt2,model,parser)

}
)
final_chain= jokechain|paralell_chain

final_joke=final_chain.invoke({'topic':'donkey'})
print(final_joke)
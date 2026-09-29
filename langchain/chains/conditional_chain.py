from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

template=PromptTemplate(
    template="generate 3 interesting facts about {topic}",
    input_variables=['topic']
)
llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
    provider="novita"
    
)
model1=ChatHuggingFace(llm=llm)

parser=StrOutputParser

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Sentiment of the feedback")


parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1= PromptTemplate(
    template="Classify the sentiment of the following feedback as positive or negative\nFeedback: {feedback}\n{format_instructions}",
    partial_variables={'format_instructions':parser2.get_format_instructions()},
    input_variables={'feedback'}
)

classifier_chain= prompt1 | model1 |parser2 

result=classifier_chain.invoke({"feedback": "this is a terrible product"})
print(result)


prompt2=PromptTemplate(
    template="wrute a proper response to this positive feedback \n {feedback} ",
    input_variable= {"feedback"}
)

prompt3=PromptTemplate(
    template="wrute a proper response to this negative feedback \n {feedback} ",
    input_variable= {"feedback"}
)


branch_chain= RunnableBranch(
    (lambda x:x.sentiment == "positive" ,  prompt2 |model1 | parser),
    (lambda x:x.sentiment == "negative" ,  prompt3 |model1 | parser),
    RunnableLambda(lambda x:" could not find sentiemnt")


)


final_chain= classifier_chain | branch_chain

final_chain.invoke({"feedback":"this is a terribel phone"})
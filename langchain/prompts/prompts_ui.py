from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv


import streamlit as st

load_dotenv()
model = ChatOpenAI(model='gpt-4o-mini')

st.header('research tool')

user_input = st.text_input('Enter your prompt')

if st.button('summarize'):
    result=model.invoke(user_input)
    st.write(result.content)

#promptTemplate
template=PromptTemplate(
    template="""
    ejrjjfjbrerbg


""",
input_variables=["input"]

)
new_template=load_prompt('template.json')


PROMPT=template.invoke({"input": user_input})
result=model.invoke(PROMPT)
st.write(result.content)

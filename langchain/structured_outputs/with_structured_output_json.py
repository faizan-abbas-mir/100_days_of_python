from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="whatever")

#schema



json_schema={
    "title":"student",
    "description":"name of the student",
    "type":"objects",
    "properties":{
        "name":"string",
        "age":"int",
        "pros":"string",
        "cons":"string"

    }


}
structured_model=model.with_structured_output(json_schema)
result=structured_model.invoke("hello this is very bad my name is john do not bu=y quality is bad")

print(result)
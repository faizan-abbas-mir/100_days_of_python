#uses pydantic model for input anf output validation

from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

class Multiplyinput(BaseModel):
    a:int   = Field(description='first input')
    b:int   =Field(description='second input')

def multiply_func(a,b):
    return a*b


multiply_tool=StructuredTool.from_function(
    func=multiply_func,
    args_schema=Multiplyinput
)

result=multiply_tool.invoke({'a':3,'b':4})

print(result)
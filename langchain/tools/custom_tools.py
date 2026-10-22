#how to make a custom tool

from langchain_core.tools import tool

@tool
def multiply(a:int,b:int)->int:
    """multiply these numbers"""
    return a*b

result=multiply.invoke({'a':3,'b':5})
print(result)

#using structured tool and pydantic

@tool
def add(a,b):
    return a+b


class Mathtoolkit:
    def get_tools(self):
        return[add,multiply]


toolkit=Mathtoolkit()
tools=toolkit.get_tools()
   
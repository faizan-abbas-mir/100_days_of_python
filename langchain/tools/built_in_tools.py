#built in search tool

from langchain_community.tools import DuckDuckGoSearchRun

search_tool=DuckDuckGoSearchRun()

result=search_tool.invoke('ipl')
print(result)

#built iin shell tool
from langchain_community.tools import ShellTool

shell_tool=ShellTool()

result=shell_tool.invoke('who am i')
print(result)
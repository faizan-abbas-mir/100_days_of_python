from pydantic import BaseModel,Field
from typing import Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="chatgpt-4.o")


class Review(BaseModel):
    key_themes:list[str]= Field(description="used to give themes of the description")
    summary: str = Field(description="sumary of the review")
    sentiment: str = Field(description="overall sentiment of the summary")
    pros: Optional[str] = Field(default=None,description="give the plus points of tge review if any")
    cons: Optional[str] = Field(default=None,description="give the negative points of the review if any")
    name: Optional[str]= Field(default=None)


structured_model=model.with_structured_output(Review)

result=structured_model.invoke("hello this is very bad my name is john do not bu=y quality is bad")

print(result.key_themes)
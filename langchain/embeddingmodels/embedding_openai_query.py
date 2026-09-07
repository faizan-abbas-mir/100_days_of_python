from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedder=OpenAIEmbeddings(model='text-embed-3-large', dimentions=32)

doc=["who isyou",
     "is you me",
     "what is the capitol of india"
     ]


result=embedder.embed_query("who are you?")
result2=embedder.embed_documents(doc)

print(str(result))
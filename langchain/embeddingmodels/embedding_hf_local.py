from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

embedder=HuggingFaceEmbeddings(model="sentence-transformer",dimentions=55)

embedder.embed_query("who")



from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


embedding=HuggingFaceEmbeddings(model='sentence-transformer')


doc1=["jdjdjdjdjjkfjfjfjfjdfjdjjdf",
      "jdejdjdjkdjdjkdjdjdjdjdjdjn",
      "kjnfkwnnfewfbwekkjehefeiffek"]

doc2=["jdjdjdjdjjkfjfjfjfjdfjdjjdf",
      "jdejdjdjkdjdjkdjdjdjdjdjdjn",
      "kjnfkwnnfewfbwekkjehefeiffek"]

embeding1=embedding.embed_documents(doc1) 
embeding2=embedding.embed_documents(doc2)

scores=cosine_similarity([embeding2],embeding1)
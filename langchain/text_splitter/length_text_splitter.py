from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader('../document_loader/docname.txt', encoding='utf-8')

doc=loader.load()


splitter=CharacterTextSplitter(
    chunk_size=5,
    separator='',
    chunk_overlap=0
)

result=splitter.split_documents(doc)

print(result[0].page_content)
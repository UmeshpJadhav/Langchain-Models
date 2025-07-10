from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser

loader = PyPDFLoader('RAG/AgenticAI-v2.0.pdf')

docs = loader.load()

print(len(docs))

print(docs[8].page_content)

print(docs[8].metadata)
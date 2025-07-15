from langchain_voyageai import VoyageAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import getpass
import os
from dotenv import load_dotenv
load_dotenv()

if not os.environ.get("VOYAGE_API_KEY"):
  os.environ["VOYAGE_API_KEY"] = getpass.getpass("Enter API key for Voyage AI: ")

embeddings = VoyageAIEmbeddings(model="voyage-3-large")

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )

docs = [doc1]

# Create FAISS vector store
# vector_store = FAISS.from_documents(
#     documents=docs,
#     embedding=embeddings
# )

# Save the FAISS index
# vector_store.save_local("./faiss_langchain_db")

vector_store.add_documents(docs)

vector_store.get(include=['embeddings','documents', 'metadatas'])

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import logging



# ✅ Use Hugging Face's free MiniLM embedding model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ✅ Set up Chroma vector DB
vectordb = Chroma(embedding_function=embedding, persist_directory="db")

def add_to_vectordb(cve_id, description):
    doc = Document(page_content=description, metadata={"cve": cve_id})
    vectordb.add_documents([doc])
    vectordb.persist()  # Save the DB to disk

def search_cve(query):
    return vectordb.similarity_search(query, k=3)

logging.basicConfig(level=logging.WARNING)  # Instead of DEBUG or INFO

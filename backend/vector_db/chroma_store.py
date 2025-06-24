from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = None  # Will be initialized later

def initialize_vectordb_if_needed(texts):
    global vectordb
    if vectordb is None:
        vectordb = FAISS.from_texts(texts, embedding)
    else:
        new_db = FAISS.from_texts(texts, embedding)
        vectordb.merge_from(new_db)

def add_to_vectordb(cve_id, description):
    initialize_vectordb_if_needed([description])

def search_cve(query):
    if vectordb is None:
        return []
    return vectordb.similarity_search(query, k=3)

# Add this at the bottom of your vector_db/faiss_store.py file

def clear_vectordb():
    global vectordb
    vectordb = None


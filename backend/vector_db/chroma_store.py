from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import streamlit as st
import os

# ✅ Cache embedding model to reduce memory usage
@st.cache_resource
def get_embedding():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L3-v2")

embedding = get_embedding()

# ✅ Load from disk if exists, else create empty FAISS
@st.cache_resource
def load_vector_store():
    index_path = "faiss_index"
    if os.path.exists(os.path.join(index_path, "index.faiss")):
        return FAISS.load_local(index_path, embedding)
    else:
        return FAISS.from_texts([], embedding)

vectordb = load_vector_store()

# ✅ Avoid rebuilding entire DB in memory repeatedly
def add_to_vectordb(cve_id, description):
    global vectordb
    new_db = FAISS.from_texts([description], embedding)
    vectordb.merge_from(new_db)
    vectordb.save_local("faiss_index")

def search_cve(query):
    if vectordb is None:
        return []
    return vectordb.similarity_search(query, k=3)

# ✅ Proper clearing + re-saving empty DB
def clear_vectordb():
    global vectordb
    vectordb = FAISS.from_texts([], embedding)
    vectordb.save_local("faiss_index")

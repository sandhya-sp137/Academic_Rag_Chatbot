import faiss
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL


# ✅ Load model only once
@st.cache_resource
def load_model():
    return SentenceTransformer(EMBEDDING_MODEL)


class VectorStore:
    def __init__(self):
        self.model = load_model()   # cached model
        self.index = None
        self.documents = []

    def build_index(self, documents):
        self.documents = documents
        texts = [doc["content"] for doc in documents]

        embeddings = self.model.encode(texts)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype("float32"))

    def search(self, query, top_k=3):
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_vector).astype("float32"), top_k
        )

        return [self.documents[idx] for idx in indices[0]]
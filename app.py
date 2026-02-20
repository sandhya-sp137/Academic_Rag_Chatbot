import streamlit as st
from document_loader import load_documents_from_folder
from vector_store import VectorStore
from rag_engine import answer_question
from ui_components import render_sidebar, render_welcome_message
from config import DATA_FOLDER

st.set_page_config(page_title="Academic RAG Chatbot", layout="wide")

render_welcome_message()
user_role = render_sidebar()

# ✅ Initialize only once
if "vector_store" not in st.session_state:
    documents = load_documents_from_folder(DATA_FOLDER)
    vector_store = VectorStore()
    vector_store.build_index(documents)
    st.session_state.vector_store = vector_store

query = st.text_input("Ask your question:")

if st.button("Submit"):
    if query:
        answer = answer_question(
            query,
            user_role,
            st.session_state.vector_store
        )
        st.markdown("### 🤖 Answer")
        st.write(answer)
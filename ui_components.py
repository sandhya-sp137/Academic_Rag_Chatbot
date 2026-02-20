import streamlit as st
from config import ROLE_ACCESS

def render_sidebar():
    st.sidebar.title("EduIntel AI")
    role = st.sidebar.selectbox("Select Your Role", list(ROLE_ACCESS.keys()))
    return role

def render_welcome_message():
    st.title("🎓 EduIntel AI - Enterprise Academic Knowledge Platform")
    st.markdown("Ask questions related to Campus information. Role-based access enabled.")
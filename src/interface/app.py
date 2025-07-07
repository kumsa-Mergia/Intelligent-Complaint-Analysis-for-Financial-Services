import streamlit as st
import os
import sys

# 🔧 Path setup
project_root = os.path.abspath(os.path.join(os.getcwd(), ""))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.rag.retriever import Retriever
from src.rag.prompt import PromptBuilder
from src.rag.generator import Generator

# Streamlit config
st.set_page_config(page_title="CrediTrust AI", page_icon="💬", layout="wide")

# Dark mode styling
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #0e1117;
            color: #ffffff;
        }
        .stTextInput input {
            background-color: #1e2127;
            color: white;
        }
        .stButton>button {
            background-color: #198754;
            color: white;
            border-radius: 6px;
            height: 3em;
        }
        .stMarkdown code {
            background-color: #1e2127;
        }
    </style>
""", unsafe_allow_html=True)

# Load RAG pipeline components
retriever = Retriever()
prompt_builder = PromptBuilder()
generator = Generator(model_name="google/flan-t5-base")

# Title
st.markdown("## 💬 CrediTrust AI Assistant")
st.caption("A smart assistant for analyzing consumer complaints 🧠")

# Input
question = st.text_input("💡 Type your question:", placeholder="e.g. What are common complaints about credit cards?")

# Buttons
col1, col2 = st.columns([1, 1])
ask_clicked = col1.button("🚀 Ask")
clear_clicked = col2.button("🧹 Clear")

# Session init
if "answer" not in st.session_state:
    st.session_state["answer"] = ""
    st.session_state["sources"] = []
    st.session_state["question"] = ""

#  Clear state
if clear_clicked:
    st.session_state["answer"] = ""
    st.session_state["sources"] = []
    st.session_state["question"] = ""
    st.rerun()

#  Ask question
if ask_clicked and question.strip():
    chunks = retriever.retrieve(question, top_k=3)

    #  Get only the complaint texts
    context_texts = [chunk["text"] if isinstance(chunk, dict) else str(chunk) for chunk in chunks]

    #  Build prompt
    prompt = prompt_builder.build_prompt(context_texts, question)

    #  Generate answer
    answer = generator.generate_answer(prompt)

    #  Store results
    st.session_state["answer"] = answer
    st.session_state["sources"] = chunks
    st.session_state["question"] = question

#  Show answer
if st.session_state.get("answer"):
    st.markdown("### ✅ Answer")
    st.success(st.session_state["answer"])

#  Show sources
if st.session_state.get("sources"):
    st.markdown("### 📚 Source Chunks Used")
    for i, chunk in enumerate(st.session_state["sources"]):
        if isinstance(chunk, dict):
            st.info(f"""
            **Source #{i+1}:**
            - Product: {chunk.get('product', 'N/A')}
            - Complaint ID: {chunk.get('complaint_id', 'N/A')}

            {chunk.get('text', '')}
            """)
        else:
            st.info(f"**Source #{i+1}:**\n\n{chunk}")

# 📎 Footer
st.markdown("---")
st.markdown(
    "<center><small>Built with ❤️ by Kumsa · Powered by Falcon / T5 · RAG Pipeline</small></center>",
    unsafe_allow_html=True
)

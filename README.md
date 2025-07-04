# Intelligent-Complaint-Analysis-for-Financial-Services

This project builds an end-to-end Retrieval-Augmented Generation (RAG) system to analyze and respond to consumer complaints from the CFPB dataset.

## 📌 Tasks Overview

### ✅ Task 1: EDA & Preprocessing

- Load and clean data for 5 selected product categories.
- Remove boilerplate text and empty narratives.
- Save cleaned data to `data/filtered_complaints.csv`.

### ✅ Task 2: Chunking & Embedding

- Break narratives into chunks.
- Use `sentence-transformers/all-MiniLM-L6-v2` for embeddings.
- Store vectors in FAISS/Chroma in `vector_store/`.

### ✅ Task 3: RAG Core Pipeline

- Retrieve top-k similar complaint chunks.
- Prompt LLM to answer user question using retrieved context.
- Evaluate answers using a Q&A evaluation table.

### ✅ Task 4: Interactive App

- A user-friendly Gradio/Streamlit app (`app.py`) to ask questions and view answers with sources.

## 🛠️ Run Instructions

```bash
# Create venv and activate
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run RAG pipeline (sample entry point)
python src/interface/app.py
```

# Intelligent-Complaint-Analysis-for-Financial-Services

This project builds an end-to-end Retrieval-Augmented Generation (RAG) system to analyze and respond to consumer complaints from the CFPB dataset.

## 📌 Tasks Overview

### ✅ EDA & Preprocessing

- Load and clean data for 5 selected product categories.
- Remove boilerplate text and empty narratives.
- Save cleaned data to `data/filtered_complaints.csv`.

### ✅ Chunking & Embedding

- Break narratives into chunks.
- Use `sentence-transformers/all-MiniLM-L6-v2` for embeddings.
- Store vectors in FAISS/Chroma in `vector_store/`.

### ✅ RAG Core Pipeline

- Retrieve top-k similar complaint chunks.
- Prompt LLM to answer user question using retrieved context.
- Evaluate answers using a Q\&A evaluation table.

### ✅ Interactive App

- A user-friendly Gradio/Streamlit app (`app.py`) to ask questions and view answers with sources.

## 📁 Folder Structure

```
├── .github/workflows/
│   └── run-pipeline.yml
├── notebooks/
├── reports/
│   ├── chunking_embedding_choice.md
│   ├── evaluation_table.md
│   └── summary.md
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   └── preprocess.py
│   ├── eda/
│   │   └── exploratory.py
│   ├── embedding/
│   │   ├── chunking.py
│   │   ├── embedder.py
│   │   └── vector_store.py
│   ├── interface/
│   │   └── app.py
│   └── rag/
│       ├── generator.py
│       ├── prompt.py
│       ├── retriever.py
│       └── __init__.py
├── .gitignore
├── README.md
└── requirements.txt
```

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

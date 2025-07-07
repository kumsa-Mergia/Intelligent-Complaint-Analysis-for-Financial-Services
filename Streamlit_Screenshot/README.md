# 📊 Interactive RAG System with Streamlit Interface

This project implements a user-friendly **chat interface** for interacting with a Retrieval-Augmented Generation (RAG) system using **Streamlit**. It enables non-technical users to ask questions and receive answers along with the source documents used by the model for transparency.

---

## 🚀 Features

- 💬 **Text Input Box**: Type in your question to query the RAG system.
- 🔍 **"Ask" Button**: Submit your question for an instant response.
- 📖 **Source Display**: View the source text chunks that support the generated answer, improving trust and verifiability.
- 🔁 **"Clear" Button**: Reset the conversation easily.

---

## 🖼️ Screenshots

### 📌 Streamlit Dashboard

![Screenshot 1](https://drive.google.com/uc?export=view&id=1vxEUfg1WlXfc1LIyaxePP-4ecO1wzSFP)

---

### 💬 Asking a Question

Click the **"Ask"** button after typing your question.
![Screenshot 2](https://drive.google.com/uc?export=view&id=1I07EULmuJOnoNOpvGIHuF1w-cdXz4gLT)

---

### 🧹 Clearing the Response

Use the **"Clear"** button to reset the interface.
![Screenshot 3](https://drive.google.com/uc?export=view&id=1lufWH3jRdm1zqbIBFdEr8Rn1yBt62LKd)

---

### ❓ Asking Another Question

Easily ask follow-up or different questions.
![Screenshot 4](https://drive.google.com/uc?export=view&id=1oEL1cvTKKf8e1c3rv1V21kw4bkSuH0lv)

---

### 🧠 More Examples

Continue exploring the capabilities of the RAG system.
![Screenshot 5](https://drive.google.com/uc?export=view&id=1TM98hjvQYuhkD8cxnrRLQxyGsHiJv4jM)

---

## 📁 File Structure Highlights

- `src/interface/app.py`: Main Streamlit interface
- `src/rag/retriever.py`: Handles document retrieval logic
- `notebooks/vector_store/`: Vector database with document embeddings

---

## ✅ Requirements

- Python 3.8+
- Streamlit
- Langchain (or relevant RAG backend)
- FAISS or Chroma for vector search

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏁 Running the App

```bash
streamlit run .\src\interface\app.py
```

---

# Task 2 – Chunking and Embedding Strategy

## Chunking Strategy

We used LangChain’s `RecursiveCharacterTextSplitter` with:

- `chunk_size`: 256 characters
- `chunk_overlap`: 32 characters

This provided a good balance between retaining sentence context and reducing LLM prompt size.

## Embedding Model

We used the `sentence-transformers/all-MiniLM-L6-v2` model for generating 384-dimensional embeddings. This model is lightweight and fast, while achieving strong performance for semantic similarity.

## Vector Store

We used `FAISS` to store the chunk vectors. Each vector is saved with metadata (original complaint ID, product) to support traceability during retrieval in Task 3.

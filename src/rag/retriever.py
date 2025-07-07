import os
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(
        self,
        index_path: str = None,
        meta_path: str = None,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        # Get the directory of this file (retriever.py)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # If no custom paths given, build absolute paths relative to retriever.py
        if index_path is None:
            index_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'notebooks', 'vector_store', 'index.faiss'))
        if meta_path is None:
            meta_path = os.path.abspath(os.path.join(base_dir, '..', '..', 'notebooks', 'vector_store', 'meta.pkl'))
        
        print(f"Loading FAISS index from: {index_path}")
        print(f"Loading metadata from: {meta_path}")

        # Load FAISS index
        self.index = faiss.read_index(index_path)
        
        # Load metadata (includes text chunks)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)
        
        # Load embedding model
        self.embedder = SentenceTransformer(model_name)

    def retrieve(self, query: str, top_k: int = 5) -> list:
        query_vec = self.embedder.encode([query])
        distances, indices = self.index.search(np.array(query_vec), top_k)
    
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                # Return full metadata dict (including text, product, complaint_id)
                results.append(self.metadata[i])
    
        return results

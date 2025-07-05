import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(
        self,
        index_path: str = "vector_store/index.faiss",
        meta_path: str = "vector_store/meta.pkl",
        model_name: str = "all-MiniLM-L6-v2"
    ):
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

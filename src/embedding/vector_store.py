import faiss
import numpy as np
import pandas as pd
import os
import pickle
from typing import List

class VectorStoreManager:
    def __init__(self, dim: int, index_path="vector_store/index.faiss", meta_path="vector_store/meta.pkl"):
        self.index_path = index_path
        self.meta_path = meta_path
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add_embeddings(self, embeddings: np.ndarray, metadata: List[dict]):
        self.index.add(embeddings)
        self.metadata.extend(metadata)

    def save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(self.index_path)
        with open(self.meta_path, "rb") as f:
            self.metadata = pickle.load(f)

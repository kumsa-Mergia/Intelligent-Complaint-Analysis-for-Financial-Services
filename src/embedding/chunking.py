from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    def __init__(self, chunk_size=256, chunk_overlap=32):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def chunk_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            split_chunks = self.splitter.split_text(text)
            chunks.extend(split_chunks)
        return chunks
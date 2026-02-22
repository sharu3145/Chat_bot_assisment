import os
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from extract_text import extract_text
from chunk_text import chunk_text

# Create vectorstore folder if not exists
os.makedirs("vectorstore", exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(pdf_path):
    print("Extracting text...")
    text = extract_text(pdf_path)

    print("Chunking text...")
    chunks = chunk_text(text)

    print("Creating embeddings...")
    embeddings = model.encode(chunks, show_progress_bar=True)

    dimension = embeddings.shape[1]

    print("Building FAISS index...")
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("✅ Index created successfully!")
    print("Total chunks stored:", len(chunks))


if __name__ == "__main__":
    build_index("data/medical.pdf")
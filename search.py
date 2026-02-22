import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, top_k=3):
    # Load index
    index = faiss.read_index("vectorstore/index.faiss")

    # Load original chunks
    with open("vectorstore/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    # Convert query to embedding
    query_embedding = model.encode([query])

    # Search
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for i in indices[0]:
        results.append(chunks[i])

    return results


if __name__ == "__main__":
    query = "What is CPR?"
    docs = retrieve(query)

    for i, doc in enumerate(docs):
        print(f"\n--- Result {i+1} ---\n")
        print(doc[:500])
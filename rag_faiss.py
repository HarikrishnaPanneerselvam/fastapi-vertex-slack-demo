from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Example troubleshooting notes
notes = [
    "Check API keys for Sentry DSN",
    "Increase timeout for slow endpoints",
    "ZeroDivisionError occurs when dividing by zero",
    "ValueError is raised intentionally",
    "Use try/except to catch errors",
]

# 3. Encode notes into embeddings
embeddings = model.encode(notes)

# 4. Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

print("FAISS mini-RAG index created successfully")

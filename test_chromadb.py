
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent vector database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="cybersecurity_test"
)

# Example cybersecurity documents
documents = [
    "Least privilege limits user permissions.",
    "Multi-factor authentication improves account security.",
    "Audit logging helps detect suspicious activity."
]

# Convert documents to embeddings
embeddings = model.encode(documents).tolist()

# Store documents and vectors
collection.upsert(
    ids=["doc1", "doc2", "doc3"],
    documents=documents,
    embeddings=embeddings
)

# Search using a question
question = "How can we restrict user access?"
query_embedding = model.encode(question).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print("Search results:")
for document in results["documents"][0]:
    print("-", document)

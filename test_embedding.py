
from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example cybersecurity text
text = "Access Control requires least privilege."

# Convert text into a vector
embedding = model.encode(text)

print(f"Vector dimensions: {len(embedding)}")
print(f"First 10 values: {embedding[:10]}")

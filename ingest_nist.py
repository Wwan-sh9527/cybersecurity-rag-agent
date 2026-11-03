
from pathlib import Path
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Load NIST PDF
pdf_path = Path("data/nist_sp_800_53.pdf")
reader = PdfReader(pdf_path)

# 2. Split text into chunks
def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        if chunk.strip():
            chunks.append(chunk)

    return chunks

documents = []
metadatas = []
ids = []

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ""

    for chunk_index, chunk in enumerate(chunk_text(text)):
        documents.append(chunk)
        metadatas.append({
            "source": "NIST SP 800-53 Rev. 5",
            "page": page_number
        })
        ids.append(f"page_{page_number}_chunk_{chunk_index}")

print(f"Prepared {len(documents)} chunks.")

# 3. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 4. Connect to persistent ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="nist_800_53"
)

# 5. Embed and store documents in batches
batch_size = 64

for start in range(0, len(documents), batch_size):
    end = start + batch_size

    batch_documents = documents[start:end]
    batch_embeddings = model.encode(
        batch_documents,
        show_progress_bar=False
    ).tolist()

    collection.upsert(
        ids=ids[start:end],
        documents=batch_documents,
        embeddings=batch_embeddings,
        metadatas=metadatas[start:end]
    )

    print(
        f"Stored {min(end, len(documents))}/{len(documents)} chunks"
    )

print(f"Database contains {collection.count()} chunks.")

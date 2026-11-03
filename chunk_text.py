
from pathlib import Path
from pypdf import PdfReader

pdf_path = Path("data/nist_sp_800_53.pdf")
reader = PdfReader(pdf_path)

# Extract text from every page
pages = [
    page.extract_text() or ""
    for page in reader.pages
]

# Split text into overlapping chunks
def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        if chunk.strip():
            chunks.append(chunk)

    return chunks

# Keep page numbers for future citations
all_chunks = []

for page_number, text in enumerate(pages, start=1):
    for chunk in chunk_text(text):
        all_chunks.append({
            "page": page_number,
            "text": chunk
        })

print(f"Total chunks: {len(all_chunks)}")
print(f"First chunk page: {all_chunks[0]['page']}")
print(f"First chunk preview:\n{all_chunks[0]['text'][:300]}")

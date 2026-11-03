
from pathlib import Path
from pypdf import PdfReader

# Locate the NIST PDF file
pdf_path = Path("data/nist_sp_800_53.pdf")

# Read the PDF
reader = PdfReader(pdf_path)

# Display the number of pages
print(f"Total pages: {len(reader.pages)}")

# Extract text from the first page
first_page = reader.pages[0].extract_text()

print("\n--- First Page Content ---")
print((first_page or "")[:1000])

# Cybersecurity RAG Agent

**A Retrieval-Augmented Generation (RAG) cybersecurity assistant built with Python, ChromaDB, and semantic search, using NIST SP 800-53 as its initial knowledge source.**

This project explores how AI-assisted retrieval can support cybersecurity professionals in researching security controls, interpreting compliance requirements, and identifying relevant security guidance.

The long-term goal is to develop an AI-powered security assistant that combines authoritative NIST documentation with Google Gemini and automated security analysis capabilities.

> **Project Status:** In Development — Document ingestion, embeddings, vector storage, and initial semantic search testing are implemented. NIST-specific retrieval validation and Gemini integration are upcoming.

## 1. Project Objectives

- Build a searchable cybersecurity knowledge base using NIST SP 800-53 Rev. 5.
- Implement semantic retrieval using vector embeddings.
- Develop a RAG pipeline that grounds AI-generated answers in retrieved security documentation.
- Provide traceable source references for cybersecurity recommendations.
- Extend the system to analyze AWS IAM policies against security best practices.

## 2. System Architecture

The project is designed around two main workflows.

**Document Ingestion Pipeline**

```text
NIST SP 800-53 PDF
        |
        v
PDF Text Extraction (pypdf)
        |
        v
Text Chunking
        |
        v
Embedding Generation
(Sentence Transformers)
        |
        v
ChromaDB Vector Database
```

**Question Answering Pipeline (In Development)**

```text
User Security Question
        |
        v
Question Embedding
        |
        v
ChromaDB Semantic Search
        |
        v
Relevant NIST Security Controls
        |
        v
Google Gemini API (Planned)
        |
        v
Grounded Answer + Source References
```

The retrieval component is designed to identify relevant security documentation before the language model generates a response.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| pypdf | PDF text extraction |
| Sentence Transformers | Semantic embedding generation |
| all-MiniLM-L6-v2 | 384-dimensional text embeddings |
| ChromaDB | Persistent vector storage and similarity search |
| Google Gemini API | Planned LLM-based answer generation |
| Streamlit | Planned interactive web interface |
| Git & GitHub | Version control and project documentation |

## 4. Current Implementation

### Document Processing

Implemented PDF extraction using `pypdf` to process NIST SP 800-53 Rev. 5.

- Processed a 492-page NIST publication.
- Extracted text from PDF pages.
- Implemented overlapping text chunking.
- Generated 2,319 text chunks.
- Preserved PDF page numbers as retrieval metadata.

The initial chunking strategy uses 1,000-character chunks with 200-character overlap.

### Semantic Embeddings

Implemented local embedding generation using the `all-MiniLM-L6-v2` model.

- Converted text into 384-dimensional vectors.
- Verified embedding model functionality.
- Generated embeddings for NIST document chunks.

### Vector Database

Implemented persistent vector storage using ChromaDB.

- Created a dedicated `nist_800_53` collection.
- Stored 2,319 NIST text chunks and their embeddings.
- Preserved document source and page metadata.
- Used batch processing for ingestion.
- Implemented upsert operations for repeatable ingestion.

### Semantic Search

Successfully tested semantic similarity search using sample cybersecurity statements.

The NIST-specific retrieval script is the next stage of development and will be evaluated for relevance, source traceability, and retrieval quality.

## 5. Project Structure

```text
cybersecurity-rag-agent/
|
|-- data/                  # Local source documents
|-- read_pdf.py            # PDF extraction test
|-- chunk_text.py          # Text chunking
|-- test_embedding.py      # Embedding model test
|-- test_chromadb.py       # Vector search test
|-- ingest_nist.py         # NIST document ingestion
|-- requirements.txt       # Python dependencies
|-- .gitignore             # Excluded local files
|-- LICENSE
|-- README.md
```

The local `.venv/` environment, `chroma_db/` database, and downloaded PDF files are excluded from version control.

## 6. Installation and Setup

### Prerequisites

- Python 3.12 or another compatible Python version
- Git
- Internet access for initial model download

### Clone the Repository

```bash
git clone https://github.com/Wwan-sh9527/cybersecurity-rag-agent.git
cd cybersecurity-rag-agent
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Download the NIST Document

Download NIST SP 800-53 Rev. 5 from the official NIST publication page:

https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final

Save the PDF as:

```text
data/nist_sp_800_53.pdf
```

Create the `data` directory if it does not exist.

### Run Document Ingestion

```bash
python ingest_nist.py
```

This process extracts text, creates overlapping chunks, generates embeddings, and stores the results in the local ChromaDB database.

### Run the Vector Search Test

```bash
python test_chromadb.py
```

This verifies that semantic similarity search works with sample cybersecurity documents.

## 7. Development Roadmap

- [x] Set up Python development environment
- [x] Implement NIST PDF extraction
- [x] Implement text chunking with overlap
- [x] Generate semantic embeddings
- [x] Configure persistent ChromaDB storage
- [x] Ingest NIST SP 800-53 document chunks
- [x] Validate vector search using sample cybersecurity data
- [ ] Validate NIST-specific semantic retrieval
- [ ] Integrate Google Gemini API
- [ ] Generate answers grounded in retrieved NIST controls
- [ ] Improve source citations and retrieval accuracy
- [ ] Implement AWS IAM policy analysis
- [ ] Introduce agent-based tool orchestration
- [ ] Develop a Streamlit user interface
- [ ] Add automated tests and evaluation metrics

## 8. Planned Security Use Cases

**NIST Control Research**

Retrieve relevant security controls for questions about access management, authentication, audit logging, and system protection.

**AWS IAM Policy Review**

Analyze IAM policies for potentially excessive permissions and compare findings with least-privilege guidance.

**Security Compliance Assistance**

Support preliminary security-control research using authoritative source documents and traceable references.

The assistant is intended as a research and analysis aid, not a replacement for professional security assessment or compliance verification.

## 9. Future Improvements

Planned enhancements include:

- Control-aware document chunking
- Hybrid keyword and vector retrieval
- Retrieval evaluation and relevance scoring
- Structured citations to NIST control identifiers
- Support for additional security frameworks
- Automated IAM policy checks
- Interactive question-answering interface

## 10. References

- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [Google Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

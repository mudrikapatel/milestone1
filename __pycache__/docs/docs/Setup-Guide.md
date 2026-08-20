# Setup Guide

## Intelligent Bug Diagnosis Platform with Fix Recommendation Assistance

This document explains how to install, configure, and run the Intelligent Bug Diagnosis Platform locally.

---

## 1. Prerequisites

Before running the project, make sure the following software is installed:

* Python 3.10 or higher
* Node.js 18 or higher
* npm
* Git
* A code editor such as VS Code
* OpenAI API Key
* GitHub account

Optional:

* Docker
* PostgreSQL
* ChromaDB / FAISS

---

## 2. Clone the Repository

Clone the project repository:

```bash
git clone https://github.com/mudrikapatel/intelligent-bug-diagnosis-platform.git
```

Move into the project directory:

```bash
cd intelligent-bug-diagnosis-platform
```

---

## 3. Backend Setup

Create a Python virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4. Install Backend Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If the project uses a separate backend requirements file:

```bash
cd backend
pip install -r requirements.txt
```

---

## 5. Environment Configuration

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=your_database_url

VECTOR_DB_PATH=./data/vector_store

EMBEDDING_MODEL=text-embedding-3-small

LLM_MODEL=gpt-4o-mini
```

### Important

Do not commit the `.env` file to GitHub.

Add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
node_modules/
```

---

## 6. Historical Defect Dataset Setup

The project uses historical defect datasets for the RAG knowledge base.

Expected sources include:

* Mozilla
* Apache
* Eclipse

Place the downloaded datasets in:

```text
datasets/
```

Example:

```text
datasets/
├── mozilla/
├── apache/
└── eclipse/
```

Dataset files should not contain confidential or sensitive information.

---

## 7. Build the Knowledge Base

Run the preprocessing pipeline:

```bash
python scripts/preprocess_data.py
```

Run chunking:

```bash
python scripts/chunk_data.py
```

Generate embeddings:

```bash
python scripts/generate_embeddings.py
```

Index the data:

```bash
python scripts/index_vector_store.py
```

After successful execution, the vector database will contain the processed historical defects.

> Update these commands if the final implementation uses different script names.

---

## 8. Start the Backend

Run the FastAPI backend:

```bash
uvicorn backend.main:app --reload
```

The backend will normally be available at:

```text
http://localhost:8000
```

API documentation can be accessed through:

```text
http://localhost:8000/docs
```

---

## 9. Frontend Setup

Open a new terminal.

Move into the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:3000
```

---

## 10. Running the Complete System

The complete workflow is:

```text
Start Backend
      ↓
Start Frontend
      ↓
Submit Bug Report
      ↓
Triage Agent
      ↓
Log Analysis Agent
      ↓
RAG Retrieval
      ↓
Root Cause Agent
      ↓
Duplicate Detection Agent
      ↓
Remediation Agent
      ↓
Structured Findings
      ↓
Analytics
```

---

## 11. Basic Verification

After starting the application:

1. Open the frontend.
2. Submit a sample bug report.
3. Verify that the submission is accepted.
4. Verify Triage Agent output.
5. Verify Log Analysis Agent output.
6. Verify historical defect retrieval.
7. Verify root-cause analysis.
8. Verify duplicate detection.
9. Verify remediation recommendation.
10. Verify results are displayed in the findings interface.

---

## 12. Troubleshooting

### API Key Error

Check that:

```env
OPENAI_API_KEY=your_api_key
```

is correctly configured.

### Vector Database Error

Re-run the knowledge-base indexing process:

```bash
python scripts/index_vector_store.py
```

### Dependency Error

Update pip:

```bash
python -m pip install --upgrade pip
```

Then reinstall:

```bash
pip install -r requirements.txt
```

### Frontend Dependency Error

Run:

```bash
npm install
```

again inside the frontend directory.

---

## 13. Security

The following information must never be committed to GitHub:

* API keys
* Passwords
* Database credentials
* Access tokens
* Private datasets
* Personal information

Use `.env` for local configuration.

---

## 14. Project URLs

After local setup:

| Service           | URL                          |
| ----------------- | ---------------------------- |
| Frontend          | `http://localhost:3000`      |
| Backend           | `http://localhost:8000`      |
| API Documentation | `http://localhost:8000/docs` |

---

## 15. Setup Completion Criteria

The setup is considered successful when:

* Backend starts successfully.
* Frontend starts successfully.
* Historical defect data is indexed.
* Vector search works.
* A bug can be submitted.
* Agents can process the submission.
* Structured findings are displayed.

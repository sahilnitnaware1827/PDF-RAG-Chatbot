# 📄 PDF RAG Chatbot

An AI-powered PDF Question Answering chatbot built using **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Google Gemini 2.5 Flash**. The chatbot retrieves relevant information from a PDF using **Retrieval-Augmented Generation (RAG)** and answers questions based only on the document's content.

---

## 🚀 Features

- 📄 Load PDF documents
- ✂️ Split documents into text chunks
- 🧠 Generate embeddings using HuggingFace Sentence Transformers
- 💾 Store embeddings in FAISS Vector Database
- 🔍 Retrieve the most relevant document chunks
- 🤖 Generate answers using Google Gemini 2.5 Flash
- 🏗️ Modular project structure using LangChain

---

# 🧠 RAG Workflow

```text
                OFFLINE (Ingestion)

PDF Document
      │
      ▼
PyPDFLoader
      │
      ▼
RecursiveCharacterTextSplitter
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Vector Database

----------------------------------------------

                 ONLINE (Chat)

User Question
      │
      ▼
Load FAISS Database
      │
      ▼
Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt Template
      │
      ▼
Google Gemini 2.5 Flash
      │
      ▼
Generated Answer
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| Framework | LangChain |
| LLM | Google Gemini 2.5 Flash |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| PDF Loader | PyPDFLoader |
| Text Splitter | RecursiveCharacterTextSplitter |
| Environment | python-dotenv |

---

# 📂 Project Structure

```text
pdf-rag-chatbot/
│
├── documents/
│   └── company.pdf
│
├── services/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── prompt.py
│   └── llm.py
│
├── chatbot.py
├── ingestion.py
├── retrieval.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

> **Note:** The `faiss_db/` folder is generated automatically after running `ingestion.py` and is intentionally excluded from Git.

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-rag-chatbot.git

cd pdf-rag-chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv

.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

### Step 1 : Build the Vector Database

```bash
python ingestion.py
```

This will:

- Load the PDF
- Create document chunks
- Generate embeddings
- Store vectors inside the FAISS database

---

### Step 2 : Start the Chatbot

```bash
python chatbot.py
```

Example:

```text
Ask Question >>> What services does the company provide?

Answer:
...
```

---

# 📚 Concepts Used

- Retrieval-Augmented Generation (RAG)
- LangChain
- Semantic Search
- Vector Embeddings
- FAISS Vector Database
- Prompt Engineering
- Google Gemini API

---

# 🔒 Security

- `.env` is excluded from Git.
- `faiss_db/` is excluded from Git because it is generated automatically.
- Store API keys only inside the `.env` file.

---

# 🚀 Future Improvements

- Streamlit UI
- FastAPI API
- Multiple PDF support
- Conversation memory
- Metadata filtering
- Docker deployment
- Support DOCX and Excel documents

---

# 👨‍💻 Author

**Sahil Nitnaware**

- GitHub: https://github.com/sahilnitnaware
- LinkedIn: https://linkedin.com/in/sahilnitnaware

---

# 📄 License

This project is licensed under the MIT License.
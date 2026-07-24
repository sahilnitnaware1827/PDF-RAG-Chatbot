📄 PDF RAG Chatbot

An AI-powered chatbot that answers questions from any PDF document using Retrieval-Augmented Generation (RAG). Built with LangChain, FAISS, HuggingFace Sentence Transformers, and Google Gemini 2.5 Flash.
---

🚀 What It Does

Upload any PDF → Ask questions in plain English → Get accurate, context-aware answers.
The chatbot does not hallucinate. It answers only from the content of your PDF. If the answer isn't in the document, it replies: "I don't know."
---

🧠 How It Works (RAG Pipeline)

```
📄 PDF Document
      ↓
  Load Pages          (PyPDFLoader)
      ↓
  Split into Chunks   (RecursiveCharacterTextSplitter)
      ↓
  Generate Embeddings (HuggingFace all-MiniLM-L6-v2)
      ↓
  Store in FAISS DB   (Vector Database)

          ⬇ ── Ingestion Complete ── ⬇

  User Question
      ↓
  Embed Question      (same embedding model)
      ↓
  Similarity Search   (FAISS — top 3 chunks)
      ↓
  Build Prompt        (context + question)
      ↓
  Send to Gemini LLM  (Google Gemini 2.5 Flash)
      ↓
  Final Answer ✅
```

---
🛠️ Tech Stack

Category	Technology
Language	Python 3.11
LLM	Google Gemini 2.5 Flash
Orchestration	LangChain
Embeddings	HuggingFace `sentence-transformers/all-MiniLM-L6-v2`
Vector Database	FAISS (Facebook AI Similarity Search)
PDF Loader	PyPDFLoader (LangChain Community)
Text Splitter	RecursiveCharacterTextSplitter
Environment	python-dotenv

---
📁 Project Structure

```
pdf-rag-chatbot/
│
├── services/
│   ├── __init__.py         # Package initializer
│   ├── loader.py           # Load PDF using PyPDFLoader
│   ├── chunker.py          # Split documents into chunks
│   ├── embeddings.py       # Load HuggingFace embedding model
│   ├── vector_store.py     # Store embeddings in FAISS
│   ├── llm.py              # Google Gemini LLM integration
│   └── prompt.py           # Prompt template for RAG
│
├── documents/
│   └── company.pdf         # Your PDF document (place here)
│
├── faiss_db/               # Auto-created after running ingest.py
│
├── ingest.py               # Step 1: Load, chunk, embed, store
├── retrieval.py            # Step 2: Retrieve relevant chunks
├── chatbot.py              # Step 3: Chat interface
│
├── .env                    # API keys (not pushed to GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```
---
⚙️ Setup & Installation

1. Clone the Repository
```bash

git clone https://github.com/yourusername/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

2. Create Virtual Environment
```bash

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

```

3. Install Dependencies
```bash

pip install -r requirements.txt

```

4. Set Up Environment Variables
Create a `.env` file in the root folder:

```env

GOOGLE_API_KEY=your_google_api_key_here

```

Get your free API key at: aistudio.google.com

5. Add Your PDF

Place your PDF file inside the `documents/` folder and update the path in `ingest.py`:

```python

pdf_path = "documents/your_file.pdf"

```

---
▶️ How to Run

Step 1 — Ingest the PDF (run once)

```bash

python ingest.py

```
Expected output:

```

Loading PDF...

Loaded 7 pages
Creating Chunks...
Created 42 chunks
Loading Embedding Model...
The final Result: Data has been stored Successfully
```

Step 2 — Start the Chatbot
```bash

python chatbot.py

```

Step 3 — Ask Questions
```

Ask question >>> Who is the CEO of the company?
Ask question >>> What products does the company offer?
Ask question >>> What is the pricing for the Growth plan?
Ask question >>> exit

```

---

💡 Key Concepts Used

Retrieval-Augmented Generation (RAG)
Instead of relying on the LLM's training data, RAG retrieves relevant information directly from your document and provides it as context to the LLM. This eliminates hallucination and keeps answers accurate and up-to-date.
Vector Embeddings
Text is converted into numerical vectors using a sentence transformer model. Similar meaning = similar vectors. This allows semantic search rather than keyword matching.
FAISS (Vector Database)
Facebook AI Similarity Search — stores embedding vectors and retrieves the most similar ones based on a user's query in milliseconds, even across millions of vectors.
Chunk Overlap
Documents are split into overlapping chunks so that context is not lost at chunk boundaries. Chunk size: 500 characters, overlap: 20 characters.

---

🔒 Security Notes
Never commit your `.env` file to GitHub
The `.gitignore` file already excludes `.env` and `faiss_db/`
API keys should always be loaded via environment variables

---

🔮 Future Improvements
[ ] Add Streamlit UI for browser-based chat interface
[ ] Support multiple PDF uploads at once
[ ] Add conversation memory (chat history)
[ ] Stream LLM responses token by token
[ ] Add FastAPI wrapper to expose as REST API
[ ] Dockerize for easy deployment
[ ] Support DOCX, Excel, and web page ingestion

---

📚 What I Learned
How RAG (Retrieval-Augmented Generation) works end-to-end
Building modular Python service architecture
Working with vector databases (FAISS) and embeddings
Integrating LLMs via LangChain (Google Gemini)
Managing API keys securely with `.env`
Chunking strategies for document processing

---

🙋 Author
Sahil Nitnaware
GitHub: github.com/sahilnitnaware
Email: sahilnitnaware71@gmail.com
LinkedIn: linkedin.com/in/sahilnitnaware

---

📄 License
This project is open source and available under the MIT License.

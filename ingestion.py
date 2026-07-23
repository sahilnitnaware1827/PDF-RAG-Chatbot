from services.loader import load_document
from services.chunker import create_chunks


'''
    Load Document
'''
pdf_path = r"D:\Codes\Python\RAG_PROJECT\pdf-rag-chatbot\documents\company.pdf"

documents = load_document(pdf_path)


'''
    Create Chunk
'''

chunks = create_chunks(documents)



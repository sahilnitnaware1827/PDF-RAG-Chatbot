from services.loader import load_document
from services.chunker import create_chunks
from services.embeddings import get_embedding_model
from services.vector_store import vector_Database


'''
    Load Document
'''
pdf_path = r"D:\Codes\Python\RAG_PROJECT\pdf-rag-chatbot\documents\company.pdf"

documents = load_document(pdf_path)


'''
    Create Chunk
'''

chunks = create_chunks(documents)

'''
    get embedding model
'''
embedding_model = get_embedding_model()


'''
    Store documents in DataBase
'''

result = vector_Database(chunks, embedding_model)

print("\n The final Result : ", result)

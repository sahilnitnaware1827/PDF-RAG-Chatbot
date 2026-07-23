# wap to load document using langchain
from langchain_community.document_loaders import PyPDFLoader

def load_document(filepath):

    loader= PyPDFLoader(filepath)

    return loader.load()

# wap to load document using langchain
from langchain_community.document_loaders import TextLoader

def load_ducument(filepath):

    loader= TextLoader(filepath)

    return loader.load()

# wap to create chunks using langchain

from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(document):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 20
    )

    chunks =  text_splitter.split_documents(document)

    return chunks

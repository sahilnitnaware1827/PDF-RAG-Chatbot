# wap to create embeddding model

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model = "sentence-transformer/all-MiniLM-L6-v2"
)


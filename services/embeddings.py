# wap to create embeddding model

from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():

    embed_model = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )

    return embed_model

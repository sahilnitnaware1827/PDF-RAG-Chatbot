# wap to put data into database


from langchain_community.vectorstores import FAISS

def vector_Database(documents, embedding_model):
    db = FAISS.from_documents(
        documents= documents,
        embedding= embedding_model
    )

    db.save_local("faiss_db")

    return " Data has been stored Successfully"

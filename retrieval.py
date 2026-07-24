# wap to retrive the data from saved data base 

from services.embeddings import get_embedding_model
from langchain_community.vectorstores import FAISS

def retrive_relavent_data(question):

    '''
        load embedding model
    '''
    embedding_model = get_embedding_model()


    '''
        load faiss saved model
    '''
    db = FAISS.load_local(
        "faiss_db",
        embeddings= embedding_model,
        allow_dangerous_deserialization=True
        )


    '''
        Create Retriever
    '''
    retriever = db.as_retriever(
        search_type = "similarity",
        search_kwargs = {"k": 3}
    )


    '''
        retrieve similar contex from database
    '''

    context = retriever.invoke(question)

    return context

# load llm 

from langchain_google_genai import ChatGoogleGenerativeAI



def get_response(prompt):
    # load llm model 
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature = 0
    )

    response = llm.invoke(prompt)

    return response

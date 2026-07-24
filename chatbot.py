# wap to Create ChatBot 

from retrieval import retrive_relavent_data
from services.prompt import create_prompt
from services.llm import get_response
from dotenv import load_dotenv

# load llm model
load_dotenv()


while True:

    # take question from user
    question = input('\n Ask question >>> ')

    # retrive related document from vector DataBase
    relevent_doc = retrive_relavent_data(question)

    # generate prompt for LLM model
    prompt = create_prompt(relevent_doc, question)

    # fill the place-holder using invoke method
    final_prompt = prompt.invoke(
        {
            "context": relevent_doc,
            "question": question
        }
    )

    # generate response from llm 
    response = get_response(final_prompt)

    # print response
    print(response.content)
    
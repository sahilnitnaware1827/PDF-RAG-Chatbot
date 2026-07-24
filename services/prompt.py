# create prompt template 

from langchain_core.prompts import PromptTemplate

def create_prompt():

    prompt = PromptTemplate.from_template(
        """
            You are an AI Assistant.

            Answer ONLY using the provided context.

            If the answer is not present in the context,
            reply with "I don't know."

            Context:
            {context}

            Question:
            {question}

        """
    )

    return prompt

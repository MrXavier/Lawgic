from typing import Dict, List
import os
from dotenv import load_dotenv

from langchain_google_vertexai import ChatVertexAI

load_dotenv()

def get_llm_completion(prompt:str) -> str:

    return get_lchain_llm_completion(prompt)


def get_lchain_llm_completion(prompt:str) -> str:
    try:
        input_messages = [
            (
                "system",
                "You are a helpful and experienced lawyer. Answer the user question based on the provided context.",
            ),
            ("human", prompt),
        ]
        # print(" -- input_messages: ", input_messages)
        chatbot = ChatVertexAI(
            model="gemini-1.5-flash-001",
            temperature=0,
            max_tokens=None,
            max_retries=6,
            stop=None,
        )
        completion = chatbot.invoke(input_messages)
        # print(" -- completion: ", completion)
        return completion.content
        
    except Exception as e:
        print(f"Error getting LLM completion: {str(e)}")
        return ""

# print(get_llm_completion("Can a 16 year old person stir or drive a boat?"))

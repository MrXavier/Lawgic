import os
from typing import Dict, List

from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI

load_dotenv()

def get_llm_completion(messages: List[Dict]) -> str:
    try:
        # Call completion API endpoint
        response = {
            "completion": "This is a mock completion. Replace with actual API call.",
            "model": "gpt-3.5-turbo",
            "messages": messages
        }
        
        return response["completion"]
        
    except Exception as e:
        print(f"Error getting LLM completion: {str(e)}")
        return ""

def get_lchain_llm_completion(messages: List[Dict]) -> str:
    try:
        input_messages = [
            (
                "system",
                "You are a helpful assistant that translates English to French. Translate the user sentence.",
            ),
            ("human", "I love programming."),
        ]
        chatbot = ChatVertexAI(
            model="gemini-1.5-flash-001",
            temperature=0,
            max_tokens=None,
            max_retries=6,
            stop=None,
        )
        completion = chatbot.get_completion(input_messages)
        return completion
        
    except Exception as e:
        print(f"Error getting LLM completion: {str(e)}")
        return ""
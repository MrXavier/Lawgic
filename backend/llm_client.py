from typing import Dict, List
import os
from dotenv import load_dotenv

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

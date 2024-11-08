from typing import Dict, List
from repository import get_relevant_context
from llm_client import get_llm_completion

def get_completion_response(model: str, messages: List[Dict]) -> Dict:
    prompt = messages[1].get('content')
    
    context = get_relevant_context(prompt)
    # print(" -- context: ", context)
    prompt = "German law:\n" + context + "\n---\nBased on the German law above, answer the following question: " + prompt
    print(" -- prompt: ", prompt)
    completion = get_llm_completion(prompt)
    
    return {
        "completion": completion,
        "messages": messages
    }

def get_chatbot_response(message: str) -> Dict:
    # TODO: Implement actual chatbot logic
    reply = "This is a sample chatbot response. Replace with actual chatbot logic."
    
    return {
        "reply": reply,
        "message": message
    }

from typing import Dict, List
from repository import get_relevant_context
from llm_client import get_llm_completion

def get_completion_response(model: str, messages: List[Dict]) -> Dict:
    context = get_relevant_context(messages[1].get('content')) # get assistant message
    messages[1]['content'] = "Context:\n" + context + "\n---\nBased on the above context, answer the following question: " + messages[1]['content']
    completion = get_llm_completion(messages)
    
    return {
        "completion": completion,
        "model": model,
        "messages": messages
    }

def get_chatbot_response(message: str) -> Dict:
    # TODO: Implement actual chatbot logic
    reply = "This is a sample chatbot response. Replace with actual chatbot logic."
    
    return {
        "reply": reply,
        "message": message
    }

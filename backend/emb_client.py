import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_embedding(text: str) -> dict:
    """
    Gets embedding from Google Cloud AI Platform Prediction API
    
    Args:
        text: Input text to get embedding for
        
    Returns:
        Response from the API endpoint
    """
    try:
        url = "https://europe-west1-prediction-aiplatform.clients6.google.com/ui/projects/1034507428097/locations/europe-west1/endpoints/329382897356111872:predict"
        params = {
            "key": "AIzaSyCI-zsRP85UVOi0DjtiCwWBwQ1djDy741g"
        }
        
        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "authorization": "Bearer " + os.getenv("GOOGLE_AUTH_TOKEN"),
            "x-goog-authuser": "0"
        }

        data = {
            "instances": [{
                "inputs": text
            }]
        }

        response = requests.post(url, params=params, headers=headers, json=data)
        if response.json().get("error") is not None:
            print(" -- error calling embedings - response: ", response.json())
        return response.json()

    except Exception as e:
        print(f"Error getting embedding: {str(e)}")
        return {}

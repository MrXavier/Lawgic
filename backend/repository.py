from emb_client import get_embedding
import requests

def get_relevant_context(question: str) -> str:
    """
    Retrieves relevant text chunks from Milvus vector DB based on input message
    and builds a context string from the chunks.
    
    Args:
        message: Input message to find relevant context for
        
    Returns:
        String containing concatenated relevant text chunks as context
    """
    try:
        embedding_resp = get_embedding(question)
        embedding = embedding_resp.get("predictions")[0]
        # print(" -- embedding:", embedding)

        search_results = search_vectors(embedding)
        # print(" -- search_results:", search_results)
        
        results = ["Sample text chunk", "Another sample text chunk", "A third sample text chunk"]
        # Build context from retrieved chunks
        context = ""
        for hit in results:
            chunk_text = hit
            if chunk_text:
                context += chunk_text + "\n\n"
                
        return context.strip()
        
    except Exception as e:
        print(f"Error retrieving context: {str(e)}")
        return ""


def search_vectors(data: list) -> dict:
    """
    Searches for vectors in Zilliz cloud using the provided data
    
    Args:
        data: Vector data to search with
        
    Returns:
        Search results from Zilliz cloud
    """
    try:
        url = "https://in05-24d6ba4a10ba788.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/entities/search"
        
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer 947d431def2443a76801786c91ae4a7e3bdb593181385ac201cf2582de95bd513b06d927e9415ba185227b905158456d7d2b2789",
            "Content-Type": "application/json"
        }

        payload = {
            "collectionName": "Laws",
            "data": data,
            "limit": 10,
            "outputFields": ["*"]
        }
        # print(" -- payload:", payload)

        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    except Exception as e:
        print(f"Error searching vectors: {str(e)}")
        return {}


## Paragraph
# Sample text chunk. Another sample text chunk. A third sample text chunk.

# vector: Sample text chunk.
# metadata: {"paragraph": "Sample text chunk. Another sample text chunk. A third sample text chunk."}

# vector: Another sample text chunk.
# metadata: {"paragraph": "Sample text chunk. Another sample text chunk. A third sample text chunk."}

# vector: A third sample text chunk.
# metadata: {"paragraph": "Sample text chunk. Another sample text chunk. A third sample text chunk."}
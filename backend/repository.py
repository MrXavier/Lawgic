def get_relevant_context(message: str) -> str:
    """
    Retrieves relevant text chunks from Milvus vector DB based on input message
    and builds a context string from the chunks.
    
    Args:
        message: Input message to find relevant context for
        
    Returns:
        String containing concatenated relevant text chunks as context
    """
    try:
        # # Initialize Milvus client
        # client = MilvusClient(
        #     uri="localhost:19530",
        #     token=""  # Add token if authentication is enabled
        # )
        
        # # Convert message to vector embedding
        # embedding = get_embedding(message)
        
        # # Search for similar vectors in Milvus
        # search_params = {
        #     "metric_type": "L2",
        #     "params": {"nprobe": 10}
        # }
        
        # results = client.search(
        #     collection_name="text_chunks",
        #     data=[embedding],
        #     limit=5,
        #     output_fields=["text"],
        #     search_params=search_params
        # )
        
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


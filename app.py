import os
import openai
import faiss
import requests
import numpy as np
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fetch_books import fetch_books
from extract_intent import extract_intent
from dotenv import load_dotenv
import json
# Load .env file
load_dotenv()

# Get API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OpenAI API Key is missing! Check your .env file.")

print(f"✅ OpenAI API Key Loaded: {OPENAI_API_KEY[:5]}... (Masked)")

# build recommend agent 
app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all request methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all request headers
)


@app.get("/recommend")
def recommend_books(query: str):
    """Returns book recommendations based on user query."""
    try:
        # Extract intent from user query
        extracted_intent = extract_intent(query)
        print(f"Extracted Intent: {extracted_intent}")

        # Fetch books based on extracted preferences
        books = fetch_books(extracted_intent)
        if not books:
            return {"message": "No books found for your query.", "extracted_intent": extracted_intent}

        # Generate embeddings for book descriptions
        embeddings = OpenAIEmbeddings()
        book_descriptions = [book["description"] for book in books if book["description"] != "No description available"]
        if not book_descriptions:
            return {"message": "No sufficient book descriptions available for recommendations.", "extracted_intent": extracted_intent}

        book_vectors = embeddings.embed_documents(book_descriptions)

        # Create FAISS index for search
        index = faiss.IndexFlatL2(len(book_vectors[0]))
        index.add(np.array(book_vectors))

        # Convert user query into vector
        query_vector = embeddings.embed_query(query)
        _, indices = index.search(np.array([query_vector]), k=5)
        recommended_books = [books[i] for i in indices[0] if i < len(books)]

        # Generate response using GPT
        messages = [
            SystemMessage(content="You are a helpful book recommendation assistant."),
            HumanMessage(content=f"I liked {query}. Can you recommend similar books? Here are some options: {recommended_books}"),
        ]
        llm = ChatOpenAI(model_name="gpt-4")
        response = llm.invoke(messages)  # Use `invoke()` instead of `__call__()`

        # Ensure response content is a string before returning
        final_response = {
            "extracted_intent": extracted_intent,
            "recommendations": recommended_books,
            "summary": response.content.strip() if hasattr(response, "content") else str(response)
        }

        print("Final Response:", json.dumps(final_response, indent=4))  # Debugging
        return final_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from fastapi import FastAPI, HTTPException


# NLP Agent: Uses GPT-4 to analyze and extract book genre, author, and themes.

def extract_intent(user_query):
    messages = [
        SystemMessage(content="You are an AI that extracts book-related user intent."),
        HumanMessage(content=f"User Query: {user_query}\nExtract the genre, author, or themes the user is interested in.")
    ]
    llm = ChatOpenAI(model="gpt-4o")
    response = llm.invoke(messages)
    return response.content.strip()
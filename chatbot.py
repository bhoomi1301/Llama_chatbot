import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
API_KEY = st.secrets.get("GROQ_API_KEY", None)

if API_KEY is None:
    api_key = os.getenv("GROQ_API_KEY")

# Groq endpoint and model
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"

def chat_with_llama(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": messages
    }
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

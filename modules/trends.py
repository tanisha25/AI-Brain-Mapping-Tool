import streamlit as st
import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def analyze_market_trends(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Analyze market trends for a business idea."},
            {"role": "user", "content": f"What are the latest market trends for {idea}?"}
        ]
    )
    return response['choices'][0]['message']['content']

def run(idea):
    st.subheader("📊 Market Trends")
    st.write(analyze_market_trends(idea))
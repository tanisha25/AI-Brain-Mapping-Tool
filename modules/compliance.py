import streamlit as st
import openai
import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def get_regulatory_requirements(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Provide key compliance regulations for a given {idea}."},
            {"role": "user", "content": f"What are the compliance regulations for {idea}?"}
        ]
    )
    return response['choices'][0]['message']['content']

def run(idea):
    st.subheader("📜 Compliance & Regulations")
    if idea:
        regulations = get_regulatory_requirements(idea)
        st.write(f"Regulatory Requirements for {idea}: {regulations}")

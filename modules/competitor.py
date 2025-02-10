import streamlit as st
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
def get_competitor_analysis(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Analyze competitors in a business domain."},
            {"role": "user", "content": f"Who are the main competitors for {idea}?"}
        ]
    )
    return response['choices'][0]['message']['content']

def run(idea):
    st.subheader("🔍 Competitor Analysis")
    st.write(get_competitor_analysis(idea))
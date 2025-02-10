import streamlit as st
import openai
from dotenv import load_dotenv
import os
load_dotenv()

def generate_monetization_strategies(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Suggest monetization strategies for a business idea."},
            {"role": "user", "content": f"What are the best monetization strategies for {idea}?"}
        ]
    )
    return response['choices'][0]['message']['content']

def run(idea):
    st.subheader("💵 Monetization Strategies")
    st.write(generate_monetization_strategies(idea))
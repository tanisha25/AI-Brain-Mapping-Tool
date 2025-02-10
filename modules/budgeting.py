import streamlit as st
import openai
from dotenv import load_dotenv
import os
load_dotenv()

def analyze_revenue_model(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Provide insights on the revenue model based on the business idea."},
            {"role": "user", "content": f"Give revenue model insights for {idea}."}
        ]
    )
    return response['choices'][0]['message']['content']

def run(idea):
    st.subheader("💰 Budgeting & Revenue Model Analysis")
    st.write(analyze_revenue_model(idea))

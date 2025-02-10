import streamlit as st
import modules.ai_utils as ai_utils

def run(idea):
    st.subheader("🤖 AI-Generated Insights")
    if idea:
        result = ai_utils.generate_text(f"Provide insights on {idea}")
        st.write(result)

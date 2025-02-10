import streamlit as st
import modules.mindmap as mindmap
import modules.research as research
import modules.ai_insights as ai_insights
import modules.trends as trends
import modules.prototype as prototype
import modules.budgeting as budgeting
import modules.monetization as monetization
import modules.competitor as competitor
import modules.compliance as compliance
import modules.ai_utils as ai_utils

def main():
    st.set_page_config(page_title="AI Brain Mapping Tool", layout="wide")
    st.title("🚀 AI-Powered Brain-Mapping and Visualization Tool")

    idea = st.text_input("Enter your business idea (used for all features):")

    if idea:
        col1, col2 = st.columns(2)

        with col1:
            with st.status("Generating Mind Map... ⏳", expanded=True):
                mindmap.run(idea)

            with st.status("Fetching Research Papers... 📄", expanded=True):
                research.run(idea)

            with st.status("Generating AI Insights... 🤖", expanded=True):
                ai_insights.run(idea)
            
            with st.status("Analyzing Market Trends... 📊", expanded=True):
                trends.run(idea)

        with col2:

            with st.status("Performing Budget Analysis... 💰", expanded=True):
                budgeting.run(idea)

            with st.status("Calculating Monetization Strategies... 💡", expanded=True):
                monetization.run(idea)

            with st.status("Evaluating Competitors... 🔍", expanded=True):
                competitor.run(idea)

            
            with st.status("Evaluating Compliance... 🔍", expanded=True):
                compliance.run(idea)
if __name__ == "__main__":
    main()

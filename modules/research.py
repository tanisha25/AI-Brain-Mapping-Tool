import streamlit as st
from scholarly import scholarly
import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
def search_research_papers(query):
    search_query = scholarly.search_pubs(query)
    papers = []
    try:
        for _ in range(3):
            papers.append(next(search_query))
    except StopIteration:
        pass
    return papers

def extract_insights(paper):
    abstract = paper['bib'].get('abstract', 'No abstract available')

    if abstract == "No abstract available":
        return abstract

    # Use OpenAI to summarize the abstract into a one-liner
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize the given abstract in a single impactful sentence."},
            {"role": "user", "content": abstract}
        ],
        max_tokens=30
    )

    return response['choices'][0]['message']['content'].strip()

def run(idea):
    st.subheader("📄 Research Paper Insights")
    if idea:
        papers = search_research_papers(idea)
        for paper in papers:
            st.write(f"[**{paper['bib']['title']}**]({paper.get('pub_url', '#')})")
            st.write(f"**Key Insights:** {extract_insights(paper)}")

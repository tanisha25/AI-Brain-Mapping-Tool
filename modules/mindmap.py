import openai
import networkx as nx
from pyvis.network import Network
import streamlit as st
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_bpmn_steps(idea):
    """Generate key workflow steps in short, structured phrases."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Generate workflow steps in 2-3 word phrases."},
                {"role": "user", "content": f"Generate BPMN steps for {idea} with dependencies in short phrases relevant to the domain. Involve maximum high level 10 steps."}
            ]
        )

        steps_text = response['choices'][0]['message']['content']
        steps = [step.strip() for step in steps_text.split("\n") if step.strip()]
    
        structured_steps = []
        previous_step = None

        for step in steps:
            if previous_step:
                structured_steps.append((previous_step, step))
            previous_step = step

        return structured_steps

    except Exception as e:
        st.error(f"Error generating BPMN steps: {str(e)}")
        return []

def create_graph(steps):
    """Create a directed graph from BPMN steps."""
    G = nx.DiGraph()

    for i, (start, end) in enumerate(steps):
        color = "dodgerblue" if i < len(steps) - 1 else "limegreen"

        G.add_node(start, color="dodgerblue", size=40)
        G.add_node(end, color=color, size=40)
        G.add_edge(start, end, label="Next Step")

    return G

def visualize_graph(G):
    """Render the NetworkX graph using PyVis with larger fonts, bold labels, and fixed zoom."""
    net = Network(height="750px", width="100%", directed=True, notebook=False)

    for node, data in G.nodes(data=True):
        net.add_node(
            node, 
            label=node, 
            color=data.get("color", "blue"), 
            size=data.get("size", 40), 
            font={"size": 22, "color": "black", "bold": True}
        )

    for source, target, data in G.edges(data=True):
        net.add_edge(source, target, title=data.get("label", ""), length=180, arrows="to")

    # Improved Visualization Settings
    net.set_options('''
    var options = {
      "interaction": {
        "zoomView": false, 
        "dragView": false
      },
      "physics": {
        "enabled": false,
        "solver": "forceAtlas2Based",
        "stabilization": { "enabled": false, "iterations": 1000 }
      }
    }
    ''')

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
        html_file = tmpfile.name
        net.write_html(html_file)

    return html_file

def run(idea):
    """Generate and visualize the BPMN-style workflow."""
    st.subheader(f"📌 Business Workflow for: {idea}")

    steps = generate_bpmn_steps(idea)
    if not steps:
        st.warning("⚠️ No steps generated. Please try again with a different idea.")
        return

    G = create_graph(steps)
    html_file = visualize_graph(G)

    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=750)

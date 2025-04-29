import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dotenv import load_dotenv
from together import Together
from prompts import critic_prompt, defender_prompt, arbiter_prompt
from config import TOGETHER_MODELS
from utils.rag_context import build_context
from agents.agent1 import run_defender
from agents.agent2 import run_prosecutor
from agents.agent3 import run_judge

# Load API Key
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

# Streamlit UI
st.title("⚖️ Agentic Courtroom - RAG LLM Simulation")

if st.button("Run Courtroom Simulation"):
    with st.spinner("Building context from legal documents..."):
        context = build_context("data/constitution.pdf", "data/case_reports")

    with st.spinner("Agent 1 (Defense Lawyer) preparing argument..."):
        defense = run_defender(context, client)
        st.subheader("🧑‍⚖️ Defense Lawyer's Argument")
        st.write(defense)

    with st.spinner("Agent 2 (Prosecutor) preparing argument..."):
        prosecution = run_prosecutor(context, client)
        st.subheader("👨‍⚖️ Prosecutor's Argument")
        st.write(prosecution)

    with st.spinner("Judge (Agent 3) deciding verdict..."):
        verdict = run_judge(defense, prosecution, context, client)
        st.subheader("⚖️ Final Verdict by Judge")
        st.write(verdict)

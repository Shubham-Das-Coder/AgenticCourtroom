import sys
import os
import streamlit as st
from datetime import datetime
import pytz
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from dotenv import load_dotenv
from together import Together
from version.v2.prompts import critic_prompt, defender_prompt, arbiter_prompt
from version.v2.config import TOGETHER_MODELS
from utils.rag_context import build_context
from version.v2.agents.agent1 import run_defender
from version.v2.agents.agent2 import run_prosecutor
from version.v2.agents.agent3 import run_judge

# Load API Key
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

# Streamlit UI
st.title("⚖️ Agentic Courtroom - v2 Real-Time Simulation")

# Court timings
court_start_hour = 10
court_end_hour = 17

# Get current IST time
india_timezone = pytz.timezone("Asia/Kolkata")
current_time = datetime.now(india_timezone)
current_hour = current_time.hour

if court_start_hour <= current_hour < court_end_hour:
    st.success(f"🕙 Court is in session: {current_time.strftime('%H:%M %p')} IST")
    
    if st.button("Proceed with Courtroom Proceedings"):
        with st.spinner("📚 Building context from legal documents..."):
            context = build_context("data/constitution.pdf", "data/case_reports")

        with st.spinner("👨‍⚖️ Prosecutor presenting argument..."):
            prosecution = run_prosecutor(context, client)
            st.subheader("🔴 Prosecutor's Argument")
            st.write(prosecution)
            time.sleep(2)

        with st.spinner("🧑‍⚖️ Defense lawyer responding..."):
            defense = run_defender(context, client)
            st.subheader("🟢 Defense Lawyer's Argument")
            st.write(defense)
            time.sleep(2)

        with st.spinner("⚖️ Judge deliberating..."):
            verdict = run_judge(defense, prosecution, context, client)
            st.subheader("📜 Final Verdict by Judge")
            st.write(verdict)
else:
    st.error(f"⛔ Court is not in session now ({current_time.strftime('%H:%M %p')} IST)")
    st.info("Court sessions are held between 10:00 AM and 5:00 PM IST. Please come back during court hours.")

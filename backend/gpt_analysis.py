import google.generativeai as genai
import streamlit as st

# Load Gemini API key securely
api_key = st.secrets["gemini"]["api_key"]
genai.configure(api_key=api_key)

# Use a valid Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def analyze_threat(cve_desc: str) -> str:
    """
    Analyze and summarize a CVE vulnerability.
    """
    prompt = f"Summarize this cybersecurity vulnerability and assess the risk:\n\n{cve_desc}"
    response = model.generate_content(prompt)
    return response.text.strip()

def analyze_passive_scan(scan_output: str) -> str:
    """
    Analyze passive scan output and summarize security concerns.
    """
    prompt = (
        "Review the following passive scan data for a website. "
        "Identify any visible security misconfigurations or missing protections:\n\n"
        f"{scan_output}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

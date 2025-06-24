import streamlit as st
from agents.run_crew import run_crew_pipeline
from passive_scanner import run_passive_scan        # 🆕 Scanning
from gpt_analysis import analyze_passive_scan      # 🆕 AI analysis for passive scan
import os
import logging

os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"
os.environ["STREAMLIT_SERVER_PORT"] = os.environ.get("PORT", "8501")

st.set_option("client.showErrorDetails", False)
st.set_option("global.deprecation.showPyplotGlobalUse", False)


# Set up the Streamlit app
st.set_page_config(page_title="Cybersecurity Threat Intelligence Bot")
st.title("🛡️ Cyber Threat Intelligence Bot")

st.write("👋 Welcome! This bot can analyze CVEs by keyword or passively scan a website.")

# Select feature mode
mode = st.radio("Choose Mode:", ["Keyword-based CVE Analysis", "Passive URL Scan"])

# ✅ Mode 1: Keyword-based CVE analysis
if mode == "Keyword-based CVE Analysis":
    keyword = st.text_input("Enter a keyword (e.g., apache, chrome, linux)", value="apache")
    limit = st.slider("Number of CVEs to analyze", min_value=1, max_value=10, value=5)

    if st.button("🛰️ Run Threat Intelligence"):
        st.info("Running agents with the latest CVE data...")
        result = run_crew_pipeline(limit=limit, keyword=keyword)
        st.success("✅ Threat report generated successfully!")
        st.text_area("🔍 Threat Summary", result, height=400)

# ✅ Mode 2: Passive website scan with AI analysis
elif mode == "Passive URL Scan":
    url = st.text_input("🔗 Enter a website URL to scan (e.g., https://example.com)")

    if st.button("🔍 Run Passive Scan"):
        if url:
            st.info(f"Scanning {url} for passive security insights...")

            scan_result = run_passive_scan(url)  # Raw headers and SSL data
            st.text_area("📋 Raw Scan Output", scan_result, height=300)

            ai_summary = analyze_passive_scan(scan_result)  # Gemini AI analysis
            st.text_area("🧠 Gemini Summary", ai_summary, height=300)

            st.success("✅ Passive scan + AI analysis complete!")
        else:
            st.warning("⚠️ Please enter a valid URL.")
            

logging.basicConfig(level=logging.WARNING)  # Instead of DEBUG or INFO



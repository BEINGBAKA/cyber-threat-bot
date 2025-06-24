import google.generativeai as genai
import os
import logging
# Load Gemini API key from environment variable
api_key = os.getenv("api_key")

# Fail-safe check
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY environment variable not found!")

genai.configure(api_key=api_key)

# Use a valid Gemini model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def analyze_threat(cve_desc: str) -> str:
    """
    Analyze and summarize a CVE vulnerability.
    """
    try:
        prompt = f"Summarize this cybersecurity vulnerability and assess the risk:\n\n{cve_desc}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error analyzing threat: {str(e)}"

def analyze_passive_scan(scan_output: str) -> str:
    """
    Analyze passive scan output and summarize security concerns.
    """
    try:
        prompt = (
            "Review the following passive scan data for a website. "
            "Identify any visible security misconfigurations or missing protections:\n\n"
            f"{scan_output}"
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error analyzing passive scan: {str(e)}"

logging.basicConfig(level=logging.WARNING)  # Instead of DEBUG or INFO


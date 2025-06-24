from crewai import Agent, Task, Crew
from scraping.cve_scrapper import fetch_latest_cves
from gpt_analysis import analyze_threat
from vector_db.chroma_store import add_to_vectordb
from gpt_analysis import analyze_passive_scan


# === AGENT DEFINITIONS ===

crawler = Agent(
    role="CVE Crawler",
    goal="Fetch and store latest CVEs in vector DB",
    backstory="Knows how to find vulnerabilities online.",
    verbose=True
)

analyzer = Agent(
    role="Threat Analyst",
    goal="Assess and classify threat severity using Cohere",
    backstory="Understands cybersecurity deeply.",
    verbose=True
)

reporter = Agent(
    role="Reporter",
    goal="Summarize threats for display in the dashboard",
    backstory="Converts findings into human-readable summaries.",
    verbose=True
)

# Optional: Agent and task for passive scanning
passive_reporter = Agent(
    role="Website Scanner",
    goal="Analyze website headers and SSL info",
    backstory="Can interpret passive web scan results for security flaws.",
    verbose=True
)
# === TASK FUNCTIONS ===

def crawling_task(cves):
    for cve in cves:
        add_to_vectordb(cve["id"], cve["desc"])
    return "✅ CVEs stored in vector DB."

def analysis_task(cves):
    analyzed = []
    for cve in cves:
        summary = analyze_threat(cve["desc"])
        analyzed.append((cve["id"], summary))
    return analyzed

def reporting_task(analyzed):
    return "\n\n".join([f"🛡️ {cid}\n{summary}" for cid, summary in analyzed])

# === Optional: Combined function to be called from Streamlit ===

def full_pipeline(limit=5, keyword="apache"):
    cves = fetch_latest_cves(limit=limit, keyword=keyword)
    crawling_task(cves)
    analyzed = analysis_task(cves)
    final_report = reporting_task(analyzed)
    return final_report


def passive_analysis_task(raw_scan_data):
    return analyze_passive_scan(raw_scan_data)

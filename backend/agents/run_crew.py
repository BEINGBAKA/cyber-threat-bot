from agents.crew_agents import fetch_latest_cves, crawling_task, analysis_task, reporting_task
import logging
from vector_db.chroma_store import add_to_vectordb, clear_vectordb

def run_crew_pipeline(limit=1, keyword="apache"):
    # Step 1: Fetch CVEs
    cves = fetch_latest_cves(limit=1, keyword=keyword)

    # ✅ Step 2: Clear vector DB ONCE
    clear_vectordb()

    # Step 3: Store in vector DB
    crawling_task(cves)

    # Step 4: Analyze
    results = analysis_task(cves)

    # Step 5: Report
    return reporting_task(results)


logging.basicConfig(level=logging.WARNING)  # Instead of DEBUG or INFO


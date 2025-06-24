from agents.crew_agents import fetch_latest_cves, crawling_task, analysis_task, reporting_task
import logging



def run_crew_pipeline(limit=3, keyword="apache"):
    # Step 1: Fetch once and pass data forward
    cves = fetch_latest_cves(limit=3, keyword=keyword)

    # Step 2: Store in vector DB
    crawling_task(cves)

    # Step 3: Analyze each CVE
    results = analysis_task(cves)

    # Step 4: Generate report
    return reporting_task(results)

logging.basicConfig(level=logging.WARNING)  # Instead of DEBUG or INFO


from agents.crew_agents import fetch_latest_cves, crawling_task, analysis_task, reporting_task

def run_crew_pipeline(limit=5, keyword="apache"):
    # Step 1: Fetch once and pass data forward
    cves = fetch_latest_cves(limit=limit, keyword=keyword)

    # Step 2: Store in vector DB
    crawling_task(cves)

    # Step 3: Analyze each CVE
    results = analysis_task(cves)

    # Step 4: Generate report
    return reporting_task(results)

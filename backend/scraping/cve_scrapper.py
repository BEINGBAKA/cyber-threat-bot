import requests

def fetch_latest_cves(limit=5, keyword="apache"):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "resultsPerPage": limit,
        "keywordSearch": keyword
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Error fetching CVEs: {e}")
        return []

    cves = []
    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})
        descriptions = cve.get("descriptions", [])
        
        # Get the first English description
        description = next((d["value"] for d in descriptions if d["lang"] == "en"), "No description available.")
        
        cves.append({
            "id": cve.get("id", "N/A"),
            "desc": description
        })

    return cves

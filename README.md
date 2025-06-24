# cyber-threat-bot
A Streamlit-based cybersecurity threat intelligence bot that fetches, analyzes, and summarizes CVEs using Gemini and vector embeddings.

#Cyber Threat Intelligence Bot

A powerful, AI-driven cybersecurity assistant that scans the latest vulnerabilities, analyzes them using large language models, and presents concise threat intelligence reports. Built using **Streamlit**, **Cohere**, and **LangChain**, this tool helps security analysts and researchers stay informed about current threats.

 #Features:

- Fetches CVEs: using keyword-based search from the National Vulnerability Database (NVD)
- Analyzes threats: using Cohere's LLM to generate human-readable summaries and risk insights
- Stores CVEs in a vector database:for similarity search using embeddings
- Passive scanning of website URLs:for exposed tech stack, headers, and SSL data
- Simple and clean Streamlit UI- no frontend coding required!

#How It Works:

1. You input a keyword (e.g. `apache`, `wordpress`, `openssl`)
2. The bot queries the NVD API for matching vulnerabilities (CVEs)
3. Each CVE description is passed to a Gemini LLM for summarization and risk assessment
4. Data is stored in a Chroma vector database for future retrieval and semantic search
5. The final summary is displayed in an easy-to-read format

---

## 📦 Tech Stack

| Layer | Technology |
|-------|------------|
| UI    | Streamlit |
| LLM   | GEMINI API (Generative AI) |
| Embeddings | gemini Embeddings + Chroma DB |
| Scraping/API | NVD REST API |
| Backend | Python (LangChain, requests, BeautifulSoup) |

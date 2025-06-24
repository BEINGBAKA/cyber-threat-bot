import requests
import ssl
import socket
import http.client
from urllib.parse import urlparse


def check_ssl_certificate(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return f"✅ SSL certificate is valid. Issued to: {cert['subject'][0][0][1]}"
    except Exception as e:
        return f"❌ SSL certificate check failed: {str(e)}"


def get_http_headers(url):
    try:
        response = requests.head(url, timeout=5)
        headers = "\n".join([f"{k}: {v}" for k, v in response.headers.items()])
        return f"✅ Retrieved HTTP headers:\n{headers}"
    except Exception as e:
        return f"❌ Failed to retrieve HTTP headers: {str(e)}"


def check_server_tech_stack(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        server = headers.get("Server", "Unknown")
        powered_by = headers.get("X-Powered-By", "Unknown")
        return f"✅ Server: {server}, Powered by: {powered_by}"
    except Exception as e:
        return f"❌ Error detecting tech stack: {str(e)}"


def run_passive_scan(site_url):
    try:
        parsed_url = urlparse(site_url)
        hostname = parsed_url.hostname or site_url.replace("https://", "").replace("http://", "").split("/")[0]

        ssl_report = check_ssl_certificate(hostname)
        headers_report = get_http_headers(site_url)
        tech_stack_report = check_server_tech_stack(site_url)

        return f"{ssl_report}\n\n{headers_report}\n\n{tech_stack_report}"

    except Exception as e:
        return f"❌ Error during scan: {str(e)}"

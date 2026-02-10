import requests
import xml.etree.ElementTree as ET
import time

BASE_URL = "https://export.arxiv.org/oai2"

def harvest_arxiv_metadata():
    params = {
        "verb": "ListRecords",
        "metadataPrefix": "arXiv"
    }

    while True:
        r = requests.get(BASE_URL, params=params, timeout=60)
        r.raise_for_status()

        root = ET.fromstring(r.text)

        yield r.text  # raw XML chunk (recommended to save)

        token = root.find(".//{http://www.openarchives.org/OAI/2.0/}resumptionToken")
        if token is None or not token.text:
            break

        params = {
            "verb": "ListRecords",
            "resumptionToken": token.text
        }

        time.sleep(1)  # be polite to arXiv servers

with open("arxiv_metadata.xml", "w", encoding="utf-8") as f:
    for chunk in harvest_arxiv_metadata():
        f.write(chunk)
        f.write("\n")
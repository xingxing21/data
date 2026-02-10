import requests

SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/{}"

def arxiv_to_semantic_scholar(arxiv_id):
    """
    Convert an arXiv ID to Semantic Scholar paper metadata.
    Returns JSON response or None if not found.
    """
    paper_id = f"arXiv:{arxiv_id}"
    url = SEMANTIC_SCHOLAR_API.format(paper_id)

    params = {
        "fields": "title,authors,year,abstract,citationCount,referenceCount,externalIds,url"
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


if __name__ == "__main__":
    arxiv_id = "2204.13640"  # example
    paper = arxiv_to_semantic_scholar(arxiv_id)

    if paper:
        print("Title:", paper["title"])
        print("Year:", paper["year"])
        print("Citations:", paper["citationCount"])
        print("Semantic Scholar URL:", paper["url"])
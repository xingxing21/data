Here’s a clean, working Python example that **takes an arXiv ID and fetches the corresponding paper from Semantic Scholar** using their public API.

Semantic Scholar already understands arXiv IDs, so the “conversion” is really just querying with the right identifier format.

---

## 1️⃣ Basic idea

Semantic Scholar API accepts:

```
arXiv:<arxiv_id>
```

Example:

```
arXiv:2301.01234
```

---

## 2️⃣ Python code (simple & practical)

```python
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
    arxiv_id = "2301.01234"  # example
    paper = arxiv_to_semantic_scholar(arxiv_id)

    if paper:
        print("Title:", paper["title"])
        print("Year:", paper["year"])
        print("Citations:", paper["citationCount"])
        print("Semantic Scholar URL:", paper["url"])
```

---

## 3️⃣ Example output fields you get

* `paperId` (Semantic Scholar internal ID)
* `title`
* `authors`
* `abstract`
* `citationCount`
* `externalIds`

  ```json
  {
    "ArXiv": "2301.01234",
    "DOI": "10.xxxx/xxxx"
  }
  ```
* `url` (Semantic Scholar page)

---

## 4️⃣ If you want *only* the Semantic Scholar URL

```python
def arxiv_to_semantic_scholar_url(arxiv_id):
    return f"https://www.semanticscholar.org/paper/arXiv:{arxiv_id}"

print(arxiv_to_semantic_scholar_url("2301.01234"))
```

---

## 5️⃣ Notes (important ⚠️)

* No API key required for light usage
* Rate limits exist (≈100 requests / 5 min unauthenticated)
* Works for **both old-style and new-style arXiv IDs**

  * `hep-th/9901001`
  * `2301.01234`

---

If you want, I can:

* Batch-convert a **list of arXiv IDs**
* Store results in **JSON / CSV**
* Add **retry & rate-limit handling**
* Cross-check arXiv → DOI → Semantic Scholar

Just tell me how you’re using this 👀

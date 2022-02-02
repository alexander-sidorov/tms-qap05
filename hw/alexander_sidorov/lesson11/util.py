import httpx


def get_localhost() -> str:
    url = "http://localhost:8000"
    resp = httpx.get(url)
    return resp.text

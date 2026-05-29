"""GitHub Trending: scraping di github.com/trending (HTML), filtrato su 'today'."""
import requests
from bs4 import BeautifulSoup
from _common import DEFAULT_HEADERS, TIMEOUT, normalize, run_and_save

PLATFORM = "github_trending"
URL = "https://github.com/trending?since=daily"


def fetch_trends() -> list[dict]:
    r = requests.get(URL, headers=DEFAULT_HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    out = []
    for art in soup.select("article.Box-row")[:10]:
        a = art.select_one("h2 a")
        if not a:
            continue
        repo = a.get("href", "").strip("/")
        desc_tag = art.select_one("p")
        desc = desc_tag.get_text(strip=True) if desc_tag else ""
        stars_tag = art.select_one("a.Link--muted")
        stars = stars_tag.get_text(strip=True) if stars_tag else ""
        out.append(normalize(
            title=repo,
            url=f"https://github.com/{repo}",
            source=PLATFORM,
            score=stars,
            snippet=desc,
        ))
    return out


if __name__ == "__main__":
    run_and_save(PLATFORM, fetch_trends)

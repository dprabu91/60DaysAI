from flask import Flask, jsonify
from playwright.sync_api import sync_playwright, TimeoutError

app = Flask(__name__)

def fetch_latest_ind_nz_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless for Flask
        context = browser.new_context(
            locale="en-IN",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        page = context.new_page()

        url = "https://news.google.com/search?q=India%20vs%20New%20Zealand"
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        try:
            page.get_by_role("link", name="India", exact=False).first.wait_for(timeout=60000)
        except TimeoutError:
            browser.close()
            return {
                "status": "error",
                "message": "Headlines did not load or layout changed"
            }

        links = page.get_by_role("link").filter(has_text="India")

        if links.count() == 0:
            browser.close()
            return {
                "status": "error",
                "message": "No relevant headlines found"
            }

        first = links.nth(0)

        headline = first.inner_text()
        href = first.get_attribute("href")

        if href and href.startswith("./"):
            href = "https://news.google.com" + href[1:]

        browser.close()

        return {
            "status": "success",
            "headline": headline,
            "link": href
        }


@app.route("/latest-news", methods=["GET"])
def latest_news():
    data = fetch_latest_ind_nz_news()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

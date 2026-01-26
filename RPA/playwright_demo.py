from playwright.sync_api import sync_playwright, TimeoutError

def fetch_latest_ind_nz_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            locale="en-IN",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        page = context.new_page()

        url = "https://news.google.com/search?q=India%20vs%20New%20Zealand"
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        try:
            # Wait for any headline-like link
            page.get_by_role("link", name="India", exact=False).first.wait_for(timeout=60000)
        except TimeoutError:
            print("❌ Headlines did not load. Google News layout changed.")
            browser.close()
            return

        # Collect visible headline links
        links = page.get_by_role("link").filter(has_text="India")

        count = links.count()
        if count == 0:
            print("❌ No relevant headlines found")
            browser.close()
            return

        first = links.nth(0)

        headline = first.inner_text()
        href = first.get_attribute("href")

        if href and href.startswith("./"):
            href = "https://news.google.com" + href[1:]

        print("\n📰 LATEST IND vs NZ NEWS")
        print("-" * 45)
        print("Headline :", headline)
        print("Link     :", href)

        browser.close()

if __name__ == "__main__":
    fetch_latest_ind_nz_news()

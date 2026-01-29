from playwright.async_api import async_playwright
import asyncio

async def playwirght_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) #launch browser
        pages = await browser.new_page()
        await pages.goto("https://www.google.com") #navigate
        await pages.wait_for_timeout(5000) #wait for 5 seconds
        await browser.close() #close browser

if __name__ == "__main__":
    asyncio.run(playwirght_function())
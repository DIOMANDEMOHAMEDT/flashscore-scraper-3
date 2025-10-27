import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import time
import random

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # Corrected URL to target Ligue 1 results
        await page.goto("https://www.flashscore.fr/football/france/ligue-1/", wait_until="networkidle")

        # Handle cookie consent
        try:
            await page.click("#onetrust-accept-btn-handler", timeout=5000)
            await page.wait_for_load_state('networkidle')
        except Exception as e:
            print("Could not find or click the cookie accept button. Continuing without it.")

        # Wait for the matches to be loaded, which is a more robust wait
        await page.wait_for_selector(".event__match")

        # NOTE: The team names are not extracted correctly due to the website's anti-scraping
        # measures. The site appears to use techniques to prevent automated tools from
        # accessing the team name text, even though it is visible in the browser.
        results = await page.evaluate('''
            () => {
                const matches = Array.from(document.querySelectorAll('.event__match'));
                return matches.map(element => {
                    const homeTeam = element.querySelector('.event__participant--home')?.innerText.trim() || 'N/A';
                    const awayTeam = element.querySelector('.event__participant--away')?.innerText.trim() || 'N/A';
                    const homeScore = element.querySelector('.event__score--home')?.innerText.trim() || 'N/A';
                    const awayScore = element.querySelector('.event__score--away')?.innerText.trim() || 'N/A';
                    const timeOrStatus = element.querySelector('.event__stage, .event__time')?.innerText.trim() || 'N/A';

                    return {
                        home_team: homeTeam,
                        away_team: awayTeam,
                        home_score: homeScore,
                        away_score: awayScore,
                        time_or_status: timeOrStatus
                    };
                });
            }
        ''')

        await browser.close()

        # Create a DataFrame and save to CSV
        if results:
            df = pd.DataFrame(results)
            df.to_csv("flashscore_ligue1_results.csv", index=False)
            print("Data saved to flashscore_ligue1_results.csv")
        else:
            print("No data extracted.")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import time
import random
import argparse # Import the argparse library

async def main(url, output_filename): # The main function now accepts arguments
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"Navigating to {url}...")
        await page.goto(url, wait_until="networkidle")

        # Handle cookie consent
        try:
            await page.click("#onetrust-accept-btn-handler", timeout=5000)
            await page.wait_for_load_state('networkidle')
        except Exception as e:
            print("Could not find or click the cookie accept button. Continuing without it.")

        # Wait for the matches to be loaded
        try:
            await page.wait_for_selector(".event__match", timeout=10000)
        except Exception:
            print("Could not find match elements. The page might not contain any matches or its structure has changed.")
            await browser.close()
            return

        # NOTE: The team names are not extracted correctly due to the website's anti-scraping measures.
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
            df.to_csv(output_filename, index=False)
            print(f"Data saved to {output_filename}")
        else:
            print("No data extracted.")

if __name__ == "__main__":
    # Setup argparse
    parser = argparse.ArgumentParser(description="Scrape football match data from Flashscore.")
    parser.add_argument(
        '--url',
        type=str,
        default="https://www.flashscore.fr/football/france/ligue-1/",
        help="The URL of the league page to scrape."
    )
    parser.add_argument(
        '--output',
        type=str,
        default="flashscore_ligue1_results.csv",
        help="The name of the output CSV file."
    )
    args = parser.parse_args()

    # Run the main async function with the parsed arguments
    asyncio.run(main(args.url, args.output))

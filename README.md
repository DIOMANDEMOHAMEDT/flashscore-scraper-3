# Flashscore Scraper for Ligue 1

This project is a web scraper designed to extract football match data from flashscore.fr. It uses Python with the Playwright and Pandas libraries.

## Description

The script navigates to a specified league's page on flashscore.fr, handles the cookie consent banner, and scrapes the details of the matches listed. The extracted data includes:

-   Home Team
-   Away Team
-   Home Score
-   Away Score
-   Time or Status of the match

The data is then saved into a CSV file.

**Note:** Due to the website's anti-scraping measures, the script is currently unable to extract the team names, which will appear as "N/A" in the output file.

## Prerequisites

-   Python 3.x

## Installation

1.  Clone the repository.

2.  Install the required Python libraries:
    ```bash
    pip install playwright pandas
    ```

3.  Install the necessary browser binaries for Playwright:
    ```bash
    playwright install
    ```
    You may also need to install system dependencies:
    ```bash
    playwright install-deps
    ```

## How to Run the Script

### Basic Usage

To run the scraper with the default settings (French Ligue 1), execute the following command:

```bash
python flashscore_scraper.py
```
This will create a file named `flashscore_ligue1_results.csv`.

### Advanced Usage (Command-Line Arguments)

You can customize the scraper's behavior using the following command-line arguments:

-   `--url`: Specify the URL of the league you want to scrape.
-   `--output`: Specify the name of the output CSV file.

**Example:** To scrape the English Premier League and save the results to `premier_league.csv`:
```bash
python flashscore_scraper.py --url "https://www.flashscore.fr/football/angleterre/premier-league/" --output "premier_league.csv"
```

## Expected Result

After the script finishes, it will create a CSV file with the name you specified (or the default name). The file will contain the scraped match data with the following columns: `home_team`, `away_team`, `home_score`, `away_score`, and `time_or_status`.

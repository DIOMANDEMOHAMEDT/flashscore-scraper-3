# Flashscore Scraper for Ligue 1

This project is a web scraper designed to extract football match data from the Ligue 1 page on flashscore.fr. It uses Python with the Playwright and Pandas libraries.

## Description

The script navigates to the French Ligue 1 football page on flashscore.fr, handles the cookie consent banner, and scrapes the details of the matches listed on the page. The extracted data includes:

-   Home Team
-   Away Team
-   Home Score
-   Away Score
-   Time or Status of the match

The data is then saved into a CSV file named `flashscore_ligue1_results.csv`.

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

To run the scraper, execute the following command in your terminal:

```bash
python flashscore_scraper.py
```

## Expected Result

After the script finishes running, it will create a file named `flashscore_ligue1_results.csv` in the same directory. The file will contain the scraped match data with the following columns: `home_team`, `away_team`, `home_score`, `away_score`, and `time_or_status`.

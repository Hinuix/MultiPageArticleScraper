# MultiPageArticleScraper

MultiPageArticleScraper is a Python script designed to scrape article titles from multiple pages of a website. It utilizes pagination to navigate through various pages and extracts article titles, which are then stored in a structured format like CSV. The script also includes error handling mechanisms to ensure smooth execution even in the presence of potential issues during the scraping process.

## Prerequisites

- Python 3.x
- `requests` library
- `BeautifulSoup` library

## Installation

1. Clone or download the repository to your local machine.
2. Install Python 3.x if you haven't already.
3. Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Modify the `base_url` variable in the script to match the website you want to scrape.
2. Adjust the `num_pages` variable to specify the number of pages you want to scrape.
3. Run the script using Python:
    ```bash
    python MultiPageArticleScraper.py
    ```
4. The scraped data will be saved 

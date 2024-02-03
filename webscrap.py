import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape the webpage and extract article titles
def scrape_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_titles = soup.find_all('h2', class_='article-title')
            return [title.text.strip() for title in article_titles]
        else:
            print(f'Failed to retrieve page: {url}')
            return []
    except Exception as e:
        print(f'Error occurred while scraping page {url}: {e}')
        return []

# Main function to scrape multiple pages and store the data
def main():
    base_url = 'https://example.com/page/'

    # Number of pages to scrape
    num_pages = 3
    all_titles = []

    for page_num in range(1, num_pages + 1):
        page_url = f'{base_url}{page_num}'
        print(f'Scraping page {page_num}...')
        titles = scrape_page(page_url)
        all_titles.extend(titles)

    # Store the scraped data in a CSV file
    csv_file = 'scraped_data.csv'
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Article Title'])
            for title in all_titles:
                writer.writerow([title])
        print(f'Scraped data saved to {csv_file}')
    except Exception as e:
        print(f'Error occurred while writing to CSV file: {e}')

if __name__ == "__main__":
    main()

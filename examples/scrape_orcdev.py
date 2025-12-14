from twitter_scraper.scraper import TwitterScraper
from twitter_scraper.utils import save_to_csv

scraper = TwitterScraper(headless=True)

tweets = scraper.scrape_user(
    username="orcdev",
    limit=10
)

save_to_csv(tweets, "orcdev.csv")

print(f"Scraped {len(tweets)} tweets")

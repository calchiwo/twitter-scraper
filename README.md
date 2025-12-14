# twitter-scraper

I built this because I wanted to understand how scraping actually works in the real world, not just theory.

This is a simple Python Twitter (X) scraper built with Playwright. It scrapes public tweets only from any username you pass in. No hardcoding. No magic.

You run it. It opens a real browser. It scrolls. It pulls tweets. That’s it.

## Why I built this

I wanted to learn a few things properly instead of just watching videos about them.

- How browser based scraping actually works  
- How to deal with dynamic pages like X  
- How to structure a Python project properly  
- How to avoid hardcoding and build something reusable  

This is not a startup product.  
It’s a learning project that actually works.

## What it can do

- Scrape public tweets from any username  
- Load tweets by scrolling  
- Extract clean tweet text  
- Extract timestamps  
- Save results to CSV  
- Run fully from the terminal  

## What it does not do

- No login  
- No private accounts  
- No API keys  
- No guarantee X won’t change things later  

This is scraping. Stuff breaks sometimes. That’s part of it.

## Tech used

- Python  
- Playwright  
- Pandas  

Nothing fancy. Just tools that get the job done.

## Setup

Clone the repo.

```bash
git clone https://github.com/calchiwo/twitter-scraper.git
cd twitter-scraper




# twitter-scraper

An open source Python tool for scraping public X (Twitter) profiles using Playwright.

## Features
- Scrape public tweets
- JavaScript rendered content
- Simple Python API
- CSV export

## Usage

```python
from twitter_scraper.scraper import TwitterScraper

import os
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time

SEASONS = list(range(2016, 2023))
DATA_DIR = "data"
ROSTER_DIR = os.path.join(DATA_DIR, "rosters")

def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(url)
                print(page.title())
                html = page.inner_html(selector)
        except PlaywrightTimeout:
            print(f"Timeout error on {url}")
            continue
        except Exception as e:
            print(f"An error occurred on {url}: {e}")
            continue
        else:
            break
    return html

def scrape_season(season):
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_per_game.html"
    save_path = os.path.join(ROSTER_DIR, url.split("/")[-1]) 
    html = get_html(url, "#all_per_game_stats")
    with open(save_path, "w+", encoding="utf-8") as f:
        f.write(html)

for season in SEASONS:
    scrape_season(season)


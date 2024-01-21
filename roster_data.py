import os
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

ROSTER_DIR = "data/rosters"

rosters = os.listdir(ROSTER_DIR)
rosters = [os.path.join(ROSTER_DIR, f) for f in rosters if f.endswith(".html")]

def parse_html(rosters):
    with open(rosters, encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, features="lxml")
    [s.decompose() for s in soup.select("tr.over_header")]
    [s.decompose() for s in soup.select("tr.thead")]
    [s.decompose() for s in soup.select("tfoot")]
    return soup


def read_stats(soup):
    html_content = str(soup)
    df = pd.read_html(StringIO(html_content), attrs={'id': 'per_game_stats'}, index_col=0)[0]
    return df

roster = pd.DataFrame()

season = 2016
for year in rosters:
    soup = parse_html(year)
    roster_year = read_stats(soup)
    roster_year = roster_year.iloc[:,[0,1,3]]
    roster_year['Season'] = season
    season = season + 1
    roster = pd.concat([roster, roster_year], axis=0, ignore_index=True)

roster = roster.drop_duplicates()
roster = pd.concat([roster], axis=0, ignore_index=True)

roster.to_csv("roster_data.csv")
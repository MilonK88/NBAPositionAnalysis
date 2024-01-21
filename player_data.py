import os
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from datetime import datetime

SCORE_DIR = "data/scores"

box_scores = os.listdir(SCORE_DIR)
box_scores = [os.path.join(SCORE_DIR, f) for f in box_scores if f.endswith(".html")]

def parse_html(box_score):
    with open(box_score, encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, features="lxml")
    [s.decompose() for s in soup.select("tr.over_header")]
    [s.decompose() for s in soup.select("tr.thead")]
    [s.decompose() for s in soup.select("tfoot")]
    return soup

def read_season_info(soup):
    nav = soup.select("#bottom_nav_container")[0]
    hrefs = [a["href"] for a in nav.find_all('a')]
    season = os.path.basename(hrefs[1]).split("_")[0]
    return season

def read_line_score(soup):
    html_content = str(soup)
    line_score = pd.read_html(StringIO(html_content), attrs={'id': 'line_score'})[0]
    cols = list(line_score.columns)
    cols[0] = "team"
    cols[-1] = "total"
    line_score.columns = cols
    line_score = line_score[["team", "total"]]
    return line_score

def mp_convert(mp):
    time = sum(x * int(t) for x, t in zip([60, 1], mp.split(":")))
    return time

def read_stats(soup, team, stat):
    html_content = str(soup)
    df = pd.read_html(StringIO(html_content), attrs={'id': f'box-{team}-game-{stat}'}, index_col=0)[0]
    mp_store = df.iloc[:,0].copy()
    for mp in range(len(mp_store)):
        if mp_store.iloc[mp]=='Did Not Play':
            mp_store.iloc[mp] = 0
        elif mp_store.iloc[mp]=='Did Not Dress':
            mp_store.iloc[mp] = 0
        elif mp_store.iloc[mp]=='Player Suspended':
            mp_store.iloc[mp] = 0
        elif mp_store.iloc[mp]=='Not With Team':
            mp_store.iloc[mp] = 0
        else:
            mp_store.iat[mp] = mp_convert(mp_store.iat[mp])
        df.iloc[:, 0] = mp_store
    df = df.apply(pd.to_numeric, errors="coerce")
    df.rename(columns={"MP": "SP"}, inplace=True)
    return df

games = pd.DataFrame()
i=0
for box_score in box_scores:
    i=i+1
    soup = parse_html(box_score)
    line_score = read_line_score(soup)
    teams = list(line_score["team"])
    for team in teams:
        basic = read_stats(soup, team, "basic")
        advanced = read_stats(soup, team, "advanced")
        name_list = basic.index.values.tolist()
        name_df = pd.DataFrame(name_list, columns=['player'])
        stats = pd.concat([basic, advanced], axis=1)
        stats = pd.concat([stats], axis=0, ignore_index=True)
        stats["season"] = read_season_info(soup)
        stats["date"] = os.path.basename(box_score)[:8]
        stats["date"] = pd.to_datetime(stats["date"], format="%Y%m%d")
        stats['ID'] = (f"{read_season_info(soup)}_{os.path.basename(box_score)[:8]}_{team}")
        player_df = pd.concat([name_df, stats], axis=1)
        games = pd.concat([games, player_df], axis=0, ignore_index=True)

    if i % 100 == 0:
        print(f"{i} / {len(box_scores)}")

games.to_csv("player_data.csv")

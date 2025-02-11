import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/87.0.4280.88 Safari/537.36"
    )
}

def extract_team_name(team_div):
    link = team_div.find("a", class_="odds-link")
    if link:
        first_span = link.find("span")
        if first_span:
            return first_span.get_text(strip=True)
    return team_div.get_text(strip=True)

def scrape_oddsshark_nba_odds(url="https://www.oddsshark.com/nba/odds"):
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        print("Failed to retrieve NBA page:", response.status_code)
        return []
    soup = BeautifulSoup(response.content, "html.parser")
    games = []
    event_containers = soup.find_all("div", class_="odds--group__event-container")
    for event in event_containers:
        participants = event.find("div", class_="odds--group__event-participants")
        if not participants:
            continue
        team_divs = participants.find_all("div", class_="participant-name")
        if len(team_divs) < 2:
            continue
        home_team = extract_team_name(team_divs[0])
        away_team = extract_team_name(team_divs[1])
        event_date = event.get("data-event-date")
        if event_date:
            try:
                commence_time = datetime.utcfromtimestamp(int(event_date)).isoformat() + "Z"
            except Exception:
                commence_time = None
        else:
            time_div = event.find("div", class_="odds--group__event-time")
            commence_time = time_div.get_text(strip=True) if time_div else None
        odds_block = event.find("div", class_=lambda c: c and "odds--group__event-book" in c and "opening" in c)
        home_moneyline = None
        away_moneyline = None
        if odds_block:
            moneyline_divs = odds_block.find_all("div", attrs={"data-odds-moneyline": True})
            if len(moneyline_divs) >= 2:
                home_moneyline = moneyline_divs[0].get_text(strip=True)
                away_moneyline = moneyline_divs[1].get_text(strip=True)
        bookmakers = []
        if home_moneyline and away_moneyline:
            bookmakers = [{
                "key": "oddsshark",
                "markets": [{
                    "key": "h2h",
                    "outcomes": [
                        {"name": home_team, "price": home_moneyline},
                        {"name": away_team, "price": away_moneyline}
                    ]
                }]
            }]
        game_obj = {
            "home_team": home_team,
            "away_team": away_team,
            "commence_time": commence_time,
            "scores": None,
            "bookmakers": bookmakers
        }
        games.append(game_obj)
    return games

def scrape_oddsshark_ufc_odds(url="https://www.oddsshark.com/ufc/odds"):
    response = requests.get(url, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        print("Failed to retrieve UFC page:", response.status_code)
        return []
    soup = BeautifulSoup(response.content, "html.parser")
    games = []
    event_containers = soup.find_all("div", class_="odds--group__event-container")
    for event in event_containers:
        participants = event.find("div", class_="odds--group__event-participants")
        if not participants:
            continue
        fighter_divs = participants.find_all("div", class_="participant-name")
        if len(fighter_divs) < 2:
            continue
        fighter1 = extract_team_name(fighter_divs[0])
        fighter2 = extract_team_name(fighter_divs[1])
        home_team = fighter1
        away_team = fighter2
        event_date = event.get("data-event-date")
        if event_date:
            try:
                commence_time = datetime.utcfromtimestamp(int(event_date)).isoformat() + "Z"
            except Exception:
                commence_time = None
        else:
            time_div = event.find("div", class_="odds--group__event-time")
            commence_time = time_div.get_text(strip=True) if time_div else None
        odds_block = event.find("div", class_=lambda c: c and "odds--group__event-book" in c and "opening" in c)
        home_moneyline = None
        away_moneyline = None
        if odds_block:
            moneyline_divs = odds_block.find_all("div", attrs={"data-odds-moneyline": True})
            if len(moneyline_divs) >= 2:
                home_moneyline = moneyline_divs[0].get_text(strip=True)
                away_moneyline = moneyline_divs[1].get_text(strip=True)
        bookmakers = []
        if home_moneyline and away_moneyline:
            bookmakers = [{
                "key": "oddsshark",
                "markets": [{
                    "key": "h2h",
                    "outcomes": [
                        {"name": home_team, "price": home_moneyline},
                        {"name": away_team, "price": away_moneyline}
                    ]
                }]
            }]
        game_obj = {
            "home_team": home_team,
            "away_team": away_team,
            "commence_time": commence_time,
            "scores": None,
            "bookmakers": bookmakers
        }
        games.append(game_obj)
    return games

if __name__ == "__main__":
    nba_games = scrape_oddsshark_nba_odds()
    print(json.dumps(nba_games, indent=2))
    ufc_games = scrape_oddsshark_ufc_odds()
    print(json.dumps(ufc_games, indent=2))

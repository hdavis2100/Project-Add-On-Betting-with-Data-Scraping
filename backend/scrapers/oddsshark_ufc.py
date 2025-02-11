import requests
from bs4 import BeautifulSoup
def scrape_oddsshark_ufc_odds():
    url = "https://www.oddsshark.com/ufc/odds"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    games = []
    events = soup.select("div.odds--group__event-container.fighting")
    for event in events:
        game = {}
        game["id"] = event.get("data-id")
        game["commence_time"] = event.get("data-event-date")
        participants = event.select("div.odds--group__event-participants div.participant-name")
        if participants and len(participants) >= 2:
            game["fighter1"] = participants[0].get_text(strip=True)
            game["fighter2"] = participants[1].get_text(strip=True)
        opening = event.select_one("div.odds--group__event-book.book-9974.opening")
        if opening:
            odds_elements = opening.select("div.odds-moneyline div[data-odds-moneyline]")
            if odds_elements and len(odds_elements) >= 2:
                game["fighter1_odds"] = odds_elements[0].get_text(strip=True)
                game["fighter2_odds"] = odds_elements[1].get_text(strip=True)
        games.append(game)
    return games

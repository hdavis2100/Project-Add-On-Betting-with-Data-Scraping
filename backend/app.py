from flask import Flask, jsonify
from flask_cors import CORS
import logging
from scrapers.oddsshark import scrape_oddsshark_nba_odds, scrape_oddsshark_ufc_odds

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    return "Backend is working!"

@app.route("/api/nba/odds")
def nba_odds():
    try:
        games = scrape_oddsshark_nba_odds()
        return jsonify(games)
    except Exception as e:
        logger.error("Error scraping Oddsshark NBA: %s", e)
        return jsonify({"error": "Failed to scrape NBA odds"}), 500

@app.route("/api/ufc/odds")
def ufc_odds():
    try:
        games = scrape_oddsshark_ufc_odds()
        return jsonify(games)
    except Exception as e:
        logger.error("Error scraping Oddsshark UFC: %s", e)
        return jsonify({"error": "Failed to scrape UFC odds"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)






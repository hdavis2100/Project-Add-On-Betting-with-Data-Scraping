from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import logging
import os
from flask import send_from_directory

from scrapers.oddsshark import scrape_oddsshark_nba_odds

app = Flask(__name__, static_folder="static", static_url_path="/")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if path != "" and os.path.exists(os.path.join(static_dir, path)):
        return send_from_directory(static_dir, path)
    return send_from_directory(static_dir, "index.html")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def index():
    return "Backend is working!"

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")
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
    app.run(debug=True)





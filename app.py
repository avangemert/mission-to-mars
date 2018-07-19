from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_scrape = mongo.db.mars_scrape.find_one()
    return render_template("index.html", mars_scrape=mars_scrape)


@app.route("/scrape")
def scraper():
    mars_scrape = mongo.db.mars_scrape
    mars_scrape_data = scrape_mars.scrape()
    mars_scrape.update(
        {},
        mars_scrape_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

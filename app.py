from flask import Flask
import json
import main

app = Flask(__name__)


@app.route("/")
def home():
    return json.dumps(main.Main().get_link_station_result())

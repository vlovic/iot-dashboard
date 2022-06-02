from flask import Flask, render_template, request, redirect, url_for
from db import get_db, close_connection
import json
import datetime


app = Flask(__name__)
app.config.from_mapping(
    DATABASE="sensor_data.sqlite",
)
app.teardown_appcontext(close_connection)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/airgradient:dc8c38/measures", methods=['POST'])
def update_graph():
    # TODO: add data to sqlite db
    data_dict = json.loads(request.data.decode("utf-8"))
    print(data_dict)
    db = get_db()
    db.execute(
        "INSERT INTO pm02 (time, pm02) VALUES (?, ?)",
        (datetime.datetime.now(), data_dict['pm02'])
    )
    db.commit()

    return ""


from flask import Flask, render_template, request, Response, stream_with_context
from db import get_db, close_connection
import json
import datetime
import time


app = Flask(__name__)
app.config.from_mapping(
    DATABASE="sensor_data.sqlite",
)
app.teardown_appcontext(close_connection)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/airgradient:dc8c38/measures", methods=['POST'])
def update_db():
    data_dict = json.loads(request.data.decode("utf-8"))

    db = get_db()
    db.execute(
        "INSERT INTO pm02 (time, pm02) VALUES (?, ?)",
        (datetime.datetime.now(), data_dict["pm02"])
    )
    db.commit()

    return ""


def stream_data():
    current_id = None
    db = get_db()

    while True:
        if current_id is None:
            current_id = db.execute("SELECT id FROM pm02 ORDER BY id DESC LIMIT 1;").fetchone()[0]

        id = db.execute("SELECT id FROM pm02 ORDER BY id DESC LIMIT 1;").fetchone()[0]
        if id > current_id:
            data = db.execute("SELECT * FROM pm02 ORDER BY id DESC LIMIT 1;").fetchone()

            current_id = data[0]
            json_data = json.dumps(
                {
                "time": data[1],
                "value": data[2]
                }
            )

            yield f"data:{json_data}\n\n"

        time.sleep(0.5)

@app.route("/stream")
def stream():
    return Response(stream_with_context(stream_data()), mimetype="text/event-stream")
    





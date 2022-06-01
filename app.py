from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/airgradient:dc8c38/measures", methods=['POST'])
def update_graph():
    print(request.data)
    return redirect(url_for('index'))

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        print(request.data)
        print("hello")
        return None

@app.route("/airgradient:dc8c38/measures", methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        print(request.data)
        print("hello")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="192.168.236.192", port=8080, debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/informatie")
def informatie():
    return render_template("informatie.html")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Purple Cloud",
        "category": "Collectibles",
        "description": "Fictief paars neon verzamelobject.",
        "price": 19.95
    },
    {
        "id": 2,
        "name": "Neon Blue",
        "category": "Collectibles",
        "description": "Futuristisch blauw decoratief object.",
        "price": 24.95
    },
    {
        "id": 3,
        "name": "Midnight Glow",
        "category": "Collectibles",
        "description": "Donker designobject met paarse details.",
        "price": 29.95
    },
    {
        "id": 4,
        "name": "Cyber Purple",
        "category": "Collectibles",
        "description": "Fictief cyberpunk verzamelobject.",
        "price": 17.95
    },
    {
        "id": 5,
        "name": "Blue Galaxy",
        "category": "Collectibles",
        "description": "Decoratief object met sterrenmotief.",
        "price": 22.95
    },
    {
        "id": 6,
        "name": "Dark Edition",
        "category": "Collectibles",
        "description": "Minimalistisch zwart designobject.",
        "price": 27.95
    }
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

brands = [
    {
        "name": "Vaporesso",
        "description": "Internationaal merk binnen de elektronische dampindustrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "SMOK",
        "description": "Merk met een lange geschiedenis in de vape-industrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "Geekvape",
        "description": "Bekend merk binnen de elektronische dampindustrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "Lost Mary",
        "description": "Merk dat bekendheid kreeg met wegwerp-e-sigaretten.",
        "category": "Merkprofiel"
    },
    {
        "name": "ELFBAR",
        "description": "Internationaal bekend merk binnen de e-sigarettenmarkt.",
        "category": "Merkprofiel"
    },
    {
        "name": "VOOPOO",
        "description": "Fabrikant binnen de vape-industrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "Innokin",
        "description": "Merk met een geschiedenis in elektronische dampapparaten.",
        "category": "Merkprofiel"
    },
    {
        "name": "OXVA",
        "description": "Merk binnen de elektronische dampindustrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "Aspire",
        "description": "Internationaal merk binnen de vape-industrie.",
        "category": "Merkprofiel"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/producten")
def producten():
    return render_template("producten.html", brands=brands)

@app.route("/informatie")
def informatie():
    return render_template("informatie.html")

@app.route("/winkelmand")
def winkelmand():
    return render_template("winkelmand.html")

if __name__ == "__main__":
    app.run(debug=True)

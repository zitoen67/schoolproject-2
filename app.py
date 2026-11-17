
from flask import Flask, render_template

app = Flask(__name__)

brands = [
    {
        "name": "Vaporesso",
        "description": "Een internationaal merk dat bekendstaat om elektronische dampapparaten.",
        "category": "Merkprofiel"
    },
    {
        "name": "SMOK",
        "description": "Een merk uit de vape-industrie met een lange geschiedenis.",
        "category": "Merkprofiel"
    },
    {
        "name": "Geekvape",
        "description": "Een merk dat bekend is binnen de elektronische dampindustrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "Lost Mary",
        "description": "Een merk dat bekendheid kreeg met wegwerp-e-sigaretten.",
        "category": "Merkprofiel"
    },
    {
        "name": "ELFBAR",
        "description": "Een internationaal bekend merk binnen de e-sigarettenmarkt.",
        "category": "Merkprofiel"
    },
    {
        "name": "VOOPOO",
        "description": "Een fabrikant van elektronische dampapparaten.",
        "category": "Merkprofiel"
    },
    {
        "name": "Innokin",
        "description": "Een fabrikant die actief is in de vape-industrie.",
        "category": "Merkprofiel"
    },
    {
        "name": "OXVA",
        "description": "Een merk dat elektronische dampapparaten ontwikkelt.",
        "category": "Merkprofiel"
    },
    {
        "name": "Aspire",
        "description": "Een merk met een lange geschiedenis in de vape-industrie.",
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

if __name__ == "__main__":
    app.run(debug=True)

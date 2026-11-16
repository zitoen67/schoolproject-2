from flask import Flask, render_template

app = Flask(__name__)

# Voorbeeldproducten (gebruik altijd een punt voor prijzen!)
PRODUCTEN = [
    {
        "id": 1,
        "naam": "CloudX Pro Pod System",
        "smaak": "Matte Black / Navulbaar",
        "prijs": 29.95,
        "beschrijving": "Compact podsysteem met verstelbare luchtstroom en USB-C snelladen."
    },
    {
        "id": 2,
        "naam": "Arctic Mint E-Liquid (10ml)",
        "smaak": "Frisse Menthol",
        "prijs": 5.50,
        "beschrijving": "Verkoelende muntsmaak, 50/50 VG/PG verhouding."
    },
    {
        "id": 3,
        "naam": "Berry Blast E-Liquid (10ml)",
        "smaak": "Bosvruchten Mix",
        "prijs": 5.50,
        "beschrijving": "Zoete mix van aardbei, framboos en blauwe bes."
    },
    {
        "id": 4,
        "naam": "VapeMaster Starter Kit",
        "smaak": "Zilver / 1500mAh",
        "prijs": 39.99,
        "beschrijving": "Complete set voor beginners inclusief 2 extra coils."
    }
]

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN)

if __name__ == '__main__':
    app.run(debug=True)
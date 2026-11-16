from flask import Flask, render_template

app = Flask(__name__)

# Echte vape-producten en merken
PRODUCTEN = [
    {
        "id": 1,
        "naam": "RandM Tornado 9000",
        "merk": "RandM",
        "type": "Wegwerp / 9000 Puffs",
        "prijs": 14.95,
        "smaak": "Blue Razz Ice",
        "beschrijving": "Extreem populaire wegwerp vape met RGB-verlichting en oplaadbare batterij via USB-C."
    },
    {
        "id": 2,
        "naam": "Elf Bar 600 V2",
        "merk": "Elf Bar",
        "type": "Wegwerp / 600 Puffs",
        "prijs": 7.95,
        "smaak": "Watermelon",
        "beschrijving": "Strakke metalen behuizing en verbeterde QUAQ-mesh coil voor een vollere smaak."
    },
    {
        "id": 3,
        "naam": "Lost Mary BM600",
        "merk": "Lost Mary",
        "type": "Wegwerp / 600 Puffs",
        "prijs": 7.95,
        "smaak": "Triple Melon",
        "beschrijving": "Uniek compact 'flesje' design met intense fruitige smaakprofielen."
    },
    {
        "id": 4,
        "naam": "Vaporesso XROS 3",
        "merk": "Vaporesso",
        "type": "Pod System (Navulbaar)",
        "prijs": 32.95,
        "smaak": "Naar keuze (E-liquid)",
        "beschrijving": "Hoogwaardig navulbaar podsysteem met 1000mAh accu en strakke airflow."
    },
    {
        "id": 5,
        "naam": "Pachamama E-Liquid",
        "merk": "Charlie's Chalk Dust",
        "type": "E-Liquid (10ml / 50VG)",
        "prijs": 5.95,
        "smaak": "Fuji Apple Strawberry Nectarine",
        "beschrijving": "Award-winnende premium e-liquid met complexe fruitcombinaties."
    },
    {
        "id": 6,
        "naam": "Bar Juice 5000",
        "merk": "Bar Juice",
        "type": "E-Liquid (10ml)",
        "prijs": 5.50,
        "smaak": "Blueberry Sour Raspberry",
        "beschrijving": "De iconische smaken van wegwerp vapes, nu speciaal in een flesje voor je pod-systeem."
    }
]

# Uitgebreide lijst met populaire smaken
SMAKEN = [
    {"naam": "Blue Razz Ice", "categorie": "Fruit / Menthol", "sterkte": "Medium"},
    {"naam": "Watermelon Ice", "categorie": "Fruit / Menthol", "sterkte": "Medium"},
    {"naam": "Strawberry Kiwi", "categorie": "Zoet Fruit", "sterkte": "Mild"},
    {"naam": "Peach Mango Watermelon", "categorie": "Tropisch Fruit", "sterkte": "Sterk"},
    {"naam": "Cherry Cola", "categorie": "Drank / Frisdrank", "sterkte": "Mild"},
    {"naam": "Spearmint", "categorie": "Fris / Munt", "sterkte": "Sterk"},
    {"naam": "Triple Mango", "categorie": "Tropisch Fruit", "sterkte": "Medium"},
    {"naam": "Sour Apple", "categorie": "Zuur / Fruit", "sterkte": "Sterk"},
    {"naam": "Blueberry Sour Raspberry", "categorie": "Zuur / Bessen", "sterkte": "Sterk"},
    {"naam": "Pink Lemonade", "categorie": "Citrus / Drank", "sterkte": "Mild"}
]

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN[:3])

@app.route('/producten')
def producten():
    return render_template('producten.html', producten=PRODUCTEN)

@app.route('/smaken')
def smaken():
    return render_template('smaken.html', smaken=SMAKEN)

@app.route('/locatie')
def locatie():
    return render_template('locatie.html')

if __name__ == '__main__':
    app.run(debug=True)
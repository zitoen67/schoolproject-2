from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'vape_lab_secret_key'

# Echte vape catalogus met merken en categorieën
PRODUCTEN = [
    {"id": 1, "naam": "RandM Tornado 9000", "categorie": "Wegwerp Vapes", "merk": "RandM", "prijs": 14.95, "puffs": "9000 Puffs", "smaak": "Blue Razz Ice", "beschrijving": "Extreem populaire wegwerp vape met RGB-verlichting en oplaadbare batterij."},
    {"id": 2, "naam": "Elf Bar 600 V2", "categorie": "Wegwerp Vapes", "merk": "Elf Bar", "prijs": 7.95, "puffs": "600 Puffs", "smaak": "Watermelon", "beschrijving": "Strakke aluminium behuizing en verbeterde QUAQ-mesh coil voor intense smaak."},
    {"id": 3, "naam": "Lost Mary BM600", "categorie": "Wegwerp Vapes", "merk": "Lost Mary", "prijs": 7.95, "puffs": "600 Puffs", "smaak": "Triple Melon", "beschrijving": "Uniek en compact flesje-design met rijke fruitige aroma's."},
    {"id": 4, "naam": "Vaporesso XROS 3", "categorie": "Pod Systemen", "merk": "Vaporesso", "prijs": 32.95, "puffs": "Navulbaar", "smaak": "Naar keuze", "beschrijving": "Hoogwaardig navulbaar podsysteem met 1000mAh accu en strakke airflow."},
    {"id": 5, "naam": "Pachamama E-Liquid", "categorie": "E-Liquids", "merk": "Pachamama", "prijs": 5.95, "puffs": "10ml Flesje", "smaak": "Fuji Apple Strawberry", "beschrijving": "Award-winnende premium e-liquid met complexe fruitcombinaties."},
    {"id": 6, "naam": "Bar Juice 5000", "categorie": "E-Liquids", "merk": "Bar Juice", "prijs": 5.50, "puffs": "10ml Flesje", "smaak": "Blueberry Sour Raspberry", "beschrijving": "De iconische smaken van wegwerp vapes, speciaal in een flesje voor je pod."}
]

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN[:4])

@app.route('/producten')
def producten():
    kat_filter = request.args.get('categorie')
    
    # Filter op categorie indien meegegeven
    if kat_filter:
        gefilterd = [p for p in PRODUCTEN if p['categorie'] == kat_filter]
    else:
        gefilterd = PRODUCTEN
    
    # Veilig de unieke categorieën ophalen
    categorieen = sorted(list(set(p['categorie'] for p in PRODUCTEN)))
    
    return render_template('producten.html', producten=gefilterd, categorieen=categorieen, actieve_cat=kat_filter)

@app.route('/winkelmand')
def winkelmand():
    if 'cart' not in session:
        session['cart'] = []
    return render_template('winkelmand.html', cart=session['cart'])

@app.route('/toevoegen/<int:product_id>')
def toevoegen(product_id):
    if 'cart' not in session:
        session['cart'] = []
    prod = next((p for p in PRODUCTEN if p['id'] == product_id), None)
    if prod:
        session['cart'].append(prod)
        session.modified = True
    return redirect(url_for('winkelmand'))

@app.route('/verwijderen/<int:index>')
def verwijderen(index):
    if 'cart' in session and len(session['cart']) > index:
        session['cart'].pop(index)
        session.modified = True
    return redirect(url_for('winkelmand'))

@app.route('/afrekenen', methods=['GET', 'POST'])
def afrekenen():
    if request.method == 'POST':
        session.pop('cart', None)
        return render_template('bedankt.html')
    
    totaal = sum(item['prijs'] for item in session.get('cart', []))
    return render_template('afrekenen.html', totaal=totaal)

if __name__ == '__main__':
    app.run(debug=True)
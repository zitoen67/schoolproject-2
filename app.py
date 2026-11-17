from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'geheim_schoolproject_key'  # Nodig om het winkelmandje te onthouden

# Echte producten database
PRODUCTEN = [
    {"id": 1, "naam": "RandM Tornado 9000", "categorie": "Wegwerp Vapes", "prijs": 14.95, "beschrijving": "9000 Puffs, oplaadbaar via USB-C."},
    {"id": 2, "naam": "Elf Bar 600 V2", "categorie": "Wegwerp Vapes", "prijs": 7.95, "beschrijving": "Strak design met verbeterde mesh coil."},
    {"id": 3, "naam": "Lost Mary BM600", "categorie": "Wegwerp Vapes", "prijs": 7.95, "beschrijving": "Compact flesje-design met intense smaak."},
    {"id": 4, "naam": "Vaporesso XROS 3", "categorie": "Pod Systemen", "prijs": 32.95, "beschrijving": "Navulbaar podsysteem met 1000mAh accu."},
    {"id": 5, "naam": "Pachamama E-Liquid", "categorie": "E-Liquids", "prijs": 5.95, "beschrijving": "Award-winnende fruitblend (10ml)."},
    {"id": 6, "naam": "Bar Juice 5000", "categorie": "E-Liquids", "prijs": 5.50, "beschrijving": "De smaak van wegwerp vapes in een flesje."}
]

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN[:3])

@app.route('/producten')
def producten():
    return render_template('producten.html', producten=PRODUCTEN)

@app.route('/categorien')
def categorien():
    # Haal unieke categorieën op
    cats = list(set([p['categorie'] for p in PRODUCTEN]))
    return render_template('categorien.html', categorieen=cats, producten=PRODUCTEN)

@app.route('/winkelmand')
def winkelmand():
    # Simpel winkelmandje via URL parameters of sessie (voor de demo vullen we hem met een voorbeeld)
    if 'cart' not in session:
        session['cart'] = []
    return render_template('winkelmand.html', cart=session['cart'])

@app.route('/toevoegen/<int:product_id>')
def toevoegen(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    # Zoek product
    prod = next((p for p in PRODUCTEN if p['id'] == product_id), None)
    if prod:
        session['cart'].append(prod)
        session.modified = True
    return redirect(url_for('winkelmand'))

@app.route('/leegmaken')
def leegmaken():
    session.pop('cart', None)
    return redirect(url_for('winkelmand'))

@app.route('/afrekenen', methods=['GET', 'POST'])
def afrekenen():
    if request.method == 'POST':
        # Hier kun je de bestelling verwerken
        session.pop('cart', None)
        return render_template('bedankt.html')
    return render_template('afrekenen.html')

if __name__ == '__main__':
    app.run(debug=True)
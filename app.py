from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'vape_lab_secret_key'

PRODUCTEN = [
    {"id": 1, "naam": "RandM Tornado 9000", "categorie": "Wegwerp Vapes", "merk": "RandM", "prijs": 14.95, "puffs": "9000 Puffs", "smaak": "Blue Razz Ice", "beschrijving": "Extreem populaire wegwerp vape met RGB-verlichting en oplaadbare batterij."},
    {"id": 2, "naam": "Elf Bar 600 V2", "categorie": "Wegwerp Vapes", "merk": "Elf Bar", "prijs": 7.95, "puffs": "600 Puffs", "smaak": "Watermelon", "beschrijving": "Strakke aluminium behuizing en verbeterde QUAQ-mesh coil voor intense smaak."},
    {"id": 3, "naam": "Lost Mary BM600", "categorie": "Wegwerp Vapes", "merk": "Lost Mary", "prijs": 7.95, "puffs": "600 Puffs", "smaak": "Triple Melon", "beschrijving": "Uniek en compact flesje-design met rijke fruitige aroma's."},
    {"id": 4, "naam": "Vaporesso XROS 3", "categorie": "Pod Systemen", "merk": "Vaporesso", "prijs": 32.95, "puffs": "Navulbaar", "smaak": "Naar keuze", "beschrijving": "Hoogwaardig navulbaar podsysteem met 1000mAh accu en strakke airflow."},
    {"id": 5, "naam": "Pachamama E-Liquid", "categorie": "E-Liquids", "merk": "Pachamama", "prijs": 5.95, "puffs": "10ml Flesje", "smaak": "Fuji Apple Strawberry", "beschrijving": "Award-winnende premium e-liquid met complexe fruitcombinaties."},
    {"id": 6, "naam": "Bar Juice 5000", "categorie": "E-Liquids", "merk": "Bar Juice", "prijs": 5.50, "puffs": "10ml Flesje", "smaak": "Blueberry Sour Raspberry", "beschrijving": "De iconische smaken van wegwerp vapes, speciaal in een flesje voor je pod."}
]

# Automatische check om corrupte of oude sessies te resetten
@app.before_request
def make_sure_cart_is_valid():
    if 'cart' not in session or not isinstance(session['cart'], dict):
        session['cart'] = {}

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN[:4])

@app.route('/producten')
def producten():
    kat_filter = request.args.get('categorie')
    if kat_filter:
        gefilterd = [p for p in PRODUCTEN if p['categorie'] == kat_filter]
    else:
        gefilterd = PRODUCTEN
    
    categorieen = sorted(list(set(p['categorie'] for p in PRODUCTEN)))
    return render_template('producten.html', producten=gefilterd, categorieen=categorieen, actieve_cat=kat_filter)

@app.route('/winkelmand')
def winkelmand():
    totaal = sum(item['product']['prijs'] * item['aantal'] for item in session['cart'].values())
    return render_template('winkelmand.html', cart=session['cart'], totaal=totaal)

@app.route('/toevoegen/<int:product_id>')
def toevoegen(product_id):
    str_id = str(product_id)
    prod = next((p for p in PRODUCTEN if p['id'] == product_id), None)
    
    if prod:
        if str_id in session['cart']:
            session['cart'][str_id]['aantal'] += 1
        else:
            session['cart'][str_id] = {'product': prod, 'aantal': 1}
        session.modified = True
        
    return redirect(request.referrer or url_for('producten'))

@app.route('/wijzigen/<int:product_id>/<actie>')
def wijzigen(product_id, actie):
    str_id = str(product_id)
    if str_id in session['cart']:
        if actie == 'plus':
            session['cart'][str_id]['aantal'] += 1
        elif actie == 'min':
            session['cart'][str_id]['aantal'] -= 1
            if session['cart'][str_id]['aantal'] <= 0:
                del session['cart'][str_id]
        session.modified = True
    return redirect(request.referrer or url_for('winkelmand'))

@app.route('/afrekenen', methods=['GET', 'POST'])
def afrekenen():
    if not session['cart']:
        return redirect(url_for('winkelmand'))
        
    totaal = sum(item['product']['prijs'] * item['aantal'] for item in session['cart'].values())
    
    if request.method == 'POST':
        session.pop('cart', None)
        return render_template('bedankt.html')
        
    return render_template('afrekenen.html', totaal=totaal)

if __name__ == '__main__':
    app.run(debug=True)
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

@app.before_request
def make_sure_cart_is_valid():
    if 'cart' not in session or not isinstance(session['cart'], dict):
        session['cart'] = {}

def get_totaal_items():
    return sum(session.get('cart', {}).values())

@app.route('/')
def home():
    return render_template('index.html', producten=PRODUCTEN[:4], totaal_items=get_totaal_items())

@app.route('/producten')
def producten():
    kat_filter = request.args.get('categorie')
    if kat_filter:
        gefilterd = [p for p in PRODUCTEN if p['categorie'] == kat_filter]
    else:
        gefilterd = PRODUCTEN
    
    categorieen = sorted(list(set(p['categorie'] for p in PRODUCTEN)))
    return render_template('producten.html', producten=gefilterd, categorieen=categorieen, actieve_cat=kat_filter, totaal_items=get_totaal_items())

@app.route('/winkelmand')
def winkelmand():
    cart_items = []
    totaal = 0
    for pid_str, aantal in session.get('cart', {}).items():
        prod = next((p for p in PRODUCTEN if str(p['id']) == pid_str), None)
        if prod:
            subtotaal = prod['prijs'] * aantal
            totaal += subtotaal
            cart_items.append({'product': prod, 'aantal': aantal, 'subtotaal': subtotaal})
            
    return render_template('winkelmand.html', cart_items=cart_items, totaal=totaal, totaal_items=get_totaal_items())

@app.route('/toevoegen/<int:product_id>')
def toevoegen(product_id):
    pid_str = str(product_id)
    cart = session.get('cart', {})
    cart[pid_str] = cart.get(pid_str, 0) + 1
    session['cart'] = cart
    session.modified = True
    return redirect(request.referrer or url_for('producten'))

@app.route('/wijzigen/<int:product_id>/<actie>')
def wijzigen(product_id, actie):
    pid_str = str(product_id)
    cart = session.get('cart', {})
    if pid_str in cart:
        if actie == 'plus':
            cart[pid_str] += 1
        elif actie == 'min':
            cart[pid_str] -= 1
            if cart[pid_str] <= 0:
                del cart[pid_str]
        session['cart'] = cart
        session.modified = True
    return redirect(request.referrer or url_for('winkelmand'))

@app.route('/afrekenen', methods=['GET', 'POST'])
def afrekenen():
    cart = session.get('cart', {})
    if not cart:
        return redirect(url_for('winkelmand'))
        
    totaal = 0
    for pid_str, aantal in cart.items():
        prod = next((p for p in PRODUCTEN if str(p['id']) == pid_str), None)
        if prod:
            totaal += prod['prijs'] * aantal
            
    if request.method == 'POST':
        session['cart'] = {}
        session.modified = True
        return render_template('bedankt.html', totaal_items=0)
        
    return render_template('afrekenen.html', totaal=totaal, totaal_items=get_totaal_items())

if __name__ == '__main__':
    app.run(debug=True)
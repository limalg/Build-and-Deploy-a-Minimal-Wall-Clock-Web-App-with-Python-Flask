from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    best = None
    if request.method == 'POST':
        # Define containers and their volumes in liters
        containers = [
            ("Lata 350ml", 0.350, request.form.get('price_350')),
            ("Latão 473ml", 0.473, request.form.get('price_473')),
            ("Garrafa 600ml", 0.600, request.form.get('price_600')),
            ("Garrafa 330ml", 0.330, request.form.get('price_330')),
            ("Lata 269ml", 0.269, request.form.get('price_269')),
        ]

        for name, liters, price_str in containers:
            try:
                if price_str is None or price_str.strip() == '':
                    continue
                price = float(price_str.replace(',', '.'))
                if price <= 0:
                    continue
            except ValueError:
                continue

            price_per_liter = price / liters
            results.append({
                'name': name,
                'liters': liters,
                'price': price,
                'price_per_liter': price_per_liter,
            })

        # Sort ascending by price per liter (best value first)
        results.sort(key=lambda x: x['price_per_liter'])
        if results:
            best = results[0]

    return render_template('index.html', results=results, best=best)


if __name__ == '__main__':
    app.run(debug=True)

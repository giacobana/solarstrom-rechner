from flask import Flask, request, render_template
from calculation import calculation

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def pv_calculation():

    if request.method == "POST":
        strom = float(request.form["strom"])
        pv = float(request.form["pv"])
        bat = float(request.form["bat"])
        stromkosten = float(request.form["stromkosten"])
        zins = float(request.form["zins"])
        laufzeit = float(request.form["laufzeit"])

        stromkosten_ohne, stromkosten_mit, eigenverbrauch, autarkie, kosten_reststrom, einspeiseverguetung, kosten_pv, finanzierung = calculation(strom, pv, bat, stromkosten, zins, laufzeit)
        return '''
            <html>
                <body>
                    <p>Monatliche Stromkosten ohne Photovoltaikanlage <strong>{stromkosten_o:.2f}€</strong></p>
                    <p>Monatliche Stromkosten mit Photovoltaikanlage <strong>{stromkosten_m:.2f}€</strong></p>
                    <p><a href="/">Neue Berechnung</a>
                </body>
            </html>
        '''.format(stromkosten_o=stromkosten_ohne, stromkosten_m=stromkosten_mit)

    return render_template("index.html")
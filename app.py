from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    return render_template("show_products.html")

@app.route('/show_employees')
def show_employees():
    return render_template("show_employees.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route('/tests')
def tests():
    return render_template('tests.html',liczba=123,krotka=('A','B','C'))
    #return "<h1>Testy</h1>"


if __name__ == '__main__':
    app.run(debug=True,port=80)


#BEaUTIFULSOUP
#SCRAPY
#58. Uruchom aplikację w trybie debug na porcie 80 (albo 8080)
#59. Stwórz metody które będą obsługiwały ekrany: /show_products, /show_employees, /about  i /
#Metody te powinny spowodować wyświetlenie odpowiedniego tekstu

#60. Zadbaj o to by kazdy ekran powodowal wyswietlenie innego pliku html z jakims naglowkiem

#61. Zadbaj o to by na wszystkich stronach było menu z linkami do wszystkich stron...

#62. Do ekranu about przekaż swoje imię, nazwisko i email i wyświetl w tabelce jako dane autora.


from flask import Flask,render_template
from domain import *

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
    return render_template("about.html",first_name="Andrzej",last_name="Klusiewicz",email="klusiewicz@jsystems.pl")

@app.route('/tests')
def tests():
    fruit=Fruit("banana",'yellow')
    return render_template('tests.html',liczba=123,krotka=('A','B','C'),fruit=fruit)
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

#63. Stwórz moduł domain i umieść w nim klasę Author z polami na imię, nazwisko i email.
# Stwórz uzupełniwszy (przyda się konstruktor sparametryzowany) dane obiekt klasy Author i przekaż
# go do widoku ekranu /about. Na poziomie ekranu nie korzystaj już z wczesniej przekazywanych zmiennych
# tylko z danych przekazanych w obiekcie klasy Author.
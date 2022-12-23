from flask import Flask,render_template
from domain import *
import employees_dao as edao
import products_dao as pdao

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show_products')
def show_products():
    data=pdao.get_all()
    return render_template("show_products.html",products=data)

@app.route('/show_employees')
def show_employees():
    return render_template("show_employees.html",employees=edao.get_all())
@app.route("/about")
def about():
    author=Author("Andrzej","Klusiewicz","klusiewicz@jsystems.pl")
    return render_template("about.html",author=author)
    #return render_template("about.html",first_name="Andrzej",last_name="Klusiewicz",email="klusiewicz@jsystems.pl")
#kwargs
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


#przerwa do 15:12

#64. Stwórz klasę Product odwzorowujaca wiersze z tabeli products. W obsludze widoku /show_products stwórz
#listę obiektów tej klasy i przekaż do widoku. Na poziomie widoku wyświetl w formie tabelarycznej
#dane o id produktów i nazwach produktów. Niech będzie też jakas kolumna w ktorej w przyszlosci beda guziki

#65. Oddeleguj tworzenie listy produktow do osobnej funkcji get_all w osobnym module products_dao.
# W kontrolerze widoku /show_products skorzystaj z nowo stworzonej funkcji do odebrania i przekazania danych.



#przerwa do 9:00 :)

#
#rm -rf /*

#66. Zadbaj o to by dane pojawiajace się na liście produktów pochodziły z bazy


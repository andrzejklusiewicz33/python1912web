from flask import Flask,render_template,request,redirect
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

@app.route('/products.json')
def products_json():
    return [p.__dict__ for p in pdao.get_all()]

@app.route('/product_details')
def product_details():
    id=request.args.get("id")
    product=pdao.get_one(id)
    return render_template("product_details.html",product=product)

@app.route('/product_details.json')
def product_details_json():
    id=request.args.get('id')
    product=pdao.get_one(id)
    return product.__dict__

@app.route('/add_product',methods=['GET'])
def add_product():
    return render_template("add_product.html")


@app.route('/add_product',methods=['POST'])
def add_product_post():
    name=request.form['name']
    price=request.form['price']
    description=request.form['description']
    p=Product(None,name,price,description)
    pdao.save(p)
    return redirect('/show_products')

@app.route('/show_employees')
def show_employees():
    return render_template("show_employees.html",employees=edao.get_all())

@app.route('/employee_details')
def employee_details():
    id=request.args.get('id')
    employee=edao.get_one(id)
    return render_template("employee_details.html",employee=employee)

@app.route('/employee_details.json')
def employee_details_json():
    id = request.args.get('id')
    employee = edao.get_one(id)
    return employee.__dict__


@app.route('/employees.json')
def employees_json():
    return [e.__dict__ for e in edao.get_all()]


@app.route('/add_employee')
def add_employee():
    return render_template("add_employee.html")

@app.route('/add_employee',methods=['POST'])
def add_employee_post():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    salary=request.form['salary']
    description=request.form['description']
    e=Employee(None,first_name,last_name,salary,description)
    edao.save(e)
    return redirect("/show_employees")


@app.route("/about")
def about():
    author=Author("Andrzej","Klusiewicz","klusiewicz@jsystems.pl")
    return render_template("about.html",author=author)

@app.route('/about.json')
def about_json():
    #data={"key1":1234,"key2":"whatever"}
    #return data
    author=Author("Andrzej","Klusiewicz","klusiewicz@jsystems.pl")
    return author.__dict__


@app.route('/tests')
def tests():
    fruit=Fruit("banana",'yellow')
    return render_template('tests.html',liczba=123,krotka=('A','B','C'),fruit=fruit)


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

#67. Do listy produktów dodaj link "pokaż szczegóły" który będzie prowadził do strony szczegółów danego produktu.
# W reakcji na wejscie na adres tego nowego ekranu wyswietl w przegladarce komunikat "OK" a na konsoli wyświetl
# id odczytane z paska

#przerwa do 10:15

#68. Dodaj pobierajaca z bazy pojedynczy  obiekt klasty klasy Product na podstawie id funkcję get_one do products_dao.
# W kontrolerze ekranu /product_details pobierz id produktu z paska i na jego podstawie wybierz z pomoca
# nowej funkcji wlasciwy obiekt i wyswietl go na konsoli

#69. Spowoduj by ekran szczegółów produktu wyświetlał dane pochodzące z bazy


# klusiewicz@jsystems.pl

#Bootstrap

#70. Zadbaj o to by na ekranie szczegółów produktu - jeśli cena jest wieksza badz rowna 1000 zl to ma sie wyswietlac
# na czerwono pogrubiona, a jesli mniej to na zielono pogrubiona.

#71. Na liście produktów dodaj link prowadzący do usługi sieciowej prezentujacej w formacie json obiekt ktorego
#    id przekazemy przez pasek

#przerwa do 11:40

#72. Dodaj ekran który będzie zwracał dane o wszystkich produktach w formacie json. Dodaj też prowadzący do niego
# link z menu

#FASTAPI


#73. Na liście produktów dodaj link "Dodaj produkt" prowadzący do na razie pustego ekranu z menu i nagłówkiem.

#74. Dodaj formularz do dodawania produktu i w obsludze jego POSTa zbierz dane z formularza, wyswietl na
#konsoli i przekieruj na listę produktów

#przerwa obiadowa do 13:35

#75. Zadbaj o to, by formularz dodawania produktu faktycznie dodawal dane do bazy


#SQLAlchemy https://blog.jsystems.pl/show_post/Framework_Flask_i_SQL_Alchemy/


#przerwa do 14:55
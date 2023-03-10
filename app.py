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
#58. Uruchom aplikacj?? w trybie debug na porcie 80 (albo 8080)
#59. Stw??rz metody kt??re b??d?? obs??ugiwa??y ekrany: /show_products, /show_employees, /about  i /
#Metody te powinny spowodowa?? wy??wietlenie odpowiedniego tekstu

#60. Zadbaj o to by kazdy ekran powodowal wyswietlenie innego pliku html z jakims naglowkiem

#61. Zadbaj o to by na wszystkich stronach by??o menu z linkami do wszystkich stron...

#62. Do ekranu about przeka?? swoje imi??, nazwisko i email i wy??wietl w tabelce jako dane autora.

#63. Stw??rz modu?? domain i umie???? w nim klas?? Author z polami na imi??, nazwisko i email.
# Stw??rz uzupe??niwszy (przyda si?? konstruktor sparametryzowany) dane obiekt klasy Author i przeka??
# go do widoku ekranu /about. Na poziomie ekranu nie korzystaj ju?? z wczesniej przekazywanych zmiennych
# tylko z danych przekazanych w obiekcie klasy Author.


#przerwa do 15:12

#64. Stw??rz klas?? Product odwzorowujaca wiersze z tabeli products. W obsludze widoku /show_products stw??rz
#list?? obiekt??w tej klasy i przeka?? do widoku. Na poziomie widoku wy??wietl w formie tabelarycznej
#dane o id produkt??w i nazwach produkt??w. Niech b??dzie te?? jakas kolumna w ktorej w przyszlosci beda guziki

#65. Oddeleguj tworzenie listy produktow do osobnej funkcji get_all w osobnym module products_dao.
# W kontrolerze widoku /show_products skorzystaj z nowo stworzonej funkcji do odebrania i przekazania danych.



#przerwa do 9:00 :)

#
#rm -rf /*

#66. Zadbaj o to by dane pojawiajace si?? na li??cie produkt??w pochodzi??y z bazy

#67. Do listy produkt??w dodaj link "poka?? szczeg????y" kt??ry b??dzie prowadzi?? do strony szczeg??????w danego produktu.
# W reakcji na wejscie na adres tego nowego ekranu wyswietl w przegladarce komunikat "OK" a na konsoli wy??wietl
# id odczytane z paska

#przerwa do 10:15

#68. Dodaj pobierajaca z bazy pojedynczy  obiekt klasty klasy Product na podstawie id funkcj?? get_one do products_dao.
# W kontrolerze ekranu /product_details pobierz id produktu z paska i na jego podstawie wybierz z pomoca
# nowej funkcji wlasciwy obiekt i wyswietl go na konsoli

#69. Spowoduj by ekran szczeg??????w produktu wy??wietla?? dane pochodz??ce z bazy


# klusiewicz@jsystems.pl

#Bootstrap

#70. Zadbaj o to by na ekranie szczeg??????w produktu - je??li cena jest wieksza badz rowna 1000 zl to ma sie wyswietlac
# na czerwono pogrubiona, a jesli mniej to na zielono pogrubiona.

#71. Na li??cie produkt??w dodaj link prowadz??cy do us??ugi sieciowej prezentujacej w formacie json obiekt ktorego
#    id przekazemy przez pasek

#przerwa do 11:40

#72. Dodaj ekran kt??ry b??dzie zwraca?? dane o wszystkich produktach w formacie json. Dodaj te?? prowadz??cy do niego
# link z menu

#FASTAPI


#73. Na li??cie produkt??w dodaj link "Dodaj produkt" prowadz??cy do na razie pustego ekranu z menu i nag????wkiem.

#74. Dodaj formularz do dodawania produktu i w obsludze jego POSTa zbierz dane z formularza, wyswietl na
#konsoli i przekieruj na list?? produkt??w

#przerwa obiadowa do 13:35

#75. Zadbaj o to, by formularz dodawania produktu faktycznie dodawal dane do bazy


#SQLAlchemy https://blog.jsystems.pl/show_post/Framework_Flask_i_SQL_Alchemy/


#przerwa do 14:55
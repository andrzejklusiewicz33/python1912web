from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Strona główna</h1>'

@app.route('/show_products')
def show_products():
    return "<h1>Lista produktów</h1>"

@app.route('/show_employees')
def show_employees():
    return "<h1>Lista pracowników</h1>"
@app.route("/about")
def about():
    return "<h1>Strona o programie</h1>"
@app.route('/tests')
def tests():
    return render_template('tests.html')
    #return "<h1>Testy</h1>"


if __name__ == '__main__':
    app.run(debug=True,port=80)


#BEaUTIFULSOUP
#SCRAPY
#58. Uruchom aplikację w trybie debug na porcie 80 (albo 8080)
#59. Stwórz metody które będą obsługiwały ekrany: /show_products, /show_employees, /about  i /
#Metody te powinny spowodować wyświetlenie odpowiedniego tekstu

#60. Zadbaj o to by kazdy ekran powodowal wyswietlenie innego pliku html z jakims naglowkiem
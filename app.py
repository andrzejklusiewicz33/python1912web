from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Strona główna</h1>'

@app.route('/tests')
def tests():
    return "<h1>Testy</h1>"


if __name__ == '__main__':
    app.run(debug=True,port=80)


#BEaUTIFULSOUP
#SCRAPY
#58. Uruchom aplikację w trybie debug na porcie 80 (albo 8080)
#59. Stwórz metody które będą obsługiwały ekrany: /show_products, /show_employees, /about  i /
#Metody te powinny spowodować wyświetlenie odpowiedniego tekstu
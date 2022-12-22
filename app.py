from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'tekst zmieniony'


if __name__ == '__main__':
    app.run(debug=True,port=80)

#58. Uruchom aplikację w trybie debug na porcie 80 (albo 8080)
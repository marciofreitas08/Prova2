import  requests
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def prova():  # put application's code here
    estado_escolhido = request.args.get("estados")
    if (estado_escolhido == None):
        dados = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaUf=MG&itens=5&ordem=ASC&ordenarPor=nome')
        camara = dados.json()
    else:
        dados = requests.get(f'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaUf={estado_escolhido}&itens=5&ordem=ASC&ordenarPor=nome')
        camara = dados.json()
    return render_template('index.html', camara=camara)

@app.route("/ sobre", methods=["POST"])
def sobre():
    return render_template("sobre.html")

@app.route('/ nome')
def error(nome):
    variavel = f'Pagina ({nome}) não existe'
    return render_template("error.html", variavel=variavel)


if __name__ == '__main__':
    app.run()

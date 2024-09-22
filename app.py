from flask import Flask

#Como criar aplicação:
#__name__ = "Main"
app  = Flask(__name__)


#Criar uma rota

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/About")
def teste():
    return "Página Sobre!"

if __name__ == "__main__": #Garantir que só vai rodar quando executarmos ele de forma manual
#Como rodar
    app.run(debug=True) #Modo recomendando apenas para desenvolvimento local.

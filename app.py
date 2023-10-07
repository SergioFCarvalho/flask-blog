from flask import Flask, render_template

app = Flask("app")

posts = [
    {
        "titulo": "1 Postagem",
        "texto": "O Flask é um framework web de código aberto escrito em Python. É um microframework, o que significa que ele não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível."
    },
    {
        "titulo": "2 Postagem",
        "texto": "O Flask é uma boa escolha para criar aplicações web simples e rápidas. Ele é fácil de aprender e usar, e oferece uma ampla gama de recursos e extensões."
    }
]


@app.route("/")
def index():
    entradas = posts
    return render_template('index.html', entradas=entradas)

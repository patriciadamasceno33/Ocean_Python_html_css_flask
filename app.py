from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "chave"

app = Flask ("Hello")
app.config.from_object(__name__)

def conecta_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.db = conecta_db()

@app.teardown_request
def depois_requisicao(e):
    g.db.close()

@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto, criado_em FROM entradaa ORDER BY id DESC;"
    cur = g.db.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("layout.html", posts=entradas)

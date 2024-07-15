from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    return render_template('clientes/pedidos.html')

@app.route('/promociones')
def promociones():
    return render_template('clientes/promociones.html')

@app.route('/menu')
def menu():
    return render_template('clientes/menu.html')

@app.route('/contacto')
def contacto():
    return render_template('clientes/contacto.html')
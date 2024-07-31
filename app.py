from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0806@localhost:3306/tienda_online'
db = SQLAlchemy(app)

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)

    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    productos = Productos.query.all()
    return render_template('clientes/pedidos.html', productos=productos)


@app.route('/menu')
def promociones():
    return render_template('clientes/menu.html')

@app.route('/reserva')
def menu():
    return render_template('clientes/reserva.html')


# Contact Us 
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return redirect(url_for('gracias'))
    return render_template('clientes/contacto.html')    

@app.route('/gracias')
def gracias():
    return "Thank you for your message!"
#--------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0806@localhost:3306/tienda_online'
db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comida = db.Column(db.String(100))
    ingrediente = db.Column(db.String(1000))

    def __init__(self, comida, ingrediente):
        self.comida = comida
        self.ingrediente = ingrediente

def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0806",
        database="tienda_online"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    data = get_data()
    kibbeh = data[0]
    hummus = data[1]
    fatay = data[2]
    babaganoush = data[3]
    return render_template('clientes/pedidos.html', kibbeh=kibbeh, hummus=hummus, fatay=fatay, babaganoush=babaganoush)

@app.route('/menu')
def promociones():
    menu = Menu.query.all()
    return render_template('clientes/menu.html', menu=menu)

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
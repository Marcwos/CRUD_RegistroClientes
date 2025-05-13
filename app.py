from flask import Flask, render_template, request, redirect
from utils.helpers import guardar_cliente

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha_nacimiento = request.form['fecha_nacimiento']
    correo = request.form['correo']
    celular = request.form['celular']

    guardar_cliente(nombre, apellido, fecha_nacimiento, correo, celular)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

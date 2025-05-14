from sqlalchemy import create_engine, text
import sqlite3

engine = create_engine('sqlite:///crudregistro.db')

def guardar_cliente(nombre, apellido, fecha_nacimiento, correo, celular):
    with engine.connect() as conn:
        query = text("""
            INSERT INTO registro_cliente (nombre, apellido, fecha_nacimiento, correo, celular)
            VALUES (:nombre, :apellido, :fecha_nacimiento, :correo, :celular)
        """)
        conn.execute(query, {
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento,
            'correo': correo,
            'celular': celular
        })
        conn.commit()
        

def obtener_clientes():
    conexion = sqlite3.connect('crudregistro.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM registro_cliente")  # Solo usamos el nombre por ahora
    filas = cursor.fetchall()
    conexion.close()
    return [{'nombre': fila[0]} for fila in filas]


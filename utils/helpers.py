from sqlalchemy import create_engine, text

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

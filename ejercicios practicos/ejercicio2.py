import sqlite3


conn = sqlite3.connect('EESTN5.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
''')


alumnos_data = [
    ("Juan", 18),
    ("Ana", 17),
    ("Luis", 19),
    ("Maria", 20),
    ("Carlos", 16),
    ("Pedro", 18),
    ("Sofia", 21),
    ("Laura", 22)
]
cursor.executemany('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', alumnos_data)


cursor.execute('SELECT * FROM alumnos WHERE edad > 17')
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")


conn.commit()
conn.close()

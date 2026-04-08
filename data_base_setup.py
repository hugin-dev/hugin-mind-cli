import sqlite3

conexion = sqlite3.connect("hugin_mind.db")
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS notas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concepto TEXT NOT NULL,
            categoria TEXT,
            definicion TEXT,
            ejemplo TEXT
)
''')

conexion.commit()
conexion.close()
print("Base de datos y tabla creadas con éxito!")
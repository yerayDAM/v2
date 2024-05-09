import sqlite3
import os

def conectar_db():
    conexion = sqlite3.connect('C:\\Users\\yeray\\Desktop\\Repositorio13-04-24\\final\\db\\d.sqlite3')
    return conexion

# Crear conexión y cursor
conn = conectar_db()
cursor = conn.cursor()

# Crear tabla UltimasEjecuciones si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS UltimasEjecuciones (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Tipo TEXT CHECK (Tipo IN ('DireccionIP', 'Dominio', 'RutaEscaneo', 'URL')),
                    Valor TEXT
                )''')

# Crear el resto de tablas
cursor.execute('''CREATE TABLE IF NOT EXISTS InformacionDireccionesIP (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DireccionIP TEXT,
                    Informacion TEXT,
                    PuertosAbiertos TEXT,
                    FOREIGN KEY (DireccionIP) REFERENCES UltimasEjecuciones(Valor)
                        ON DELETE RESTRICT
                        ON UPDATE CASCADE
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS InformacionDominios (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Dominio TEXT,
                    rutaimagen TEXT,
                    SubdominiosEncontrados TEXT, 
                    FOREIGN KEY (Dominio) REFERENCES UltimasEjecuciones(Valor)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS InformacionEscaneoDirectorios (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DirectorioDominio TEXT,
                    ListaRutasUsadas TEXT,
                    FOREIGN KEY (DirectorioDominio) REFERENCES UltimasEjecuciones(Valor)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS InformacionWebCrawling (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    URL TEXT,
                    ListaEnlacesRutasEncontrados TEXT,
                    FOREIGN KEY (URL) REFERENCES UltimasEjecuciones(Valor)
                )''')                  

# Guardar los cambios
conn.commit()

# Ejecutar la consulta en la tabla UltimasEjecuciones
cursor.execute("SELECT * FROM UltimasEjecuciones")
resultado1 = cursor.fetchall()
print(resultado1)
print("\nÚltimas Ejecuciones:")
print(resultado1)

# Cerrar la conexión
conn.close()
print("La base de datos ha sido creada.")

import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    conexion = sqlite3.connect('C:\\Users\\yeray\\Desktop\\Repositorio13-04-24\\final\\db\\d.sqlite3')
    return conexion

# Función para cerrar la conexión a la base de datos
def cerrar_db(conexion):
    conexion.close()

# Función para consultar todos los registros de la tabla de Últimas Ejecuciones
def consultar_ultimas_ejecuciones(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM UltimasEjecuciones")
    resultados = cursor.fetchall()
    return resultados

# Función para consultar registros de la tabla de Últimas Ejecuciones filtrados por tipo
def consultar_ultimas_ejecuciones_por_tipo(conexion, tipo):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM UltimasEjecuciones WHERE Tipo = ?", (tipo,))
    resultados = cursor.fetchall()
    return resultados

# Ejemplo de uso:
conexion = conectar_db()

# Consultar todos los registros de la tabla de Últimas Ejecuciones
resultados_ultimas_ejecuciones = consultar_ultimas_ejecuciones(conexion)
print("Últimas Ejecuciones:")
for resultado in resultados_ultimas_ejecuciones:
    print(resultado)

# Consultar registros de la tabla de Últimas Ejecuciones filtrados por tipo
tipo_a_consultar = "DireccionIP"
resultados_ultimas_ejecuciones_tipo = consultar_ultimas_ejecuciones_por_tipo(conexion, tipo_a_consultar)
print(f"\nÚltimas Ejecuciones de tipo '{tipo_a_consultar}':")
for resultado in resultados_ultimas_ejecuciones_tipo:
    print(resultado)

cerrar_db(conexion)
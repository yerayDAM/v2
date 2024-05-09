import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    conexion = sqlite3.connect('.\\db\\d.sqlite3')
    return conexion

# Función para cerrar la conexión a la base de datos
def cerrar_db(conexion):
    conexion.close()

# Función para insertar datos en la tabla de Últimas Ejecuciones
def insertar_ultimas_ejecuciones(conexion, tipo, valor):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO UltimasEjecuciones (Tipo, Valor) VALUES (?, ?)", (tipo, valor))
    conexion.commit()

# Función para insertar datos en la tabla de Información de Direcciones IP
def insertar_informacion_direcciones_ip(conexion, direccion_ip, informacion, puertos_abiertos):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO InformacionDireccionesIP (DireccionIP, Informacion, PuertosAbiertos) VALUES (?, ?, ?)", (direccion_ip, informacion, puertos_abiertos))
    conexion.commit()

# Función para insertar datos en la tabla de Información de Dominios
def insertar_informacion_dominios(conexion, dominio, rutaimagen, subdominios_encontrados):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO InformacionDominios (Dominio, rutaimagen, SubdominiosEncontrados) VALUES (?, ?, ?)", (dominio, rutaimagen, subdominios_encontrados))
    conexion.commit()

# Función para insertar datos en la tabla de Información de Escaneo de Directorios
def insertar_informacion_escaneo_directorios(conexion, directorio_dominio, lista_rutas_usadas):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO InformacionEscaneoDirectorios (DirectorioDominio, ListaRutasUsadas) VALUES (?, ?)", (directorio_dominio, lista_rutas_usadas))
    conexion.commit()

# Función para insertar datos en la tabla de Información de Web Crawling
def insertar_informacion_web_crawling(conexion, url, lista_enlaces_rutas_encontrados):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO InformacionWebCrawling (URL, ListaEnlacesRutasEncontrados) VALUES (?, ?)", (url, lista_enlaces_rutas_encontrados))
    conexion.commit()

# Función para consultar todos los registros de la tabla de Últimas Ejecuciones
def consultar_ultimas_ejecuciones(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM UltimasEjecuciones")
    resultados = cursor.fetchall()
    return resultados

# Función para consultar todos los registros de la tabla de Información de Direcciones IP
def consultar_informacion_direcciones_ip(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM InformacionDireccionesIP")
    resultados = cursor.fetchall()
    return resultados

# Función para consultar todos los registros de la tabla de Información de Dominios
def consultar_informacion_dominios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM InformacionDominios")
    resultados = cursor.fetchall()
    return resultados

# Función para consultar todos los registros de la tabla de Información de Escaneo de Directorios
def consultar_informacion_escaneo_directorios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM InformacionEscaneoDirectorios")
    resultados = cursor.fetchall()
    return resultados

# Función para consultar todos los registros de la tabla de Información de Web Crawling
def consultar_informacion_web_crawling(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM InformacionWebCrawling")
    resultados = cursor.fetchall()
    return resultados

# Ejemplo de uso:
conexion = conectar_db()

# Insertar datos de Últimas Ejecuciones
#insertar_ultimas_ejecuciones(conexion, "DireccionIP", "92.166.143.123")
#insertar_ultimas_ejecuciones(conexion, "Dominio", "intelequia.com")

# Insertar datos de Información de Direcciones IP
#insertar_informacion_direcciones_ip(conexion, "2.166.143.5", "Información relevante", "80, 443")

# Consultar todos los registros de la tabla de Últimas Ejecuciones
#resultados_ultimas_ejecuciones = consultar_ultimas_ejecuciones(conexion)
#print("Últimas Ejecuciones:")
#for resultado in resultados_ultimas_ejecuciones:
#    print(resultado)

#resultados_ultimas_ejecuciones_ip = consultar_informacion_direcciones_ip(conexion)
#print("Últimas Ejecuciones ip:")
#for resultado in resultados_ultimas_ejecuciones_ip:
#    print(resultado)

#cerrar_db(conexion)

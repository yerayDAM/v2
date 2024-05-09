import requests
import re
import urllib3
from db.insertarDatos import conectar_db, cerrar_db, insertar_ultimas_ejecuciones, insertar_informacion_web_crawling#, consultar_informacion_web_crawling

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def generar_arbol_directorios(valores_unicos):
    arbol = {}  # Estructura de datos para el árbol de directorios
    for regex, valor in valores_unicos:
        partes = valor.split("/")
        nodo_actual = arbol
        for parte in partes:
            if parte not in nodo_actual:
                nodo_actual[parte] = {}
            nodo_actual = nodo_actual[parte]
    return arbol


def obtener_contenido_html(url):
    try:
        response = requests.get(url, verify=False)
        print(response.text)
# Advertencia: Desactiva la verificación SSL
        html_content = response.text
        if html_content:
            valores_unicos = set()
            regexes = [
                r"src=\"/([^\"]*)",
                r"href=\"/([^\"]*)",
                r"src=\"https://([^\"]*)",
                r"href=\"https://([^\"]*)",
                r"content=\"https://([^\"]*)",
                r"content=\"/([^\"]*)",
            ]
            for regex in regexes:
                pattern = re.compile(regex)
                matcher = pattern.finditer(html_content)
                for match in matcher:
                    valor_encontrado = match.group(1)
                    #print("----\n")
                    #plantear limpieza sobre el resultado de valor_enconttrado para coger el valor de match.group(0) y eliminar el href= o src= o content= es decir eliminar la primera parte de la regex.
                    #print(match.group(0))
                    valores_unicos.add((regex, valor_encontrado))
                    print(f"Resultado encontrado ({regex}):", valor_encontrado)
#        conexion = conectar_db()
#        insertar_ultimas_ejecuciones(conexion, "URL", url)
#        insertar_informacion_web_crawling(conexion, url, str(valores_unicos))
#        resultados_ultima_ejecucion_web_crawling = consultar_informacion_web_crawling(conexion)
#        print("Últimas Ejecuciones:")
#        for resultado in resultados_ultima_ejecucion_web_crawling:
#            print(resultado)
#        cerrar_db(conexion)
        return generar_arbol_directorios(valores_unicos)
    except requests.exceptions.RequestException as e:
        print("Error al obtener el contenido HTML:", e)
        return None
    finally:
        print("Recursos liberados (si es necesario)")


if __name__ == "__main__":
    url = "https://www.intelequia.com"
    html_content = obtener_contenido_html(url)
#    if html_content:
#        valores_unicos = set()
#        regexes = [
#            r"src=\"/([^\"]*)",
#            r"href=\"/([^\"]*)",
#            r"src=\"https://([^\"]*)",
#            r"href=\"https://([^\"]*)",
#            r"content=\"https://([^\"]*)",
#            r"content=\"/([^\"]*)",
#        ]
#        for regex in regexes:
#            pattern = re.compile(regex)
#            matcher = pattern.finditer(html_content)
#            for match in matcher:
#                valor_encontrado = match.group(1)
#                valores_unicos.add((regex, valor_encontrado))
#                print(f"Resultado encontrado ({regex}):", valor_encontrado)
#
#        arbol_directorios = generar_arbol_directorios(valores_unicos)
#        print("\nÁrbol de Directorios:")
#        print(arbol_directorios)

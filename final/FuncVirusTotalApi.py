import requests
#from db.insertarDatos import conectar_db, cerrar_db, insertar_ultimas_ejecuciones, insertar_informacion_direcciones_ip#, consultar_informacion_direcciones_ip
import os

def obtener_apikey():
    # Obtiene la ruta absoluta del archivo apikey-virustotal.txt en relación con este script
    ruta_archivo = os.path.join(os.path.dirname(__file__), 'apikey-virustotal.txt')
    # Lee el contenido del archivo
    with open(ruta_archivo, 'r') as archivo:
        apikey = archivo.read().strip()  # Lee el contenido y elimina cualquier espacio en blanco extra
    return apikey

def consultar_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    apikey = obtener_apikey()
    headers = {
        "x-apikey": apikey
    }

    response = requests.get(url, headers=headers, timeout=3)
    if response.status_code == 200:
        resultado = response.json()
        print(resultado)
        resultados = []
        if resultado:
            data = resultado.get('data', {})
            attributes = data.get('attributes', {})
            reputation_stats = data.get('attributes', {}).get('last_analysis_stats', {})
            common_name = None
            if 'last_https_certificate' in attributes:
                common_name = attributes['last_https_certificate'].get('subject', {}).get('CN')
            owner = data.get('attributes', {}).get('as_owner')
            network = data.get('attributes', {}).get('network')
            continent = data.get('attributes', {}).get('continent')
            country = data.get('attributes', {}).get('country')

            reputation_malicious = reputation_stats.get('malicious')
            reputation_suspicious = reputation_stats.get('suspicious')
            reputation_harmless = reputation_stats.get('harmless')

            resultado_fila = [ip, data.get('type'), owner, common_name, network, continent, country, reputation_malicious, reputation_suspicious, reputation_harmless]
            resultados.append(resultado_fila)
#            conexion = conectar_db()
#            insertar_ultimas_ejecuciones(conexion, "DireccionIP", ip)
#            insertar_informacion_direcciones_ip(conexion, ip, str(resultados),"")
#            resultados_ultimas_ejecuciones = consultar_informacion_direcciones_ip(conexion)
#            print("Últimas Ejecuciones:")
#            for resultado in resultados_ultimas_ejecuciones:
#                print(resultado)
#            cerrar_db(conexion)
            return resultados
    else:
        print(f"Error al consultar la IP {ip}. Código de estado: {response.status_code}")
        return None



#r = consultar_ip("81.4.72.170")

# Desempaquetar la lista y asignar cada valor a una variable
#ip, tipo, owner, common_name, network, continent, country, reputation_malicious, reputation_suspicious, reputation_harmless = r[0]

# Ahora cada variable contiene el valor correspondiente
#print("IP:", ip)
#print("Tipo:", tipo)
#print("Owner:", owner)
#print("Common Name:", common_name)
#print("Network:", network)
#print("Continent:", continent)
#print("Country:", country)
#print("Reputation (Malicious):", reputation_malicious)
#print("Reputation (Suspicious):", reputation_suspicious)
#print("Reputation (Harmless):", reputation_harmless)

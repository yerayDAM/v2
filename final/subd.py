import requests
import json
import re
import sys
import socket
from time import sleep
from db.insertarDatos import conectar_db, cerrar_db, insertar_ultimas_ejecuciones, insertar_informacion_dominios#, consultar_informacion_dominios
from dnsMapImage import obtener_info_imagen_dns_dumpster
from bs4 import BeautifulSoup


import urllib3
import warnings
urllib3.disable_warnings()
warnings.simplefilter("ignore")

# Subdomain discovery function
def subDomain(domain):

    print(f"\n[*] Discovering subdomains from {domain}...\n")
    sleep(0.1)
    subDoms = []

    # Consulting crt.sh
    try:
        r = requests.get(f"https://crt.sh/?q={domain}&output=json", timeout=20)
        file = json.dumps(json.loads(r.text), indent=4)
        sub_domains = sorted(set(re.findall(r'"common_name": "(.*?)"', file)))
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f" Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting Hackertarget
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=20)
        sub_domains = re.findall(f'(.*?),', r.text)
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f"Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting RapidDNS
    try:
        r = requests.get(f"https://rapiddns.io/subdomain/{domain}#result", timeout=20)
        sub_domains = re.findall(r'target="_blank".*?">(.*?)</a>', r.text)
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f"Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting AlienVault
    try:
        r = requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns", timeout=20)
        sub_domains = sorted(set(re.findall(r'"hostname": "(.*?)"', r.text)))
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f" Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting URLScan
    try:
        r = requests.get(f"https://urlscan.io/api/v1/search/?q={domain}", timeout=20)
        sub_domains = sorted(set(re.findall(r'https://(.*?).' + domain, r.text)))
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f" Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting Riddler
    try:
        r = requests.get(f"https://riddler.io/search/exportcsv?q=pld:{domain}", timeout=20)
        sub_domains = re.findall(r'\[.*?\]",.*?,(.*?),\[', r.text)
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f"Interrupt handler received, exiting...\n")
    except:
        pass

    # Consulting ThreatMiner
    try:
        r = requests.get(f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=5", timeout=20)
        file = json.loads(r.content)
        sub_domains = file['results']
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f"Interrupt handler received, exiting...\n")
    except:
        pass
        
    try:
        url = "https://dnsdumpster.com/"
        # Realiza la solicitud GET para obtener el token csrf
        response = requests.get(url)
        cookie = response.cookies["csrftoken"]
        print(cookie)
        soup = BeautifulSoup(response.content, "html.parser")

        # Encuentra el campo de entrada con nombre "csrfmiddlewaretoken"
        csrf_token_input = soup.find("input", {"name": "csrfmiddlewaretoken"})

        # Obtiene el valor del token
        csrf_token_value = csrf_token_input["value"]

        print("El valor del csrfmiddlewaretoken es: "+ csrf_token_value)

        # Datos que deseas enviar (reemplaza con tus propios datos)
        payload = {
            "csrfmiddlewaretoken": csrf_token_value,
            "targetip": domain,
            "user": "free"
        }

        # Encabezados de la solicitud
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "csrftoken=" + cookie + ";",
            "Referer": "https://dnsdumpster.com"
        }

        # Realiza la solicitud POST
        response = requests.post(url, data=payload, headers=headers)

        # Expresión regular para extraer la parte después de "?q="
        subDoms = re.compile(r'\?q=([^&"]+)', response.text)
        # Lista para almacenar los resultados filtrados
        for sub in sub_domains:
            if sub.endswith(domain) and sub not in subDoms:
                subDoms.append(sub)
    except KeyboardInterrupt:
        sys.exit(f"Interrupt handler received, exiting...\n")
    except:
        pass

#    conexion = conectar_db()
#    insertar_ultimas_ejecuciones(conexion, "Dominio", domain)
#    insertar_informacion_dominios(conexion, domain,"", str(subDoms))
#    resultados_ultimas_ejecuciones_dominios = consultar_informacion_dominios(conexion)
#    print("Últimas Ejecuciones:")
#    for resultado in resultados_ultimas_ejecuciones_dominios:
#        print(resultado)
#    cerrar_db(conexion)

    return subDoms

# Subdomain discovery get imagen from dns dumstep
def obtener_imagen_dns_dumpster(domain):
    ruta_imagen = obtener_info_imagen_dns_dumpster(domain)
    print(ruta_imagen)
    return ruta_imagen
#marca = "marca.com"
#subDomain(marca)
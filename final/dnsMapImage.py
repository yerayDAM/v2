import requests
from bs4 import BeautifulSoup
#import webCrawling
import shutil
import resizeImages
import os

def obtener_info_imagen_dns_dumpster(domain):
    url = "https://dnsdumpster.com/"
    urli = "https://dnsdumpster.com/static/map/"+domain+".png"
    # Realiza la solicitud GET para obtener el token csrf
    response = requests.get(url)
    cookie = response.cookies["csrftoken"]
    print(cookie)
    soup = BeautifulSoup(response.content, "html.parser")

    # Encuentra el campo de entrada con nombre "csrfmiddlewaretoken"
    csrf_token_input = soup.find("input", {"name": "csrfmiddlewaretoken"})

    # Obtiene el valor del token
    csrf_token_value = csrf_token_input["value"]

    print(f"El valor del csrfmiddlewaretoken es: {csrf_token_value}")

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
    #result = webCrawling.buscar_valor_recursivo_v2(response.text)

    filename = 'DnsDums\\{}.dnsmap.png'.format(domain)
    url = 'https://dnsdumpster.com/static/map/{}.png'.format(domain)
    print(url)
    # Verificar si el directorio existe, si no, crearlo
    directory = 'DnsDums'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    response1 = requests.get(url, stream=True)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(response1.raw, out_file)
    del response
    
    ruta_resize = resizeImages.resize_image(filename)

    # Imprime la respuesta (puedes adaptar esto según tus necesidades)
    # print(response.text)
    return ruta_resize

# Llamada a la función con el dominio deseado
#domain = "webtenerife.com"
#resultado = obtener_info_dns_dumpster(domain)
#print(resultado)

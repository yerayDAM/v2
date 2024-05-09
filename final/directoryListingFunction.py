import requests
from colorama import Fore, init
from db.insertarDatos import conectar_db, cerrar_db, insertar_ultimas_ejecuciones, insertar_informacion_escaneo_directorios#, consultar_informacion_escaneo_directorios


def check_wordlist_for_domain(domain, wordlist_path='./wordlist.txt'):
    """
    Checks a wordlist for domain availability using HTTP requests.

    Args:
        domain (str): The domain to check.
        wordlist_path (str, optional): Path to the wordlist file. Defaults to './wordlist.txt'.
    """
    init()  # Initialize colorama for consistent color output

    protocol = 'https://'
    headers = {'Content-Type': 'application/json'}
    available_elements = []

    try:
        with open(wordlist_path, "r") as file:
            for line in file:
                url = protocol + domain + "/" + line.strip()
                response = requests.get(url, headers=headers, timeout=3)
                code_response = str(response.status_code)
                available_elements.append((url,code_response))
                if 200 <= int(code_response) < 400:
                    print(Fore.GREEN + f"{line.strip()} - {code_response}")
                else:
                    print(Fore.RED + f"{line.strip()} - {code_response}")
#        conexion = conectar_db()
#        insertar_ultimas_ejecuciones(conexion, "RutaEscaneo", domain)
#        insertar_informacion_escaneo_directorios(conexion, domain, str(available_elements))
#        resultados_ultimas_ejecuciones = consultar_informacion_escaneo_directorios(conexion)
#        print("Últimas Ejecuciones:")
#        for resultado in resultados_ultimas_ejecuciones:
#            print(resultado)
#        cerrar_db(conexion)
        return available_elements

    except FileNotFoundError:
        print(Fore.RED + "Error: Wordlist file not found.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")


# Example usage:
#a=check_wordlist_for_domain("marca.com")
#print(a)

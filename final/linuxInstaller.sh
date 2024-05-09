#!/bin/bash

# Función para instalar curl si no está presente
install_curl() {
    if ! command -v curl &>/dev/null; then
        echo "Instalando curl..."
        if [[ "$(uname)" == "Darwin" ]]; then
            brew install curl
        elif [[ "$(uname -s)" == "Linux" ]]; then
            if [[ -f /etc/redhat-release ]]; then
                sudo yum install curl -y
            elif [[ -f /etc/debian_version ]]; then
                sudo apt-get update
                sudo apt-get install curl -y
            else
                echo "No se pudo determinar la distribución de Linux."
                exit 1
            fi
        else
            echo "No se pudo determinar el sistema operativo."
            exit 1
        fi
    fi
}

# Función para instalar wine si no está presente
install_wine() {
    if ! command -v wine &>/dev/null; then
        echo "Instalando wine..."
        if [[ "$(uname)" == "Darwin" ]]; then
            echo "Wine no es compatible con macOS."
            exit 1
        elif [[ "$(uname -s)" == "Linux" ]]; then
            if [[ -f /etc/redhat-release ]]; then
                sudo yum install wine -y
            elif [[ -f /etc/debian_version ]]; then
                sudo apt-get update
                sudo apt-get install wine -y
            else
                echo "No se pudo determinar la distribución de Linux."
                exit 1
            fi
        else
            echo "No se pudo determinar el sistema operativo."
            exit 1
        fi
    fi
}

# Instalar curl y wine si no están presentes
install_curl
install_wine

# Comprobando si Python ya está instalado
if command -v python &>/dev/null; then
    echo "Python ya está instalado."
else
    echo "Descargando Python 3..."
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe

    echo "Instalando Python 3..."
    python python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

    # Limpiando
    rm python-installer.exe
fi

# Añadiendo Python al PATH si no está presente
if ! command -v python &>/dev/null; then
    echo "Añadiendo Python al PATH..."
    echo 'export PATH="$PATH:/usr/local/bin/python3"' >> ~/.bashrc
    source ~/.bashrc
fi

# Comprobando si Nmap ya está instalado
if command -v nmap &>/dev/null; then
    echo "Nmap ya está instalado."
else
    echo "Descargando Nmap..."
    curl -o nmap-installer.exe https://nmap.org/dist/nmap-7.91-setup.exe

    echo "Instalando Nmap..."
    wine nmap-installer.exe /S

    # Limpiando
    rm nmap-installer.exe
fi

# Añadiendo Nmap al PATH si no está presente
if ! command -v nmap &>/dev/null; then
    echo "Añadiendo Nmap al PATH..."
    echo 'export PATH="$PATH:/usr/bin/nmap"' >> ~/.bashrc
    source ~/.bashrc
fi

# Instalando paquetes de Python desde requirements.txt si está presente
if [ -f requirements.txt ]; then
    echo "Instalando paquetes de Python desde requirements.txt..."
    pip install -r requirements.txt
fi

echo "Instalación completada."
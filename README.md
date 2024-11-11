#Script de Integración para Ciberseguridad

####Este proyecto en Python permite ejecutar scripts de Bash, PowerShell y Python para realizar diversas tareas relacionadas con ciberseguridad. El objetivo es proporcionar una interfaz centralizada para ejecutar análisis de red, detección de malware y más, utilizando diferentes lenguajes y herramientas.

##Requisitos

Python 3.x
PowerShell (para ejecutar los scripts de PowerShell)
Bash (para ejecutar los scripts de Bash)
Librerías adicionales de Python (dependiendo de los scripts adicionales)
Instalación

###Clona el repositorio:

git clone <repositorio>
cd <directorio>

###Asegúrate de tener permisos de ejecución para los scripts de Bash:

chmod +x bash/*.sh

###Para los scripts de PowerShell, permite la ejecución:

powershell
Copiar código
Set-ExecutionPolicy Bypass -Scope Process

##Uso

El script principal se ejecuta con Python e incluye varias opciones para ejecutar scripts específicos. Usa el siguiente comando para ver la ayuda:

python main.py --help

##Opciones Disponibles

###Bash

--monitoreo: Inicia el monitoreo del ancho de banda de la red.
--trafico: Registra el tráfico de red.
--escaneo: Detecta dispositivos conectados en la red.
--rendimiento: Analiza el rendimiento de la red.

###PowerShell

--hashes: Genera y analiza hashes.
--oculto <ruta>: Busca archivos ocultos en la ruta especificada.
--recursos: Registra los recursos del sistema utilizados.
--proceso: Busca los procesos con más uso de recursos.

###Python

--password <longitud>: Genera una contraseña con la longitud especificada.
--ipshodan <APIKEY> <IP>: Escanea información de una IP usando la API de Shodan.
--malware <ruta>: Escanea un directorio en busca de malware.
--abuse <APIKEY> <opción> <valor>: Analiza si una IP o dominio tiene reportes maliciosos usando la API de Abuse. Uso:
opción: 1 para IP, 2 para dominio.
--red <número>: Monitorea el tráfico de red en tiempo real, indicando el número de líneas a registrar.

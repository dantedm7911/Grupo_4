#!/bin/bash
# Instalar los comandos tcpdump y nmap antes de usar
trafico_red() {
    # Verificar si tcpdump está instalado
    if ! command -v tcpdump &> /dev/null
    then
        echo "tcpdump no está instalado. Por favor, instálalo para capturar tráfico de red."
        exit 1
    fi

    # Verificar si nmap está instalado
    if ! command -v nmap &> /dev/null
    then
        echo "nmap no está instalado. Por favor, instálalo para detectar dispositivos en la red."
        exit 1
    fi

    # Detectar la interfaz de red activa
    INTERFAZ=$(ip route | grep default | awk '{print $5}')

    # Si no se detecta ninguna interfaz
    if [ -z "$INTERFAZ" ]; then
        echo "No se ha podido detectar una interfaz de red activa."
        exit 1
    fi

    # Definir el archivo de reporte
    REPORTE="reporte_trafico_red_$(date +%Y-%m-%d).log"

    # Escribir encabezado en el reporte
    echo "=== Reporte de Tráfico de Red - $(date) ===" > $REPORTE

    # Capturar tráfico de red local (sin privilegios de root, puede no funcionar en algunas interfaces)
    echo "Captura de tráfico de red local (primeros 10 paquetes en $INTERFAZ):" | tee -a $REPORTE
    tcpdump -i $INTERFAZ -c 10 2>/dev/null | tee -a $REPORTE
    echo "" | tee -a $REPORTE

    # Detectar dispositivos en la red local
    echo "Dispositivos en la red local (192.168.1.0/24):" | tee -a $REPORTE
    nmap -sn 192.168.1.0/24 --host-timeout 5s | tee -a $REPORTE
    echo "" | tee -a $REPORTE

    # Analizar rendimiento de la red local (ping al router)
    echo "Análisis de rendimiento de red local (ping al router 192.168.1.1):" | tee -a $REPORTE
    ping -c 4 192.168.1.1 | tee -a $REPORTE
    echo "" | tee -a $REPORTE

    # Mensaje final
    echo "Reporte de tráfico de red generado en $REPORTE"
}

trafico_red

#!/bin/bash

monitoreo(){
# A ver si tienes ifstat instalado, si no, pues lo bajamos
if ! command -v ifstat &> /dev/null
then
    echo "ifstat no esta instalado en el dispositivo. INSTALANDO..."
    sudo apt-get install ifstat -y
fi

# Define la interfaz de red (cambia esto si es diferente en tu compu)
INTERFACE="eth0"

# Tiempo de monitoreo (en segundos)
TIME=5

#Nombre reporte
REPORTE="reporte_red.txt"

echo "Reporte generado el $(date)" > "$REPORTE"
ifstat -i "$INTERFACE" 1 "$TIME" >> "$REPORTE"
echo "Reporte guardado en $REPORTE"

}

monitoreo

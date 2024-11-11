#!/bin/bash

escaneo(){
    
# Inicializa una lista para los hosts activos
hosts_activos=()

#Reporte
REPORTE="reporte_escaneo_red.txt"

#Mostrar informacion sobre el archivo

echo "Feche y hora: $(date)" >> "REPORTE"
echo "------------------------------------------" >> "$REPORTE"


# Bucle para escanear los hosts
for i in {1..255}; do
    if timeout 2 ping -c 1 192.168.56.$i >/dev/null 2>&1; then
        echo "El host 192.168.56.$i está activo"
        # Agrega el host a la lista de hosts activos
        hosts_activos+=("192.168.56.$i")
    fi
done

    #Guardar la lista en el REPORTE
    echo -e "\nDispositivos conectados a la red local:" >> "$REPORTE"
    for host in "${hosts_activos[@]}"; do
        echo "$host" >> "REPORTE"
    done

    echo "Reporte almacenado en $REPORTE"
 
 
 }
escaneo

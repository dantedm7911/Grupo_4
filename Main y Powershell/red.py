from scapy.all import sniff

def analizar_trafico_red_y_guardar():
    results = []
    
    while True:
        try:
            # Define la cantidad de paquetes a capturar
            packet_count = int(input("¿Cuántas líneas de tráfico deseas imprimir? "))
            if packet_count <= 0:
                print("Por favor, introduce un número positivo.")
                continue  # Volver a preguntar si el número es negativo o cero
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    def packet_callback(packet):
        results.append(f"Origen: {packet[0][1].src} -> Destino: {packet[0][1].dst}")  # Agrega un resumen del paquete a los resultados
        if len(results) >= packet_count:
            return False  # Detiene la captura después de alcanzar el número deseado

    sniff(prn=packet_callback, count=packet_count)
    
    # Imprimir y devolver los resultados
    if results:
        print("\nResultados del análisis de tráfico de red:")
        for result in results:
            print(result)  # Imprime el resultado para el usuario

        # Guardar los resultados en un archivo txt
        with open("trafico_red_output.txt", "a") as archivo:
            archivo.write("\nResultados del análisis de tráfico de red:\n")
            for result in results:
                archivo.write(f"{result}\n")
        print("Resultados guardados en 'trafico_red_output.txt'")
    else:
        print("No se capturaron paquetes.")

# Llamar a la función para ejecutarla
analizar_trafico_red_y_guardar()

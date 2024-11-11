from scapy.all import sniff
import argparse

def analizar_trafico_red_y_guardar(packet_count):
    results = []
    
    def packet_callback(packet):
        results.append(f"Origen: {packet[0][1].src} -> Destino: {packet[0][1].dst}")  # Agrega un resumen del paquete a los resultados
        if len(results) >= packet_count:
            return False  # Detiene la captura después de alcanzar el número deseado

    sniff(prn=packet_callback, count=packet_count)
    
    # Imprimir y devolver los resultados
    if results:
        print("\Resultados generados")  

        # Guardar los resultados en un archivo txt
        with open("trafico_red_output.txt", "a") as archivo:
            archivo.write("\nResultados del análisis de tráfico de red:\n")
            for result in results:
                archivo.write(f"{result}\n")
        print("Resultados guardados en 'trafico_red_output.txt'")
    else:
        print("No se capturaron paquetes.")

def main():
    # Configurar argparse para recibir la cantidad de paquetes como argumento
    parser = argparse.ArgumentParser(description="Analizar el tráfico de red y guardar los resultados.")
    parser.add_argument("packet_count", type=int, help="Número de paquetes a capturar.")
    
    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con el argumento proporcionado
    analizar_trafico_red_y_guardar(args.packet_count)

if __name__ == "__main__":
    main()

from shodan import Shodan
import argparse

def obtener_info_y_guardar(api_key, ip):
    try:
        # Conectarse a la API de Shodan usando la API Key proporcionada
        api = Shodan(api_key)

        # Obtener la información de la IP
        info_ip = api.host(ip)

        # Formatear los resultados
        result = (
            f'Información de la IP {ip}:\n'
            f'Organización: {info_ip.get("org", "No disponible")}\n'
            f'Sistema operativo: {info_ip.get("os", "No disponible")}\n'
            f'Puertos abiertos: {info_ip.get("ports", "No disponible")}\n'
            f'Ubicación: {info_ip.get("country_name", "No disponible")}, {info_ip.get("city", "No disponible")}\n'
        )

        # Guardar la información en un archivo txt
        with open("info_ip.txt", "a") as archivo:
            archivo.write(f"{result}\n")
        print("Información guardada en 'info_ip.txt'")

    except Exception as e:
        print(f'Ocurrió un error al querer obtener información: {e}')

def main():
    # Configurar argparse para recibir la API Key y la IP como argumentos
    parser = argparse.ArgumentParser(description="Analizar IP usando la API de Shodan.")
    parser.add_argument("apikey", help="API Key de Shodan")
    parser.add_argument("ip", help="Dirección IP a analizar")

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con los argumentos proporcionados
    obtener_info_y_guardar(args.apikey, args.ip)

if __name__ == "__main__":
    main()

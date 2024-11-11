from shodan import Shodan

def obtener_info_y_guardar():
    try:
        # Solicitar la API Key y la IP al usuario
        api_key = input("Introduce tu API Key de Shodan: ")
        ip = input("Introduce la dirección IP para obtener información: ")

        # Conectarse a la API de Shodan usando nuestra API Key
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

        # Mostrar el resultado en consola
        print(result)
        
        # Guardar la información en un archivo txt
        with open("info_ip.txt", "a") as archivo:
            archivo.write(f"{result}\n")
        print("Información guardada en 'info_ip.txt'")

    except Exception as e:
        print(f'Ocurrió un error al querer obtener información: {e}')

# Llamar a la función para ejecutarla
obtener_info_y_guardar()

import requests
import subprocess
import os
from datetime import date
from datetime import datetime

def AbuseIP():
    
    API_KEY = input("Ingresa tu API KEY: ")  # Ingresa tu API KEY 

    while True:  
        print("1. Hacer el análisis en base a una IP")
        print("2. Hacer el análisis a partir de un dominio al que quieras analizar")
        print("3. Salir")

        op = int(input("Ingresa la opción deseada: "))

        if op == 1:
            ip_address = input("Ingresa la dirección IP que quieras analizar: ")

            url = 'https://api.abuseipdb.com/api/v2/check'
            params = {
                'ipAddress': ip_address,
                'maxAgeInDays': 90
            }
            headers = {
                'Accept': 'application/json',
                'Key': API_KEY
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                print("\nInformación sobre la IP:")
                print(f"Dirección IP: {data['data']['ipAddress']}")
                print(f"País: {data['data']['countryCode']}")
                print(f"Reportes: {data['data']['totalReports']}")
                print(f"Última actividad maliciosa: {data['data']['lastReportedAt']}")
                print(f"Score de abuso: {data['data']['abuseConfidenceScore']}")

                try:
                    if not os.path.exists("Reportes_de_Consulta_API"):
                        os.makedirs("Reportes_de_Consulta_API")

                    with open("Reportes_de_Consulta_API/Abuse_API.txt", "a") as file:
                        file.write("== Reporte de Análisis de IP ==\n")
                        file.write(f"Dirección IP: {data['data']['ipAddress']}\n")
                        file.write(f"País: {data['data']['countryCode']}\n")
                        file.write(f"Reportes: {data['data']['totalReports']}\n")
                        file.write(f"Última actividad maliciosa: {data['data']['lastReportedAt']}\n")
                        file.write(f"Score de abuso: {data['data']['abuseConfidenceScore']}\n")
                        file.write(f"Fecha: {date.today()} Hora: {datetime.now().strftime('%H:%M:%S')} \n")
                        file.write("================================\n\n")
                except Exception as e:
                    print(f"Error al escribir el reporte: {e}")

            else:
                print(f"Error en la solicitud: {response.status_code}")
                print(response.text)

        elif op == 2:
            url_method = input("Ingresa el dominio que quieras analizar: ")

            result = subprocess.run(
                ["powershell", "-Command", f"[System.Net.Dns]::GetHostAddresses('{url_method}') | ForEach-Object {{ $_.IPAddressToString }}"],
                capture_output=True,
                text=True
            )

            ip_address = result.stdout.strip()
            if ip_address:
                print(f"\nDirección IP obtenida para el dominio {url_method}: {ip_address}")

                url = 'https://api.abuseipdb.com/api/v2/check'
                params = {
                    'ipAddress': ip_address,
                    'maxAgeInDays': 90
                }
                headers = {
                    'Accept': 'application/json',
                    'Key': API_KEY
                }

                response = requests.get(url, headers=headers, params=params)

                if response.status_code == 200:
                    data = response.json()
                    print("\nInformación sobre la IP:")
                    print(f"Dirección IP: {data['data']['ipAddress']}")
                    print(f"País: {data['data']['countryCode']}")
                    print(f"Reportes: {data['data']['totalReports']}")
                    print(f"Última actividad maliciosa: {data['data']['lastReportedAt']}")
                    print(f"Score de abuso: {data['data']['abuseConfidenceScore']}")

                    try:
                        if not os.path.exists("Reportes_de_Consulta_API"):
                            os.makedirs("Reportes_de_Consulta_API")

                        # Guardar el reporte del análisis de dominio en un archivo separado
                        with open("Reportes_de_Consulta_API/Abuse_Dominio.txt", "a") as file:
                            file.write("== Reporte de Análisis de Dominio ==\n")
                            file.write(f"Dominio: {url_method}\n")
                            file.write(f"Dirección IP obtenida: {ip_address}\n")
                            file.write(f"País: {data['data']['countryCode']}\n")
                            file.write(f"Reportes: {data['data']['totalReports']}\n")
                            file.write(f"Última actividad maliciosa: {data['data']['lastReportedAt']}\n")
                            file.write(f"Score de abuso: {data['data']['abuseConfidenceScore']}\n")
                            file.write(f"Fecha: {date.today()} Hora: {datetime.now().strftime('%H:%M:%S')}\n")
                            file.write("================================\n\n")
                    except Exception as e:
                        print(f"Error al escribir el reporte: {e}")
                else:
                    print(f"Error en la solicitud: {response.status_code}")
                    print(response.text)
            else:
                print("No se pudo obtener la dirección IP del dominio especificado.")

        elif op == 3:
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

AbuseIP()




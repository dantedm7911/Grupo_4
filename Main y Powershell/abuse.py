import requests
import subprocess
import os
import argparse
from datetime import date, datetime

def analizar_ip(api_key, ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': 90
    }
    headers = {
        'Accept': 'application/json',
        'Key': api_key
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

def analizar_dominio(api_key, dominio):
    result = subprocess.run(
        ["powershell", "-Command", f"[System.Net.Dns]::GetHostAddresses('{dominio}') | ForEach-Object {{ $_.IPAddressToString }}"],
        capture_output=True,
        text=True
    )

    ip_address = result.stdout.strip()
    if ip_address:
        print(f"\nDirección IP obtenida para el dominio {dominio}: {ip_address}")
        analizar_ip(api_key, ip_address)
    else:
        print("No se pudo obtener la dirección IP del dominio especificado.")

def main():
    parser = argparse.ArgumentParser(description="Analizar IP o dominio usando AbuseIPDB API.")
    parser.add_argument("api_key", type=str, help="Tu API key para AbuseIPDB.")
    parser.add_argument("opcion", type=int, choices=[1, 2], help="Opción de análisis: 1 para IP, 2 para dominio.")
    parser.add_argument("valor", type=str, help="IP o dominio a analizar.")

    args = parser.parse_args()

    if args.opcion == 1:
        analizar_ip(args.api_key, args.valor)
    elif args.opcion == 2:
        analizar_dominio(args.api_key, args.valor)

if __name__ == "__main__":
    main()




import argparse
import subprocess

# Función para ejecutar los scripts de Bash correspondientes
def ejecutar_comando(bash_comando):   #AGREGAR PARAMETROS DE CADA OPCION? 
    try:
        subprocess.run(bash_comando, shell=True, check=True)    
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")

# Función para ejecutar los scripts de PowerShell
def ejecutar_comando_powershell(ps_comando, ruta=None):
    try:
        # Si se pasa una ruta, se agrega al comando
        if ruta:
            subprocess.run(["powershell", "-ExecutionPolicy", "ByPass", "-file", ps_comando, "-path", ruta], check=True)
        else:
            subprocess.run(["powershell", "-ExecutionPolicy", "ByPass", "-file", ps_comando], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando de PowerShell: {e}")

# Función para ejecutar los scripts de Python con argumentos
def ejecutar_comando_python(py_comando, *args):
    try:
        # Construir el comando incluyendo los argumentos
        comando = ["python", py_comando] + list(args)
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando de Python: {e}")



def main():
    parser = argparse.ArgumentParser(description="Scripts en Powerhsell, Bash y Python de analisis de ciberseguridad. Ejemplo de entrada: python main.py --argumento *parametros*") 
    
    # Argumentos para bash
    parser.add_argument("--monitoreo", action="store_true", help="Iniciar monitoreo de ancho de banda.")
    parser.add_argument("--trafico", action="store_true", help="Registrar tráfico de red.")
    parser.add_argument("--escaneo", action="store_true", help="Detectar dispositivos en la red.")
    parser.add_argument("--rendimiento", action="store_true", help="Analizar rendimiento de la red.")


    # Argumentos para PowerShell
    parser.add_argument("--hashes", action="store_true", help="Crea hashes y los analiza.")
    parser.add_argument("--oculto", type=str, help="Busca archivos ocultos en la ruta especificada.")
    parser.add_argument("--recursos", action="store_true", help="Registra los recursos del sistema usados.")
    parser.add_argument("--proceso", action="store_true", help="Busca los procesos con mas recursos usados.")

    # Argumentos para Python      
    parser.add_argument("--password", type=int, metavar="LONGITUD", help="Genera una contraseña de la longitud especificada")
    parser.add_argument("--ipshodan", nargs=2, metavar=("APIKEY", "IP"), help="Escanea informacion de una IP mediante Api shodan Con parametros APIKEY e IP.")
    parser.add_argument("--malware", type=str, metavar="DIRECTORY_PATH", help="Escanea un directorio en busca de malware.")
    parser.add_argument("--abuse", nargs=3, metavar=("APIKEY", "OPCION", "VALOR"), help="Analiza si una IP tiene reportes maliciosos mediante Api Abuse. Uso: --abuse APIKEY OPCION(1=IP, 2=DOMINIO) VALOR")
    parser.add_argument("--red", type=int, metavar="PACKET_COUNT", help="Permite monitorear en Tiempo Real el trafico de tu red proporcionando el numero de lienas a guardar.")
    
    args = parser.parse_args()
    
    # Verificar las opciones seleccionadas
    if args.monitoreo:
        print("Ejecutando monitoreo de ancho de banda...")
        ejecutar_comando("bash bash/monitoreo.sh")
    
    if args.trafico:
        print("Registrando tráfico de red...")
        ejecutar_comando("bash bash/trafico_red.sh")
    
    if args.escaneo:
        print("Detectando dispositivos en la red...")
        ejecutar_comando("bash bash/escaneo.sh")
    
    if args.rendimiento:
        print("Analizando rendimiento de la red...")
        ejecutar_comando("bash bash/rendimiento.sh")

    # Verificar las opciones seleccionadas para PowerShell
    if args.hashes:
        print("Analizando hashes...")
        ejecutar_comando_powershell("powershell/API_VIRUSTOTAL_2.ps1")
    
    if args.oculto:
        print(f"Buscando archivos ocultos en {args.oculto}...")
        ejecutar_comando_powershell("powershell/BuscarArchivosOcultos.ps1", args.oculto)

    
    if args.recursos:
        print("Registrando recursos...")
        ejecutar_comando_powershell("powershell/Recursos.ps1")
    
    if args.proceso:
        print("Detectando procesos...")
        ejecutar_comando_powershell("powershell/TopProcess.ps1")   

    # Verificar las opciones seleccionadas para Python  
    if args.password:
        longitud = args.password
        print("Generando contraseña...")
        ejecutar_comando_python("python/password.py", str(longitud))
    
    if args.ipshodan:
        apikey, ip =args.ipshodan
        print("Escaneando IP con shodan...")
        ejecutar_comando_python("python/ipshodan.py", apikey, ip)
    
    if args.malware:
        directory_path = args.malware
        print("Escaneando malware...")
        ejecutar_comando_python("python/malware.py", directory_path)
    
    if args.abuse:
        api_key, opcion, valor = args.abuse
        print("Verificando reportes de IP...")
        ejecutar_comando_python("python/abuse.py", api_key, opcion, valor)

    if args.red:
        packet_count = args.red
        print("Verificando trafico de red en tiempo real...")
        ejecutar_comando_python("python/red.py", str(packet_count))
        
    
   # Mensaje de error si no se seleccionó ninguna opción 
    if not (args.monitoreo or args.trafico or args.escaneo or args.rendimiento or 
            args.hashes or args.oculto or args.recursos or args.proceso or 
            args.password or args.ipshodan or args.malware or args.abuse or args.red):
        print("Error: No se seleccionó ninguna opción válida. Usa --help para más detalles.")

if __name__ == "__main__":
    main()


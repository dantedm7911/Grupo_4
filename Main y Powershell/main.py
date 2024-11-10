import argparse
import subprocess

# Función para ejecutar los scripts de Bash correspondientes
def ejecutar_comando(bash_comando):
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

# Función para ejecutar los scripts de Python
def ejecutar_comando_python(py_comando):
    try:
        subprocess.run(["python", py_comando], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando de Python: {e}")


def main():
    parser = argparse.ArgumentParser(description="Scripts en Powerhsell, Bash y Python de analisis de ciberseguridad.") 
    
    # Argumentos
    parser.add_argument("--monitoreo", action="store_true", help="Iniciar monitoreo de ancho de banda.")
    parser.add_argument("--trafico", action="store_true", help="Registrar tráfico de red.")
    parser.add_argument("--escaneo", action="store_true", help="Detectar dispositivos en la red.")
    parser.add_argument("--rendimiento", action="store_true", help="Analizar rendimiento de la red.")


    # Argumentos para PowerShell
    parser.add_argument("--hashes", action="store_true", help="Crea hashes y los analiza.")
    parser.add_argument("--oculto", type=str, help="Busca archivos ocultos en la ruta especificada.")
    parser.add_argument("--recursos", action="store_true", help="Registra los recursos del sistema usados.")
    parser.add_argument("--proceso", action="store_true", help="Busca los procesos con mas recursos usados.")

    args = parser.parse_args()
    
    # Verificar las opciones seleccionadas
    if args.monitoreo:
        print("Ejecutando monitoreo de ancho de banda...")
        ejecutar_comando("bash monitoreo.sh")
    
    if args.trafico:
        print("Registrando tráfico de red...")
        ejecutar_comando("bash trafico_red.sh")
    
    if args.escaneo:
        print("Detectando dispositivos en la red...")
        ejecutar_comando("bash escaneo.sh")
    
    if args.rendimiento:
        print("Analizando rendimiento de la red...")
        ejecutar_comando("bash rendimiento.sh")

    # Verificar las opciones seleccionadas para PowerShell
    if args.hashes:
        print("Analizando hashes...")
        ejecutar_comando_powershell(".\\API_VIRUSTOTAL_2.ps1")
    
    if args.oculto:
        print(f"Buscando archivos ocultos en {args.oculto}...")
        ejecutar_comando_powershell(".\\BuscarArchivosOcultos.ps1", args.oculto)

    
    if args.recursos:
        print("Registrando recursos...")
        ejecutar_comando_powershell(".\\Recursos.ps1")
    
    if args.proceso:
        print("Detectando procesos...")
        ejecutar_comando_powershell(".\\TopProcess.ps1")   
    
    if not (args.monitoreo or args.trafico or args.escaneo or args.rendimiento or args.hashes or args.oculto or args.recursos or args.proceso ):  #AGREGAR LAS DE PY
        print("Error: No se seleccionó ninguna opción válida. Usa --help para más detalles.")

if __name__ == "__main__":
    main()


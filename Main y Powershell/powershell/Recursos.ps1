#JOSAFAT DE LA GARZA AMARO 2076405
#CODIGO PARA VER EL USO DE LA CPU Y LA RAM Y DISCO DURO 

<#
.SYNOPSIS
Muestra el uso actual de los recursos del sistema, incluyendo CPU, memoria y espacio en disco.

.DESCRIPTION
La función `Get-ResourceUsage` obtiene y muestra información sobre el uso de recursos del sistema, como el porcentaje de tiempo de procesador, la memoria disponible en megabytes y el porcentaje de espacio libre en disco. La información se actualiza cada 2 segundos y se muestra en formato de texto.

.EXAMPLE
Get-ResourceUsage
Muestra el uso de recursos del sistema en la consola cada 2 segundos.

.PARAMETER
Este script no acepta parámetros.

.NOTES
- La función utiliza `Get-Counter` para obtener los contadores de rendimiento del sistema.
- La función maneja errores y muestra mensajes en caso de problemas al obtener los datos.
- La actualización de los datos de recursos se realiza cada 2 segundos.
- Para salir del bucle de los 2 segundos presionar ´ctrl+c´
- Autor: Josafat De La Garza (User: josa3) 
- Fecha: 18/09/2024
#>

function Get-ResourceUsage {
    Set-StrictMode -Version Latest
    try {
        $totalRam = (Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property capacity -Sum).Sum
        if (-not $totalRam) {
            throw "No se pudo obtener la informacion de la memoria fisica"
        }
    } catch {
        Write-Error "Error al obtener la memoria fisica: $_"
        return
    }
    
    $counter = 0  # Contador de iteraciones
    $fileName = "$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').txt"  # Nombre del archivo con fecha y hora actuales
    $filePath = Join-Path -Path $PWD -ChildPath $fileName  # Ruta completa del archivo

    while ($counter -lt 5) {  # Solo se ejecuta 5 veces
        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        
        try {
            # Obtener el uso de recursos
            $cpuTime = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue
            $availMem = (Get-Counter '\Memory\Available MBytes').CounterSamples.CookedValue
            $diskFree = (Get-Counter '\LogicalDisk(_Total)\% Free Space').CounterSamples.CookedValue

            if (-not $cpuTime -or -not $availMem -or -not $diskFree) {
                throw "No se pudieron obtener los contadores de recursos"
            }
        } catch { 
            Write-Error "Error al obtener los contadores de recursos: $_"
            Start-Sleep -s 2
            continue
        }
        
        # Generar la salida
        try {
            $output = "$date > CPU: {0}%, Avail. RAM.: {1}MB ({2}%), Disco Libre: {3}%" -f `
                $cpuTime.ToString("#,0.000"), `
                $availMem.ToString("N0"), `
                (104857600 * $availMem / $totalRam).ToString("#,0.0"), `
                $diskFree.ToString("#,0.0")
            
            # Guardar la salida en el archivo
            Add-Content -Path $filePath -Value $output
        } catch { 
            Write-Error "Error al formatear la salida: $_"
        }
        
        $counter++  # Incrementar el contador
        Start-Sleep -s 2
    }

    # Mensaje indicando dónde se guardó el archivo
    Write-Host "Los datos de uso de recursos se guardaron en: $filePath"
}

Get-ResourceUsage

#CODIGO PARA VER EL USO DE LA CPU Y LA RAM Y DISCO DURO 

<#
.SYNOPSIS
Muestra los procesos que est�n utilizando m�s memoria.

.DESCRIPTION
La funci�n `TopProcess` obtiene la lista de todos los procesos en ejecuci�n, los ordena por el uso de memoria (Working Set) y selecciona los procesos que est�n utilizando m�s memoria.

.EXAMPLE
TopProcess -Count 5
Muestra los 5 procesos que est�n utilizando m�s memoria en el sistema.

.NOTES
 -La funci�n utiliza el cmdlet `Get-Process` para obtener los procesos que se estan ejecutando
 -Ordena los procesos por la memoria f�sica utilizada (`WS` o Working Set)
 -Selecciona los procesos con mayor uso de memoria.
 -Autor: Jonathan Francisco Vela Guerrero
 -Fecha: 18/09/2024
 #>

Set-StrictMode -Version Latest #Activa el modo estricto en su version mas reciente

function TopProcess {
    try {
        # Obtener los 5 procesos con mayor uso de memoria y guardarlos en una variable
        $topProcesses = ps | Sort-Object -Property WS | Select-Object -Last 5 -ErrorAction "Stop"

        # Crear el nombre del archivo con la fecha y hora actuales
        $fileName = "$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').txt"
        $filePath = Join-Path -Path $PWD -ChildPath $fileName

        # Guardar la informaci�n en el archivo de texto
        $topProcesses | Out-File -FilePath $filePath -Encoding UTF8

        # Mensaje indicando d�nde se guard� el archivo
        Write-Host "La informaci�n de los procesos se guard� en: $filePath"
    }
    catch {
        Write-Host "Ocurri� un error:" $_.Exception.Message
    }
}

TopProcess

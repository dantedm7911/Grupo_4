<#
.SYNOPSIS
   Muestra los archivos ocultos en una ruta especificada.
.DESCRIPTION
   La funcion recibe una ruta ingresada por el usuario y muestra todos los archivos ocultos en esa ruta.
.PARAMETER None
   La función no recibe parametros, pero solicita al usuario que ingrese una ruta.
.NOTES
   Autor: TeyssiHM
   Fecha: 12/09/2024
#>

function Get-HiddenFiles {
    Set-StrictMode -Version Latest
    
    # Pedir la ruta al usuario
    $path = Read-Host "Enter the path to your folder to see hidden files"

    # Crear el nombre del archivo con la fecha y hora actuales
    $fileName = "$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').txt"
    $filePath = Join-Path -Path $PWD -ChildPath $fileName

    if (Test-Path -Path $path) {
        try {
            # Obtener archivos ocultos
            $hiddenFiles = Get-ChildItem -Path $path -Force -Hidden -File -ErrorAction Stop

            # Crear una lista para almacenar los resultados
            $outputList = @()

            # Verificar si se encontraron archivos ocultos
            if (-not $hiddenFiles) {
                $outputList += "No hidden files found in ${path}."
            } else {
                $outputList += "Hidden files found in ${path}:"
                $count = 1
                foreach ($file in $hiddenFiles) {
                    $outputList += "$count. $($file.Name)"
                    $count++
                }

                $outputList += "Total number of hidden files: $($hiddenFiles.Length)"
            }

            # Guardar toda la lista en el archivo
            $outputList | Out-File -FilePath $filePath -Encoding UTF8
        } catch {
            # Guardar mensaje de error en el archivo
            "Error: $($_.Exception.Message)" | Out-File -FilePath $filePath -Encoding UTF8
        }
    } else {
        # Guardar mensaje si la ruta no es válida
        "The specified path does not exist. Please enter a valid path." | Out-File -FilePath $filePath -Encoding UTF8
    }

    # Mostrar mensaje indicando dónde se guardó el archivo
    Write-Host "La información de archivos ocultos se guardó en: $filePath"
}

# Llamar a la función
Get-HiddenFiles


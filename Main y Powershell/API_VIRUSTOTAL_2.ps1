
<#
.SYNOPSIS
Genera una lista de hashes SHA-256 de archivos en el directorio actual y consulta la API de VirusTotal para analizar esos hashes.

.DESCRIPTION
La función `Api_HashView` realiza los siguientes pasos:
1. Obtiene todos los archivos en el directorio actual y calcula el hash SHA-256 de cada uno.
2. Exporta los hashes a un archivo CSV.
3. Importa los hashes del archivo CSV.
4. Consulta la API de VirusTotal para cada hash utilizando una clave API proporcionada.
5. Muestra el nombre del archivo y los resultados del análisis (malicioso y sospechoso) en la consola.
6. Hace una pausa de 15 segundos entre cada consulta para evitar exceder el límite de solicitud de la API.

.EXAMPLE
Api_HashView
Genera hashes SHA-256 para todos los archivos en el directorio actual, exporta estos hashes a un archivo CSV y luego consulta la API de VirusTotal para obtener información sobre cada hash.

.PARAMETER
Este script no acepta parámetros.

.NOTES
- Asegúrate de tener una clave API válida de VirusTotal.
- La función realiza una pausa de 15 segundos entre cada consulta para evitar exceder los límites de solicitud de la API.
- Los resultados de la consulta se muestran en la consola.

#>

function Api_HashView {
    Set-StrictMode -Version Latest
    Write-Host "Generaremos una lista de hashes para registrar su sistema de archivos local"
    
    # Crear el nombre de archivo basado en la fecha y hora actuales
    $fileName = "$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').txt"
    $filePath = Join-Path -Path $PWD -ChildPath $fileName

    # Obtener todos los archivos en el directorio actual
    $files = Get-ChildItem -Path ".\*" -File
    $hashes = foreach ($file in $files) {
        Get-FileHash -Path $file.FullName -Algorithm SHA256 | Select-Object -Property Hash
    }

    # Exportar los hashes al archivo CSV
    $hashes | Export-Csv -Path .\hashes.csv -NoTypeInformation

    # Importar los hashes del archivo CSV
    $hashList = Import-Csv -Path .\hashes.csv | Select-Object -ExpandProperty Hash
    
    if ($hashList.Count -eq 0) {
        "No se encontraron hashes para procesar." | Out-File -FilePath $filePath -Encoding UTF8
        Write-Host "Los resultados se guardaron en: $filePath"
        return
    }

    $apiKey = "9f65611169a66d27dd54c8efb20b08fa69675d63fa739eb545e2c1755eee3ae0"
    $headers = @{
        "accept" = "application/json"
        "x-apikey" = $apiKey
    }

    # Iterar sobre cada hash y hacer las peticiones
    foreach ($hash in $hashList) {
        try {
            $url = "https://www.virustotal.com/api/v3/files/$hash"
            $response = Invoke-RestMethod -Uri $url -Method GET -Headers $headers -ErrorAction Stop

            if ($response -and $response.data) {
                $name = $response.data.attributes.meaningful_name
                $malicious = $response.data.attributes.last_analysis_stats.malicious
                $suspicious = $response.data.attributes.last_analysis_stats.suspicious
                $output = "Name: $name `nMalicious: $malicious `nSuspicious: $suspicious"
                $output | Out-File -FilePath $filePath -Append -Encoding UTF8
            } else {
                $output = "No data returned for hash $hash"
                $output | Out-File -FilePath $filePath -Append -Encoding UTF8
            }

            Start-Sleep -Seconds 15  # Asegurarse de no sobrepasar el límite de tasa de la API

        } catch {
            if ($_.Exception.Response.StatusCode -eq 404) {
                $output = "Hash $hash no encontrado en VirusTotal (404)."
                $output | Out-File -FilePath $filePath -Append -Encoding UTF8
            } else {
                $output = "Error: " + $_.Exception.Message
                $output | Out-File -FilePath $filePath -Append -Encoding UTF8
            }
        }
    }

    # Mostrar mensaje indicando dónde se guardó el archivo
    Write-Host "Los resultados se guardaron en: $filePath"
}

# Llamar a la función
Api_HashView


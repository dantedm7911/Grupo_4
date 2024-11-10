import string
import random

def generador_contrasena():
    try:
        # Solicitar al usuario la longitud de la contraseña
        longitud = int(input("Introduce la longitud de la contraseña: "))
        
        # Manejo de errores si el usuario introduce un valor no válido
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número positivo.")
        
        # Caracteres posibles para la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        # Generar la contraseña
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña generada: {contrasena}")
        
        # Guardar la contraseña en un archivo txt
        with open("contraseñas.txt", "a") as archivo:
            archivo.write(f"{contrasena}\n")
        print("Contraseña guardada en 'contraseñas.txt'")
    
    except ValueError as ve:
        print(f"Error: {ve}. Por favor, introduce un número positivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutarla
generador_contrasena()

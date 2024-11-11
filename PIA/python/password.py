import string
import random
import argparse

def generador_contrasena(longitud):
    try:
        # Manejo de errores si la longitud no es válida
        if longitud <= 0:
            raise ValueError("La longitud debe ser un número positivo.")

        # Caracteres posibles para la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Generar la contraseña
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

        # Guardar la contraseña en un archivo txt
        with open("contraseñas.txt", "a") as archivo:
            archivo.write(f"{contrasena}\n")
        print("Contraseña guardada en 'contraseñas.txt'")

    except ValueError as ve:
        print(f"Error: {ve}. Por favor, introduce un número positivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    # Configurar argparse para recibir la longitud de la contraseña como argumento
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras.")
    parser.add_argument("longitud", type=int, help="Longitud de la contraseña a generar")

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función con el argumento proporcionado
    generador_contrasena(args.longitud)

if __name__ == "__main__":
    main()

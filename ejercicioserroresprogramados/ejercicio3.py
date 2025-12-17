#Author: Jose Soriano
try:
    archivo = input("Introduce el nombre del archivo a abrir: ")
    with open(archivo, 'r') as file:
        contenido = file.read()

    print("Contenido del archivo:")
    print(contenido)
except FileNotFoundError:
    print('Hola amigo! El fichero no se encuentra por favor introduce correctamente el nombre del archivo')


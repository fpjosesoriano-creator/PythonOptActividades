#Author: Jose Soriano

def leer_archivo(nombre):
    try:
        archivo = open(nombre, 'r')
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    except Exception as e:
        print(f"Vaya parece que ha ocurrido un error")
        print(f"{e}")
    finally:
        archivo.close()

nombre_archivo = input("Introduce el nombre del archivo: ")
leer_archivo(nombre_archivo)

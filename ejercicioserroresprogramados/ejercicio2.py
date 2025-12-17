#Author: Jose Soriano
try:
    edades = {
        "Ana": 25,
        "Juan": 30,
        "Luis": 28
    }

    nombre = input("Introduce un nombre para obtener la edad: ")
    print(f"La edad de {nombre} es: {edades[nombre]}")
except KeyError:
    print('El nombre introducido no existe por favor introduzca un nombre que se encuentre en el diccionario')


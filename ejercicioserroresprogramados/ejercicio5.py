#Author: Jose Soriano

def obtener_numero():
    try:
        return int(input("Introduce un número entero: "))
    except ValueError:
        return obtener_numero()

numero = obtener_numero()
print(f"El número introducido es: {numero}")


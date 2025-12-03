#Author: Jose Soriano
""" Ejercicio 7
En este ejercicio se creará un diccionario para almacenar la cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el producto al diccionario, hasta que el usuario decida terminar. 
Al final se mostrará por pantalla toda la cesta de la compra y el coste total de la cesta. """
DICCIONARIO={}
while True:
    DICCIONARIO[str(input("Introduce producto: "))]=str(input("Introduce precio: "))
    opc=str(input("¿Desea continuar añadiendo productos? (y/n): "))
    if opc !="y":
        break
suma=0
for indice in DICCIONARIO:
    suma+=int(DICCIONARIO[indice])

print(DICCIONARIO)
print(f"La suma total de productos es: {suma}€")


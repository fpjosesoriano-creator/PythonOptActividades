#Author: Jose Soriano

#Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla. 
# Después deberá preguntar al usuario por un producto y el número de kilos que desea. 
# Por último, deberá mostrar por pantalla un mensaje indicando el precio total. 
# Si el producto no está en el diccionario, deberá mostrar un mensaje indicándolo

verduras={
    "Cebolla":1.30,
    "Patata":0.90,
    "Tomate":1.59,
    "Berenjena":1.25
}
verdura=str(input("Introduce verdura: ")).capitalize()
kg=float(input("Introduce el numero de kg: "))

if verdura in list(verduras.keys()):
    calculo=verduras[verdura]*kg
    print(f"El total a pagar es {calculo} €")
else:
    print(f"Vaya la verdura no se encuentra en stock")
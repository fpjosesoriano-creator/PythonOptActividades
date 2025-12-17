#Author: Jose Soriano

try:
    lista = [1, 2, 3, 4, 5]
    indice = int(input("Introduce un índice para acceder a la lista: "))

    print(f"El valor en la posición {indice} es: {lista[indice]}")
except IndexError:
    print('El indice introducido no existe o no es correcto')

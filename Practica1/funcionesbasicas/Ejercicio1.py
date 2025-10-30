"""
Ejercicio 1: Saludo
Crea una función que reciba dos parámetros. El primero será el saludo y el segundo será la persona a la que va dirigido el saludo. 
Deberá imprimir por pantalla el saludo correspondiente. Invoca la función para comprobar su funcionamiento.
"""
def saludo():
    saludo=str(input('Introduce el saludo personalizado: '))
    persona=str(input('Introduce el nombre de la persona: '))
    print(f"{saludo} {persona}")

saludo()
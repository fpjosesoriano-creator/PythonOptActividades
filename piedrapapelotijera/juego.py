#Author: Jose Soriano
import random

array = ["piedra", "papel", "tijera"]

while True:
    print("Bienvenido al juego!!")
    print("1-piedra , 2-papel, 3-tijera")
    opc = int(input("Introduce opcion: "))

    if opc < 1 or opc > 3:
        print("Por favor introduce numero del 1 al 3")
        break

    eleccion_usuario= array[opc - 1]

    eleccion_aleatoria = random.choice(array)

    print("\nTú elegiste:", eleccion_usuario)
    print(f"La eleccion aleatoria es:{eleccion_aleatoria}")

    
    if eleccion_usuario== eleccion_aleatoria:
        print("¡Empate!")
    elif (eleccion_usuario== "piedra" and eleccion_aleatoria == "tijera"):
        print("¡Has Ganado!")
    elif (eleccion_usuario== "papel" and eleccion_aleatoria == "piedra"):
        print("¡Has Ganado!")
    elif (eleccion_usuario== "tijera" and eleccion_aleatoria == "papel"):
        print("¡Has Ganado!")
    else:
        print("Has perdido... :(")


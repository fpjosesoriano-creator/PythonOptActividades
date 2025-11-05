#Crear un programa en Python que solicite al usuario el precio de un producto. 
#El programa mostrará por pantalla un mensaje informando del total de euros y céntimos en esa cantidad.

#Author: jsoriano

precio=input("Introduce un precio: ")

if precio.find(".")==-1:
    print(f"El precio es: {precio}")
else:
    posicion=precio.find(".")
    print(f"El importe total es de {precio[:posicion]} euros con {precio[posicion+1:]} centimos")
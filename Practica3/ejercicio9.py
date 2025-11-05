#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
#Author:jsoriano
cadena=input("Introduce cadena: ")
subcadena=input("Introduce subcadena: ")

if subcadena==cadena[:len(subcadena)]:
    print("La cadena empieza por subcadena")
else:
    print("La cadena no empieza por subcadena")
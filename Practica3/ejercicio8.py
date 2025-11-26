#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
#Author:jsoriano

cadena=input("Introduce cadena: ")
subcadena=input("Introduce subcadena: ")

if cadena.find(subcadena)==-1:
     print("La subcadena no esta en la cadena")
else:
     print("La subcadena está en la cadena")
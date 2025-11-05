#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
#Author:jsoriano
cadena=input("Introduce cadena: ")

if cadena==cadena[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")
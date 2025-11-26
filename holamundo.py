#Esto es un comentario de una linea
"""
Esto es un comentario multilinea
"""

mi_variable="Hola"#Notación en snake case
MiVariable="Hola"#notacion en camel case

#Estas 3 variables son distintas porque python interpreta las mayusculas.
edad=20
Edad=35
EDAD=40

#Imprimir un mensaje por consola
print('Hola Mundo')

saludo="Hola"
destinatario="ASIR2"
print(saludo,destinatario)

num1,num2,num3=2,4,6 #creación multiple de variables

num1=num2=num3=4 

var1="Texto" #Esta variable es de tipo texto
var2=4 #Esta variable es de tipo entero 

boolean=True #De tipo booleano
boolean=False

#obtener el tipo de una variable
print (type(boolean))
print (type(var1))

numero_con_decimales= 4.24 # De tipo float

print(type(numero_con_decimales))

#edad = input("Dime que edad tienes?")

#funcion con variables funcion f - f-strings
# print("Oye tu edad es de" + edad)

#print(f"Hola, tienes {edad} años")

saludo = input("Introduce saludo: ")
destinatario = input("Introduce el destinatario: ")

print(f"{saludo} {destinatario}")

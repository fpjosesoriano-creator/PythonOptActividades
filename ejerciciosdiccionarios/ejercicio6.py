#Author:Jose Soriano

""" Ejercicio 6
Escribir un programa que cree un diccionario vacío. 
El programa pedirá información al usuario (nombre, apellidos, fechaNacimiento, email, teléfono, etc.) y 
la irá almacenando en el diccionario. Al final se imprimirán todas las claves del diccionario y  el diccionario completo.
 """

diccionario={
    "Nombre":str(input('Introduce el nombre: ')),
    "Apellidos":str(input('Introduce el apellido: ')),
    "FechaNac": str(input('Introduce la fecha de nacimiento: ')),
    "Email": str(input('Introduce el email: ')),
    "Telefono": str(input('Introduce el Telefono: ')),
}

print(diccionario.keys())
print(diccionario)
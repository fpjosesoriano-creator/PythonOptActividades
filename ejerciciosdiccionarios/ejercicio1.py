#Author: Jose Soriano

#Escribir un programa en Python que pregunte al usuario su nombre, edad, 
# teléfono y dirección y lo almacene en una variable de tipo diccionario. 
# Después deberá imprimir por pantalla el mensaje

diccionario={
    "nombre":str(input("Introduce tu nombre: ")),
    "edad":str(input("Introduce tu edad: ")),
    "telefono":str(input("Introduce tu telefono: ")),
    "direccion":str(input("Introduce tu direccion: "))
    }
print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su telefono es {diccionario['telefono']}")

"""
Ejercicio 10
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""
 
passw=str(input('Introduce la contraseña: ')).lower()

def averiguapass(passw):
    passw2=str(input('Introduce la contraseña: ')).lower()
    if passw == passw2:
        print("Las contraseñas coinciden")
    else:
        print("Vaya las contraseñas no coinciden repite de nuevo") 
        averiguapass(passw)

averiguapass(passw)

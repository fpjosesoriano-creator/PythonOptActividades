#Crear un programa que pida al usuario su correo electrónico. 
#Ejemplo: msanchez@ciudadjardin.org. El programa deberá mostrar por pantalla el nombre de usuario, 
#es decir todo el texto hasta la @ y el dominio, es decir, desde la @ hasta el final de la cadena. 

#Author: jsoriano

correo=input("Introduce un correo electronico: ")

if "@" in correo and "." in correo:
    posicion=correo.find("@")
    print(correo[:posicion])
    print(correo[posicion:])
else:
    print("La estructura del correo no es correcta")
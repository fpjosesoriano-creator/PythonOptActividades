#Author: Jose Soriano

""" Ejercicio 8
Escribir un programa que cree un traductor español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por comas. 
El programa debe añadir al diccionario las palabras y sus traducciones. 
Tras rellenar el diccionario, el programa pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir. """
espanol=str(input("Introduce palabras en español, Ejemplo Hola,Adios: ")).split(",")

ingles=str(input("Introduce palabras en ingles Ejemplo Hello, Good bye: ")).split(",")

DICCIONARIO={}


while True:
    buffer=[]
    for i in range(len(espanol)):
        DICCIONARIO[espanol[i].lower()] = ingles[i].lower()

    frase=str(input("Introduce frase a traducir: ")).lower()
    for palabra in frase.split(" "):
        if palabra in DICCIONARIO:
            buffer.append(DICCIONARIO[palabra])
        else:
            print("Parece que alguna palabra proporcionada no se encuentra en el diccionario proporcionado")

    
    print(f"{" ".join(buffer)}")

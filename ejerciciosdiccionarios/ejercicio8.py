#Author: Jose Soriano

""" Ejercicio 8
Escribir un programa que cree un traductor español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por comas. 
El programa debe añadir al diccionario las palabras y sus traducciones. 
Tras rellenar el diccionario, el programa pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir. """
espanol=str(input("Introduce palabras con sus traducciones separadas por , Ejemplo Hola,Adios: ")).split(",")
ingles=str(input("Introduce palabras con sus traducciones separadas por , Ejemplo Hola,Adios: ")).split(",")
diccionario={}


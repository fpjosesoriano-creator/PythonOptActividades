#Author: Jose Soriano

#Escribir un programa que almacene el diccionario con las horas de cada módulo del curso {“ASO”: 6, “EIE”: 4} 
# Después deberá mostrar por pantalla las horas que tiene cada módulo en el formato
#El módulo ASO tiene 6 horas semanales.
#Al final deberá mostrar también el total de horas semanales.

modulos={
    "ASO": 5, 
    "SRI": 5,   
    "IAW": 4,   
    "ASGBD": 3,
    "SYAD": 3,  
    "INGL": 2,  
    "IPEC2": 3, 
    "PIN": 2,   
    "OPT": 3
}

suma=0
for key in modulos:
    print(f"El modulo {key} tiene {modulos[key]} horas semanales")
    suma+=modulos[key]

print(f"El computo total de horas semanales es {suma}")

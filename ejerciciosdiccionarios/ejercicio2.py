#Author: Jose Soriano

#Escribir un programa  en Python que almacene en una variable de tipo diccionario la correspondencia entre moneda y símbolo 
# {“Euro”:”€”, “Dolar”:”$”, “Libra”:”£”’’’’, “Yen”: “¥”}. 
# El programa preguntará al usuario por una divisa y mostrará su símbolo o un mensaje de aviso en caso de no encontrar la divisa
#  en el diccionario
divisas={"Euro":"€","Dolar":"$","Libra":"£","Yen":"¥"}

moneda=str(input("Introduce moneda: ")).capitalize()

if moneda not in list(divisas.keys()):
    print(f"La moneda {moneda} no se encuentra")
else:
    print(f"El simbolo de la moneda es {divisas[moneda]}")
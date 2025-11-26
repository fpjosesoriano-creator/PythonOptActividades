"""
Ejercicio 6
Escribe un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por en coche y la cantidad de litros de combustible 
que consumió durante ese recorrido. Mostrar el consumo del vehículo por cada 100 kilómetros recorridos.
"""
km=float(input('Intruce el numero de km: '))
litros=float(input('Intruce el numero litros: '))
print(f"El consumo del vehiculo a los 100 es: {((100*litros))/km}")
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde. 
hora=int(input('Dame el numero de horas'))
precio=float(input('Dame precio por hora'))
print(f"La paga que te corresponde es {hora*precio}€")
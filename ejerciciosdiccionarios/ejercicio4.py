#Author: Jose Soriano

#Crear un programa que almacene todos los meses en un diccionario. 
#El programa deberá pedir al usuario una fecha en formato dd/mm/aaaa y deberá indicar a qué mes (Enero, Febrero, etc) corresponde dicha fecha.

meses = {
    "01": "Enero",
    "02": "Febrero",
    "03": "Marzo",
    "04": "Abril",
    "05": "Mayo",
    "06": "Junio",
    "07": "Julio",
    "08": "Agosto",
    "09": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre"
}

fecha=str(input("Introduce fecha en formato dd/mm/aaaa: "))

print(f"La fecha {fecha} pertenece al mes {meses[fecha[3:5:1]]}")
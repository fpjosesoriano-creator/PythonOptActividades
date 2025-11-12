
#2.Realiza una función que reciba como parámetro un mes y devuelva el número de días que tiene ese mes.  
# Debes resolver este ejercicio con listas. Pista: puedes crear una lista con los meses que tienen 30 días y otra con los meses que tienen 31.  
# Puedes suponer que febrero tendrá 28 para simplificar.
#Author:Jsoriano



def calcular_dias(mes):
    meses_31 = ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre")
    meses_30 = ("abril", "junio", "septiembre", "noviembre")
    if mes in meses_31:
        print(f"El mes {mes} tiene 31 dias")
    elif mes in meses_30:
        print(f"El mes {mes} tiene 30 dias")
    else:
        print("el mes Febrero tiene 28 dias")

meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

for mes in meses:
    calcular_dias(mes)





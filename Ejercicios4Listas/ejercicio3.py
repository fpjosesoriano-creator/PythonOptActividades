#3.Realiza una función para calcular el salario de un trabajador. 
# La función deberá recibir el puesto del trabajador y el número de años de antigüedad en la empresa. 
# A partir de estos dos parámetros, deberá calcular el sueldo del empleado, teniendo en cuenta el salario base, 
# que cada año de antigüedad el sueldo sube según indica la siguiente tabla y por cada tres años completos el trabajador cobra un trienio. 
# La función deberá devolver el sueldo total del empleado.

#Author:Jsoriano

def calcular_salario(sal_base,sub_anual,sub_trienio,num_anos):
    return  sal_base+(num_anos*sub_anual)+((num_anos//3)*sub_trienio)

def calcular_salario_puesto(puesto,num_anos):
    if puesto=="informatica":
        print(calcular_salario(1500,22,120,num_anos))
    elif puesto=="rrhh":
        print(calcular_salario(1200,12,100,num_anos))
    elif puesto=="ventas":
        print(calcular_salario(1000,10,27,num_anos))


calcular_salario_puesto("informatica",8)
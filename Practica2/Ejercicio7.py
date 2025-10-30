edad=int(input("Introduce tu edad"))

def es_mayor_edad(edad):
    if edad<=18:
        return "Eres menor de edad"
    else:
        return "Eres mayor de edad"
    
print(f"{es_mayor_edad(edad)}")

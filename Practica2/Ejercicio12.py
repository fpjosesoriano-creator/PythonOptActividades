


def convertir_a_horas_minutos_segundos(segundos):
    horas=segundos/3600
    minutos=((segundos%3600)/60)
    segundo=((segundos%3600)%60)
    return int(horas),int(minutos),int(segundo)



def convertir_a_segundos(horas,minutos,segundos):
    return (horas*3600)+(minutos*60)+segundos


horas=int(input("Introduce las horas: "))
minutos=int(input("Introduce los minutos: "))
segundos=int(input("Introduce los segundos: "))

print(f"El total de segundos de los datos proporcionados son: {convertir_a_horas_minutos_segundos(segundos)}")
print(f"Los segundos convertidos a horas,minutos y segundos son: {convertir_a_segundos(horas,minutos,segundos)}")

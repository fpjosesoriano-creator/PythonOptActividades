nota=input("Introduce nota: ")

def calificaciones(nota):

    if isinstance(nota,float):
        if nota<5:
            return "Insuficiente"
        elif nota>5 and nota<7:
            return "Bien"
        elif nota>6 and nota<9:
            return "Notable"
        elif nota>9 and nota<10:
            return "Sobresaliente" 
        else:
            return "Matricula"
    else:
        nota=float(nota)
        return calificaciones(nota)

print(f"{calificaciones(nota)}")

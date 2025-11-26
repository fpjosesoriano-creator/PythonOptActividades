alumnos=["Ana","Pablo","Paco","Rosario","Tamara","Benito"]

#Matricula alumno

alumno=input("Introduzca alumno: ")

#Comprobamos que el alumno no este ya matriculado

if alumno in alumnos:
    print(f"El alumno {alumno} ya está matriculado")
else:
    print(f"Se ha registrado el usuario {alumno}")
    alumnos.append(alumno)

print(alumnos)

# Bucle for

for nombre in alumnos:
    print(f"El alumno {nombre} está matriculado en 2ASIR")

#Desmatricular un alumno

alumno=input("Introduce el nombre del alumno a desmatricular")

if alumno in alumnos:
    alumnos.remove(alumno)
else:
    print("El alumno no estaba matriculado")

print(f"En nuestra escuela hay {len(alumnos)}")

#Ordenar por orden alfabético 
print(alumnos.sort())
alumnos.sort(reverse=True)
print(alumnos)

# Fin de curso borrar la lista entera

alumnos.clear()
print(alumnos)

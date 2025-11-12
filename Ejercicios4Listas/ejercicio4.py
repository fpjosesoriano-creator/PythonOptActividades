#El instituto dispone de la siguiente lista de alumnos:

#alumnos_matriculados = ["Juan Sanchez”, "Luis Ramos”, “Ana Romero”, “Marta Moreno”]

#Realizar un programa que muestre un menú:

#Consultar matrícula.
#Matricular a un alumno.
#Anular la matrícula.
#Obtener el total de alumnos.

#La opción 1 pedirá el nombre de un alumno y nos dirá si está matriculado en nuestro instituto. La opción 2 pedirá un alumno y si no está matriculado, lo añadirá a la lista. La tercera opción pedirá un alumno y lo eliminará de la lista. La opción número 4 nos dirá el número de alumnos matriculados en nuestro instituto.

alumnos_matriculados = [ "Juan Sanchez", "Luis Ramos", "Ana Romero", "Marta Moreno" ]

while True :
    print("0. Salir")
    print("1.Consultar matrícula.")
    print("2.Matricular a un alumno.")
    print("3.Anular la matrícula.")
    print("4.Obtener el total de alumnos.")
    opcion=int(input("Introduce numero del menu para ejecutar: "))
    if opcion<5 and opcion>=0:
        if opcion==0:
            break
        if opcion==1:
            alumno=str(input("Introduce alumno: "))
            if alumno in alumnos_matriculados:
                print(f"El alumno {alumno} esta matriculado")
            else:
                print(f"El alumno {alumno} no esta matriculado")
        elif opcion==2:
            alumno=str(input("Introduce alumno: "))
            alumnos_matriculados.append(alumno)
            print(f"El alumno {alumno} ha sido matriculado")
        elif opcion==3:
            alumno=str(input("Introduce alumno: "))
            if alumno in alumnos_matriculados:
                alumnos_matriculados.pop(alumnos_matriculados.index(alumno))
                print(f"La matricula del alumno {alumno} ha sido anulada")
            else:
                print(f"No se puede anular la matricula el alumno {alumno} no esta matriculado")
        else:
            print(f"El total de alumnos son: {len(alumnos_matriculados)}")
    else:
        print("El parametro introducido no esta en el menu")
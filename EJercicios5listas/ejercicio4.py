#Author:jsoriano
letras_dni = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')

dni=input("Introduce DNI:")

if len(dni)!=9:
    print("DNI no valido")

numero=dni[:-1]
if numero.isnumeric() and len(dni)==9:
    numero=int(numero)
    if dni[8:9] == letras_dni[numero%23]:
        print(f"La letra es correcta {letras_dni[numero%23]}")
    else:
        print(f"La letra no es correcta {letras_dni[numero%23]} es distinto de {dni[8:9]}")
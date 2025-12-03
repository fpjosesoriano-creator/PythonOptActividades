while True:
    try:
        numero=int(input("Introduce numero: "))
        break
    #Si no ponemos el tipo de error va a capturar cualquier error
    except TypeError:
        print("Error, Debes introducir un numero")
    
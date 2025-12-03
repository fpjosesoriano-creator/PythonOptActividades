try:
    num1=int(input("Introduce el dividendo:"))
    num2=int(input("Introduce el divisor:"))

    print(f"La division entre {num1} y {num2} es {num1/num2}")
except ZeroDivisionError as e: 
    print("ERROR no puedes dividir entre 0!!!")
    print(e)
except ValueError as e:
    print("ERROR: Debes de introducir numeros.")
    print(e)
except:
    print("ERROR Inesperado.")

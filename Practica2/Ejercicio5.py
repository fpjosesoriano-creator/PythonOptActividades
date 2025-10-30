num1=int(input("Introduce numero1: "))
num2=int(input("Introduce numero2 para elevar el numero1: "))

def elevar(num1,num2):
    return num1**num2

print(f"El numero1 elevado a numero2 es: {elevar(num1,num2)}")

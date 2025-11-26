num1=int(input("Introduce numero1:"))
num2=int(input("Introduce numero2:"))

def esMultiplo(num1,num2):
    if num1%num2==0:
        return "num1 es multiplo de num2"
    elif num2%num1==0:
        return "num2 es multiplo de num1"
    else:
        return "No es multiplo"

print(f"{esMultiplo(num1,num2)}")
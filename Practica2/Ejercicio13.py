num1=int(input("Introduce numero1:"))
num2=int(input("Introduce numero2:"))

def division(num1,num2):
    if num2==0:
        return "Lo siento no se puede realizar una división entre 0"
    elif num1==0:
        return "Lo siento no se puede realizar una división si num1 es 0"
    else:
        return num1/num2

print(f"La división es: {division(num1,num2)}")
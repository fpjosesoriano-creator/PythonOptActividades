""" 
Esto produce un error de tipo index error
list=["enero","febrero"]
print(list[0])
print(list[2]) """

#numero=int(input("Introduce numero: "))

num1=int(input("Introduce el dividendo:"))
num2=int(input("Introduce el divisor:"))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Operacion no permitida no se puede dividir entre 0")



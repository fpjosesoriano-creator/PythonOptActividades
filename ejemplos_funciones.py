#Así es como definimos las funciones
def saludo():
    print("Buenos dias")
    print("Adiós")

#Así es como la invocamos
saludo()

def mensaje_bienvenida():
    return "Bienvenidos a Python"
    print("Hola") #Esta linea no se ejecuta ya que está detras de un return

mensaje=mensaje_bienvenida()
print(mensaje)
print(mensaje_bienvenida())

#función suma

def suma(num1,num2):
    return num1 + num2

print(suma(4,6))

def suma_v2():
    num1= int(input("Introduce numero: ")) 
    num2= int(input("Introduce el segundo numero: "))
    return num1 + num2

print(suma_v2())

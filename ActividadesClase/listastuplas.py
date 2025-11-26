#Tipos de datos compuestos

#Listas

frutas=["pera","manzana","chirimoya","fresa"]
loteria=[10,25,48,49,56]
alumnos=[]

print(len(frutas))
print(len(loteria))
print(len(alumnos))

#Añadir elemento a una lista
frutas.append("Melocoton")
frutas.append("platano")

#añadimos varios elementos a la lista original
frutas_exoticas=["papaya","mango","paraguayo","dragon fruit"]
frutas.extend(frutas_exoticas)
print(frutas)

#imprimir el elemento de una posicion
print(frutas[0])
print(frutas[-1])
print(frutas[::2])
print(frutas[::-1])

#insertar un elemento en la lista en una determinada posicion
frutas.insert(1,"maracuya")
print(frutas)

frutas[3]="kiwi"
print(frutas)

fruta=input("¿Que fruta quieres?")
#saber si tenemos un elemento en la lista
if fruta in frutas:
    print(f"Tenemos {fruta}")
else:
    print(f"No tenemos {fruta}")

if fruta not in frutas:
    print(f"No tenemos {fruta}")

#Eliminar elementos de una lista 

del frutas[0] #Elimina el elemento de la posición 0
print(frutas)

frutas.remove("paraguayo") #Elimina por nombre
print(frutas)

frutas.pop() #Elimina la de la ultima posición
print(frutas)

frutas.pop(2) # Elimina la fruta de la posción 2
print(frutas)

#convertir de string a lista
var3="hola"
var3=list(var3)
print(var3)
#convertir una lista a string
var4=['h','o','l','a']
var4="".join(var4)
print(var4)


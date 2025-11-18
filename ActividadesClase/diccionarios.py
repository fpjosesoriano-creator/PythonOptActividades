#Diccionarios
paises = {
    "España":"Madrid",
    "Francia":"Paris",
    "Portugal":"Lisboa",
    "Alemania":"Berlin"
}
meses={1:"Enero",2:"Febrero",3:"Marzo"}

print(paises)
print(paises['España'])
#Otra forma de hacer lo mismo
print(paises.get('Portugal'))
#Esto produce keyError porque la clave Islandia no existe en el diccionario
#print(paises['Islandia'])
#Esto nos devuelve un none, porque no se encuentra la clave en el diccionario
print(paises.get('Islandia'))

print(paises.keys())#Esto imprime las claves del diccionario
print(paises.values())#Esto imprime los valores del diccionario

#Añadir un nuevo elemento al diccionario o modificar uno existente
paises['Islandia']= "Reikiavik"

#Recorer el diccionario con un for
for clave in paises:
    print(f"El pais {clave} tiene de capital  {paises[clave]}")

# otra forma

for clave,valor in paises:
    print(f"El pais {clave} tiene de capital  {valor}")

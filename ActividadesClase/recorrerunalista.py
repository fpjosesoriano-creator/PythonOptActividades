modulos=["ASO","SAD","SRI","OPT",'IAW']

for modulo in modulos:
    print(f"Voy a aprobar {modulo}")

paises=["Japon","Italia","Francia"]

for pais in paises:
    print(f"He visitado {pais}")

tienda=["PCS","ratones","teclados","graficas"]

for producto in tienda:
    print(f"Tengo {producto}")

dinero = [4,5,6,1000]
total=0
for importe in dinero:
    total+=importe

print(f"Tengo {total}")

notas=[5,3,9,8]

total_notas=len(notas)
suma=0
for nota in notas:
    suma+=nota

resultado=suma/total_notas
print(f"La media es {resultado}")

print(max(notas))
print(min(notas))

#Implementar max
max=0
for nota in notas:
    if nota>max:
        max=nota

print(f"La nota mas alta es {max}")

provincias=["Palencia","Teruel","Murcia","Lugo"]
for i,provincia in enumerate(provincias):
    print(f"{i} - {provincia}")


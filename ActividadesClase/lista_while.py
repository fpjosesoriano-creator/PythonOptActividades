regalos=["reloj","ipad","playstation","xbox"]

for regalo in regalos:
    print(f"Quiero un/a {regalo}")

# Recorrer la lista con un while
i=0
while i<len(regalos):
    print(f"Quiero un/a {regalos[i]}")
    i+=1

i=len(regalos)-1

#Recorrer la lista con un while a la inversa
while i >= 0:
    print(f"Quiero un/a {regalos[i]}")
    i-=1

#Imprime del 0 al 2 
i=0
while i<6:
    if i==3:
        break
    print(i)
    i+=1
#Se queda en bucle infinito 
i=0
while i<6:
    if i==3:
        continue
    print(i)
    i+=1
#Author:jsoriano
def elimina_repetidos(lista):
    buffer=[]
    for valor in lista:
        if valor not in buffer:
            buffer.append(valor)
    buffer.sort()     
    return buffer
print(elimina_repetidos([5,1,2,3,4,2,1,4,3]))
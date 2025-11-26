#Author:jsoriano
def mini(lista):
    valor_minimo=lista[0]
    for valor in lista:
        if valor < valor_minimo:
            valor_minimo=valor
    return valor_minimo

print(mini([5,4,1,7]))
print(mini([1,5,6,723,0,85,66]))

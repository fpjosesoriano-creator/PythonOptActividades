# 1. Crea una función is_empty que reciba una lista y devuelva True si la lista está vacía o False si no lo está.
#Author: Jsoriano

def is_empty(lista):
    if len(lista)<=0:
        return True
    else:
        return False
    
print(is_empty([]))

#Author:jsoriano
def son_anagramas(palabra1,palabra2):
    if palabra1 == "" or palabra2=="":
        return "Las palabras no pueden estar vacias"
    
    lista_palabra1=list(palabra1.lower())
    lista_palabra2=list(palabra2.lower())
    lista_palabra1.sort()
    lista_palabra2.sort()
    palabra1="".join(lista_palabra1)
    palabra2="".join(lista_palabra2)
    return palabra1==palabra2

print(son_anagramas("roma","primo"))
print(son_anagramas("perro","poerr"))
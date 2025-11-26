
#Crea una función llamada file_type que reciba el nombre de un archivo y nos indique el tipo de archivo en función de su extensión.  Vamos a suponer que el nombre del archivo no va contener puntos.
#Si el archivo es (.jpg, .jpeg, o .png) nos dirá que es una imagen.
#Si el archivo es .pdf nos dirá que es un documento PDF.
#Si el archivo es (.rar, .zip, o .tar.gz) nos dirá que es un comprimido.
#En cualquier otro caso, la función imprimirá un mensaje indicando “Tipo de archivo no reconocido”.

#Author:jsoriano
nombre_archivo=input("Introduce nombre archivo: ")
imagenes=[".jpg",".png",".jpeg"]
comprimidos=[".rar", ".zip",".tar.gz"]

def file_type(nombre_archivo):
    if nombre_archivo.find(".") == -1:
        return "No se encuentra extension"
    
    extension=nombre_archivo[nombre_archivo.find("."):]
    if extension in imagenes:
        return "Es una imagen"
    elif extension in comprimidos:
        return "Es un comprimido"
    elif extension==".pdf":
        return "Es un pdf"
    else:
        return "Extension desconocida"

    
print(file_type(nombre_archivo))

precio=input("Introduce el total de la factura: ")
iva=input("Introduce el porcentaje de Iva sin el %")

def calcularIva(precio,iva):
    if iva=='':
        return int(precio) + (int(precio)*21/100)
    else:
        return int(precio) + (int(precio)*int(iva)/100)


print(f"El total de la factura con IVA es: {calcularIva(precio,iva)}" )



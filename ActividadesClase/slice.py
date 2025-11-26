codigo="10520-2025"

# Slice de cadena
print(codigo[0:5:1])
print(codigo[0])
print(codigo[9])
print(codigo[-1])
print(codigo[-2])
print(codigo[0:])# Si no especifico posición final va desde la posición dada hasta el final
print(codigo[:]) # toda la cadena
print(codigo[:6]) # si no ponemos la posición inicial seria por defecto 0

telefono="+34667852545"
print(telefono[0:3])

fecha="25/09/2025"
dia=fecha[0:2]
mes=fecha[3:5]
ano=fecha[6:]

print(dia,mes,ano)

mensaje="SALUDOS"
print(mensaje[::2]) #Desde el inicio hasta el final con salto 2
print(mensaje[::1])
print(mensaje[::-1])

print(mensaje.find("A")) # Me devuelve la posición de la primera letra A que encuentre

fecha2="5/4/2024"
dia=fecha2[:fecha2.find("/")]
mes_ano=fecha2[fecha2.find("/")+1:]
mes=mes_ano[:mes_ano.find("/")]
ano=mes_ano[mes_ano.find("/")+1:]

print(dia,mes,ano)

mes_ano.find("/",0,5)
print(fecha2.rfind("/"))
def area_circulo():
    radio=int(input("Introduce radio del circulo: "))
    return 3.1416*(radio**2)


def area_cilindro(area):
    altura=int(input("Introduce altura del cilindro: "))
    return area * altura

print(f"{area_circulo()}")
print(f"{area_cilindro(area_circulo())}")
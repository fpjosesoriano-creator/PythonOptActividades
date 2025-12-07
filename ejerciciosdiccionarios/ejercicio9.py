facturas = {}
cobrado = 0

while True:
    print("\n--- MENÚ ---")
    print("1. Insertar factura")
    print("2. Pagar factura")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        numero = input("Número de factura: ")
        importe = float(input("Importe: "))
        facturas[numero] = importe

    elif opcion == "2":
        numero = input("Número de factura a pagar: ")
        if numero in facturas:
            cobrado += facturas[numero]
            del facturas[numero]
        else:
            print("Esa factura no existe.")
    elif opcion == "3":
        print("Saliendo...")
        break

    pendiente = sum(facturas.values())
    print("Cobrado:", cobrado)
    print("Pendiente:", pendiente)

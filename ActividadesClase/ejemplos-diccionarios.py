fruteria={"peras":1.50, "Manzanas":2.60, "platanos":2.8}

fruta=input("Introduce la fruta que quieres: ")
kg=int(input("Cuantos kilos quieres: "))

preciokg=fruteria[fruta]
precioTotal=preciokg*kg

print(f"Su cuenta asciende a {precioTotal}")

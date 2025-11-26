"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
kg=float(input('Dame tu peso en KG: '))
altura=float(input('Dame tu altura en m2: '))
print(f"Tu calculo de IMC es: {(kg/((altura)**2)):.2f}")
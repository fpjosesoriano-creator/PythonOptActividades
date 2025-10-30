"""
Ejercicio 7
Escribe un programa que solicite al usuario una temperatura en escala Fahrenheit (debe permitir decimales) 
y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: Celsius = (5/9) * (Fahrenheit-32). 
Mostrar el resultado utilizando dos decimales.
"""
Fahrenheit=float(input('Dame la temperatura en escala Fahrenheit: '))
print(f"La temperatura convertida a Celsius es: {((5/9)*(Fahrenheit-32)):.2f}")
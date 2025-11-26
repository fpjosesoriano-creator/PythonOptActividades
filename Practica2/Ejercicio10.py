instancia=input("Introduce instancia en cm: ")

def convierte_cm_a_m(instancia):
    return instancia/100

def convierte_cm_a_km(instancia):
    return instancia/100000

def main(instancia):
    if isinstance(instancia,float):
        print(f"Son {convierte_cm_a_km(instancia)} km , Son {convierte_cm_a_m(instancia)} m y {instancia} cm")
    else:
        instancia=float(instancia)
        print(f"Son {convierte_cm_a_km(instancia)} km , Son {convierte_cm_a_m(instancia)} m y {instancia} cm")
        
main(instancia)
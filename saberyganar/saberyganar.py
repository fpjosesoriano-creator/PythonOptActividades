#Author: Jsoriano
import random
preguntas = [
    {
        'pregunta': '¿Cuál es la capital de Francia?',
        'respuestas': ['Madrid', 'París', 'Berlín', 'Lisboa'],
        'correcta': 1  # La respuesta correcta es 'París', índice 1
    },
    {
        'pregunta': '¿Quién pintó la Mona Lisa?',
        'respuestas': ['Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet'],
        'correcta': 2  # La respuesta correcta es 'Leonardo da Vinci', índice 2
    },
    {
        'pregunta': '¿Qué planeta está más cerca del Sol?',
        'respuestas': ['Venus', 'Mercurio', 'Marte', 'Tierra'],
        'correcta': 1  # La respuesta correcta es 'Mercurio', índice 1
    },
    {
        'pregunta': '¿Cuál es el océano más grande?',
        'respuestas': ['Atlántico', 'Índico', 'Ártico', 'Pacífico'],
        'correcta': 3  # La respuesta correcta es 'Pacífico', índice 3
    },
    {
        'pregunta': '¿En qué año llegó el hombre a la Luna?',
        'respuestas': ['1965', '1969', '1971', '1962'],
        'correcta': 1  # La respuesta correcta es '1969', índice 1
    },
    {
        'pregunta': '¿Cuál es la capital de España?',
        'respuestas': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia'],
        'correcta': 0  # Madrid, índice 0
    },
    {
        'pregunta': '¿Quién escribió "Cien años de soledad"?',
       'respuestas': ['Gabriel García Márquez', 'Mario Vargas Llosa', 'Pablo Neruda', 'Julio Cortázar'],
        'correcta': 0  # Gabriel García Márquez
    },
    {
        'pregunta': '¿Qué planeta es conocido como el "planeta rojo"?',
        'respuestas': ['Marte', 'Venus', 'Júpiter', 'Saturno'],
        'correcta': 0  # Marte
    },
    {
        'pregunta': '¿Cuántos continentes hay en el mundo?',
        'respuestas': ['5', '6', '7', '8'],
        'correcta': 2  # 7 continentes
    },
    {
        'pregunta': '¿En qué año comenzó la Segunda Guerra Mundial?',
        'respuestas': ['1939', '1914', '1945', '1929'],
        'correcta': 0  # 1939
    }
]

def premios(contador):
    if contador>=4 and contador<7:
        print (f"Enhorabuena has ganado 500€")
    elif contador>=7 and contador<9:
        print (f"Enhorabuena has ganado 1000€")
    elif contador==9:
        print (f"Enhorabuena has ganado 2000€")
    elif contador==10:
        print (f"Enhorabuena has ganado 5000€ ")
    else:
        print("Te vas sin un euro :))")
        

random.shuffle(preguntas)
contador_respuestas=0
try:
    for indice,pregunta in enumerate(preguntas):
        print(f"Llevas {contador_respuestas} acertadas")
        if len(pregunta)>0:
            print(pregunta['pregunta'])
            if len(pregunta['respuestas'])>0:
                for respuesta in enumerate(pregunta['respuestas']):
                    print(f"{respuesta}")
                respuesta=int(input("Introduce respuesta: "))
            if respuesta==pregunta['correcta'] and respuesta<=len(pregunta['respuestas']):
                print(f'Correcto la respuesta correcta es {pregunta['respuestas'][pregunta['correcta']]}')
                contador_respuestas+=1
            else:
                print('Incorrecta! vaya...')
except ValueError:
    print("Error el valor introducido debe ser el numero de la respuesta")
except IndexError:
    print("Vaya parece que hubo un error interno en el formulario...")
premios(contador_respuestas)









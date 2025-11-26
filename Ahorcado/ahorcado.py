import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
BUFFER=[]
def get_palabra_secreta():
    palabras=["casa","coche","tomate","lechuga"]
    palabra_secreta=random.choice(palabras)
    return palabra_secreta

def print_horca(posicion):
    return AHORCADO[posicion]

def crea_buffer(palabra_secreta):
    for posicion in palabra_secreta:
        BUFFER.append("-")

def main():
    palabra_secreta=get_palabra_secreta()
    crea_buffer(palabra_secreta)
    print(BUFFER)
    intentos=0
    while True:
        if "".join(BUFFER) != palabra_secreta:
            letra_adivinar=input("Introduce letra: ")
            if letra_adivinar in BUFFER or letra_adivinar not in palabra_secreta:
                intentos+=1
                print(print_horca(intentos))
                if intentos==6:
                    print(f"Perdiste la palabra secreta era {palabra_secreta}")
                    break
            for indice,letra_secreta in enumerate(palabra_secreta):
                if letra_adivinar in palabra_secreta and letra_adivinar==letra_secreta:
                    BUFFER[indice]=letra_adivinar
            print(BUFFER)
        else:
            print(f"Ganaste! la palabra secreta es {palabra_secreta}")
            break;        
    
main()





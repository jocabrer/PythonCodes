import random

def adivina_el_numero(numero_secreto, intentos):
    print("¡Adivina el número secreto entre 1 y 100!")
    
    for intento in range(1, intentos + 1):
        guess = int(input(f"Intento {intento}: Ingresa tu adivinanza: "))
        
        if guess < numero_secreto:
            print("El número secreto es mayor.")
        elif guess > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto}) en {intento} intentos!")
            break
    
    if guess != numero_secreto:
        print(f"¡Agotaste tus {intentos} intentos! El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    numero_secreto = random.randint(1, 100)
    intentos = 10  # Puedes cambiar el número de intentos si lo deseas.
    adivina_el_numero(numero_secreto, intentos)
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    print("Bienvenido al generador de la Secuencia de Fibonacci.")
    print("La secuencia comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")
    
    while True:
        try:
            n = int(input("Ingrese un valor entero 'n' para generar la secuencia (ingrese 0 para salir): "))
            
            if n == 0:
                print("¡Hasta luego!")
                break
            elif n < 0:
                print("Por favor, ingrese un valor entero no negativo.")
            else:
                sequence = fibonacci(n)
                print(f"Secuencia de Fibonacci hasta el término {n}: {sequence}")
        except ValueError:
            print("Por favor, ingrese un valor entero válido.")

        choice = input("¿Desea continuar? (Sí/No): ").lower()
        if choice != 'si' and choice != 'sí':
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()


import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza de números!")
    print("Intenta adivinar el número secreto entre 1 y 100.")
    print("Tienes un total de 10 intentos. ¡Buena suerte!\n")

    while intentos < 10:
        try:
            suposicion = int(input("Ingrese tu suposición: "))
            
            if 1 <= suposicion <= 100:
                intentos += 1
                if suposicion == numero_secreto:
                    print(f"\n¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
                    break
                elif suposicion < numero_secreto:
                    print("El número secreto es mayor. Intenta de nuevo.\n")
                else:
                    print("El número secreto es menor. Intenta de nuevo.\n")
            else:
                print("Por favor, ingresa un número entre 1 y 100.\n")
        except ValueError:
            print("Por favor, ingresa un número válido.\n")

    if intentos == 10:
        print(f"\n¡Agotaste tus 10 intentos! El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    juego_adivinanza()

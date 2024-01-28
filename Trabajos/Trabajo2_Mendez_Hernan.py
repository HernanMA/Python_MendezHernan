# ---- Trabajo 0 ---- 
# Definimos fibonacci y le agregamos un parametro que será donde ingresemos el número.

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
 
# Creamos un por para que se repita la secuencia hasta el número que digamos.    

    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

# Permitimos la entrada al usuario. 

def main():
    print("Bienvenido al generador de la Secuencia de Fibonacci.")
    print("La secuencia comienza con 0 y 1, y cada término subsiguiente es la suma de los dos términos anteriores.")

# Creamos un ciclo mientras y le agregamos las condiciones que solicitó el usuario.

    while True:
        
        # Dentro del bucle, se utiliza un bloque try-except para manejar posibles errores de entrada. Si el usuario ingresa un valor
        # no entero, se captura una excepción de tipo ValueError, y se le pide al usuario que ingrese un valor válido.
        try:
            # El usuario ingresa la cantidad de veces que se hará la secuencia fibonacci y si el usuario preciona 0 le dará fin a la secuencia.
            n = int(input("\nIngrese un número entero positivo para obtener la secuencia de Fibonacci (ingrese 0 para salir): "))
            
            # Si el usuario ingresa un número negativo se le informará que no es un número válido y que debe ingresar un número positivo.
            if n < 0:
                print("Número ingresado no valida, por favor, ingrese un número entero positivo.")
                continue

            # Si el usuario presiona 0 se dará fin a la secuencia fibonacci.
            if n == 0:
                print("¡Hasta luego, que tenga un buen día!")
                break

            fib_result = fibonacci_sequence(n)
            print(f"Secuencia de Fibonacci hasta el término {n}: {fib_result}")

        except ValueError:
            print("Error: Ingrese un valor entero válido.")

if __name__ == "__main__":
    main()


# ---- Trabajo 1 ----

# Se importa el módulo random para generar el número secreto de manera aleatoria.
import random

def guess_the_number():
    
    # Se utiliza random.randint(a, b) para seleccionar aleatoriamente un número secreto entre 1 y 100.
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    # Se imprime un mensaje de bienvenida e instrucciones para el usuario.
    print("¡Bienvenido al juego de adivinar el número secreto!")
    print(f"Adivina un número entre 1 y 100. Tienes un total de {max_attempts} intentos.")

    # El juego continúa mientras el número de intentos sea menor que el máximo permitido.
    while attempts < max_attempts:
        try:
            user_guess = int(input("Ingresa tu número: "))

            if user_guess < 1 or user_guess > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            attempts += 1

            # Se compara la suposición del usuario con el número secreto y se proporcionan pistas.
            if user_guess == secret_number:
                print(f"¡Felicidades! Adivinaste el número secreto {secret_number} en {attempts} intentos.")
                break
            elif user_guess < secret_number:
                print("El número secreto es mayor. ¡Inténtalo de nuevo!")
            else:
                print("El número secreto es menor. ¡Inténtalo de nuevo!")

        # Si el usuario ingresa algo que no es un número, se captura la excepción ValueError y se muestra un mensaje de error.
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

    if attempts == max_attempts:
        print(f"Lo siento, has agotado tus {max_attempts} intentos. El número secreto era {secret_number}.")

if __name__ == "__main__":
    guess_the_number()

## Desarrollado por Hernan Mendez Guerrero - 1101685607 
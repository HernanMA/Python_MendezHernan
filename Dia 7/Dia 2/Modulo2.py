# ---- Trabajo 1 ----
import math

def calcular_area_circulo(radio):
    # Fórmula para calcular el área del círculo: A = π * r^2
    area = math.pi * radio**2
    # Devolver el área calculada
    return area


# ---- Trabajo 2 ----
def encontrar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# ---- Trabajo 3 ----
def suma_de_dos_numeros(numero1, numero2):
    # Calcular la suma de los dos números
    suma = numero1 + numero2
    # Devolver el resultado
    return suma


# ---- Trabajo 4 ----
def calcular_total_productos(precios):
    total = sum(precios)
    # Devolver el total calculado
    return total


# ---- Trabajo de autos ----
def calcular_promedio_precios_autos(precios):
    # Verificar si la lista de precios está vacía
    if not precios:
        return "No se ingresaron precios."
    # Calcular el promedio de los precios
    promedio = sum(precios) / len(precios)
    # Devolver el resultado
    return promedio


# modulo_fibonacci.py
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


# modulo_adivinanza.py
import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while intentos < 10:
        try:
            suposicion = int(input("Ingrese tu suposición: "))
            
            if 1 <= suposicion <= 100:
                intentos += 1
                if suposicion == numero_secreto:
                    return f"\n¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos."
                elif suposicion < numero_secreto:
                    print("El número secreto es mayor. Intenta de nuevo.\n")
                else:
                    print("El número secreto es menor. Intenta de nuevo.\n")
            else:
                print("Por favor, ingresa un número entre 1 y 100.\n")
        except ValueError:
            print("Por favor, ingresa un número válido.\n")

    return f"\n¡Agotaste tus 10 intentos! El número secreto era {numero_secreto}."


## Desarrollado por Hernan Mendez Guerrero - 1101685607
import Modulo2

# Solicitar al usuario los valores para el cálculo del área del círculo
radio = float(input("Ingrese el radio del círculo: "))
print(Modulo2.calcular_area_circulo(radio))

# Solicitar al usuario los valores para encontrar el número mayor
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(Modulo2.encontrar_mayor(num1, num2, num3))

# Solicitar al usuario los valores para la suma de dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print(Modulo2.suma_de_dos_numeros(num1, num2))

# Solicitar al usuario los precios de los productos
n = int(input("Ingrese la cantidad de productos: "))
precios = []
for i in range(n):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    precios.append(precio)
print(Modulo2.calcular_total_productos(precios))

# Solicitar al usuario los precios de los autos
n = int(input("Ingrese la cantidad de autos: "))
precios = []
for i in range(n):
    precio = float(input(f"Ingrese el precio del auto {i + 1}: "))
    precios.append(precio)
print(Modulo2.calcular_promedio_precios_autos(precios))

# main.py
import Modulo2
import Modulo2

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
                sequence = Modulo2.fibonacci(n)
                print(f"Secuencia de Fibonacci hasta el término {n}: {sequence}")
        except ValueError:
            print("Por favor, ingrese un valor entero válido.")

        choice = input("¿Desea continuar? (Sí/No): ").lower()
        if choice != 'si' and choice != 'sí':
            print("¡Hasta luego!")
            break

    print("¡Bienvenido al juego de adivinanza de números!")
    print("Intenta adivinar el número secreto entre 1 y 100.")
    print("Tienes un total de 10 intentos. ¡Buena suerte!\n")
    print(Modulo2.juego_adivinanza())

if __name__ == "__main__":
    main()


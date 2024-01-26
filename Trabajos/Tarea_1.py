## ---- Trabajo 0 ----
# ---- Array ----

def calcular_promedio_precios_autos(precios):
    # Verificar si la lista de precios está vacía
    if not precios:
        print("No se ingresaron precios.")
        return
    
    # Calcular el promedio de los precios
    promedio = sum(precios) / len(precios)
    
    # Imprimir el resultado
    print(f"El promedio de precios de los autos es: {promedio}")

# Crear una lista para almacenar los precios de los autos
precios_autos = []

# Solicitar al usuario ingresar los precios de los autos
n = int(input("Ingrese la cantidad de autos: "))
for i in range(n):
    precio = float(input(f"Ingrese el precio del auto {i + 1}: "))
    precios_autos.append(precio)

# Llamar a la función para calcular y mostrar el promedio
calcular_promedio_precios_autos(precios_autos)



## ---- Trabajo 1 ----
# ---- Sin parametro y con retorno ----
import math

def calcular_area_circulo():
    # Valor predeterminado para el radio del círculo
    radio = 5.0
    
    # Fórmula para calcular el área del círculo: A = π * r^2
    area = math.pi * radio**2
    
    # Devolver el área calculada
    return area

# Llamada a la función y muestra del resultado
area_del_circulo = calcular_area_circulo()
print(f"El área del círculo es: {area_del_circulo}")


## ---- Trabajo 2 ----
# ---- Con parametro y sin retorno ----

def encontrar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"El número mayor es: {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"El número mayor es: {num2}")
    else:
        print(f"El número mayor es: {num3}")

# Ejemplo de uso
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

encontrar_mayor(numero1, numero2, numero3)


## ---- Trabajo 3 ----
# ---- Sin parametro y sin retorno ----

def suma_de_dos_numeros():
    # Solicitar al usuario que ingrese dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    # Calcular la suma de los dos números
    suma = numero1 + numero2
    
    # Imprimir el resultado
    print(f"La suma de {numero1} y {numero2} es: {suma}")

# Llamada a la función
suma_de_dos_numeros()


## ---- Trabajo 4 ----
# ---- Con parametro y con retorno ----

def calcular_total_productos(n):
    total = 0
    
    for i in range(n):
        # Solicitar al usuario que ingrese el precio del producto
        precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
        
        # Sumar el precio al total
        total += precio
    
    # Devolver el total calculado
    return total

# Solicitar al usuario la cantidad de productos
cantidad_productos = int(input("Ingrese la cantidad de productos: "))

# Llamar a la función y obtener el resultado
total_compra = calcular_total_productos(cantidad_productos)

# Imprimir el total de la compra
print(f"El total de la compra es: {total_compra}")



# ---- Ejercicio 6.2 ----

# Cadena de texto
texto = "Hola, este es un ejemplo de una cadena de texto. Este texto será analizado."

# Convertir la cadena a una lista de palabras
lista_palabras = texto.split()

# Crear un diccionario para almacenar la frecuencia de las palabras
frecuencia_palabras = {}

# Recorrer la lista de palabras
for palabra in lista_palabras:
    # Si la palabra ya está en el diccionario, incrementar su frecuencia
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    # Si la palabra no está en el diccionario, agregarla con frecuencia 1
    else:
        frecuencia_palabras[palabra] = 1

# Crear un conjunto de palabras únicas
conjunto_palabras = set(lista_palabras)

# Crear una tupla de números (las frecuencias de las palabras)
tupla_frecuencias = tuple(frecuencia_palabras.values())

# Imprimir los resultados
print("Lista de palabras:", lista_palabras)
print("Diccionario de frecuencias:", frecuencia_palabras)
print("Conjunto de palabras únicas:", conjunto_palabras)
print("Tupla de frecuencias:", tupla_frecuencias)


# Hecho por Hernan Mendez Guerrero 1101685607
import Modulo6

texto = "Hola, este es un ejemplo de una cadena de texto. Este texto será analizado."
lista_palabras, frecuencia_palabras, conjunto_palabras, tupla_frecuencias = Modulo6.procesar_texto(texto)

print("Lista de palabras:", lista_palabras)
print("Diccionario de frecuencias:", frecuencia_palabras)
print("Conjunto de palabras únicas:", conjunto_palabras)
print("Tupla de frecuencias:", tupla_frecuencias)



b = -10001

neg_b = Modulo6.negate(b)
print("b:", b, "neg_b: ", neg_b)

big = Modulo6.large_num(b)
print("b is big: ", big)



import Modulo6

print("introduce las cordenas de la primera bola")
bola1_x = int(input("Digita la posicion de (x): "))
bola1_y = int(input("Digita la posicion de (y): "))
bola1_radio = int(input("Ingresa el radio de la bola: "))
print("introduce las cordenas de la segunda bola")

bola2_x =  int(input("Digita la posicion de (x): "))
bola2_y = int(input("Digita la posicion de (y): "))
bola2_radio = int(input("Ingresa el radio de la bola: "))

distancia_centros = Modulo6.calcular_distancia(bola1_x, bola1_y, bola2_x, bola2_y)
suma_radios = Modulo6.calcular_suma_radios(bola1_radio, bola2_radio)

chocaran = Modulo6.verificar_colision(distancia_centros, suma_radios)

if chocaran:
    print(True)
else:
    print(False)

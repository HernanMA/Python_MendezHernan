def procesar_texto(texto):
    lista_palabras = texto.split()

    frecuencia_palabras = {}
    for palabra in lista_palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    conjunto_palabras = set(lista_palabras)
    tupla_frecuencias = tuple(frecuencia_palabras.values())

    return lista_palabras, frecuencia_palabras, conjunto_palabras, tupla_frecuencias



def negate(num):
    return -num

def large_num(num):
    res = (num > 10000)
    return res



import math

def calcular_distancia(bola1_x, bola1_y, bola2_x, bola2_y):
    return math.sqrt((bola2_x - bola1_x)**2 + (bola2_y - bola1_y)**2)

def calcular_suma_radios(bola1_radio, bola2_radio):
    return bola1_radio + bola2_radio

def verificar_colision(distancia_centros, suma_radios):
    return distancia_centros <= suma_radios


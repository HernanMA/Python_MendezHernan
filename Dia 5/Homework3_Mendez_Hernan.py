#---- Homework...3 ----

def negate(num):
    return -num

#Error: La función large_num(num) calcula si num > 10000 y almacena el resultado en res, pero no devuelve ningún valor.
#Solución: Debes devolver el resultado res en la función large_num(num).
def large_num(num):
    res = (num > 10000)
    return res

#Error: La variable b no está definida antes de ser usada en la función negate(b). 
#Solución: Debes definir la variable b antes de usarla.
b = -10001

#Error: En la línea neg_b = num, la variable num no está definida. 
#Solución: Deberías asignar el resultado de la función negate(b) a neg_b, es decir, neg_b = negate(b).
neg_b = negate(b)
print("b:", b, "neg_b: ", neg_b)

big = large_num(b)
print("b is big: ", big)


#Error 1: Falta registrar el valor de "b"

#Error 2: El negate(b) de la linea 6 reemplazarlo por el -num de la linea 7

#Error 3: prints de linea 8 y 11 le faltan paréntesis

#----------------------------------


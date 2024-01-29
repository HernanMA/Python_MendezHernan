# ---- job 0 ----
#Define una función que toma un parámetro.
def calculate_coins(amount):
#Divide la cantidad entre 10 utilizando la división entera (//) y almacena el resultado en la variable 
#coins_10. Esto representa la cantidad de monedas de 10 necesarias.
    
#cantidad %= 10: Utiliza el operador de asignación %= para actualizar el valor de cantidad tomando el residuo de la división por 10. 
#Ahora, cantidad contiene la cantidad restante después de calcular las monedas de 10.cantidad %= 10: Utiliza el operador de asignación
#%= para actualizar el valor de cantidad tomando el residuo de la división por 10. Ahora, cantidad 
#contiene la cantidad restante después de calcular las monedas de 10.
    coins_10 = amount // 10
    amount %= 10
#monedas_5 = cantidad // 5: Similar al paso 2, divide la cantidad actual entre 5 y almacena el resultado en 
#monedas_5, representando la cantidad de monedas de 5 necesarias.
    coins_5 = amount // 5
#cantidad %= 5: Actualiza cantidad tomando el residuo de la división por 5, ahora representando la cantidad restante después de calcular las monedas de 5.
    amount %= 5
#monedas_1 = cantidad: Almacena el valor actual de cantidad en monedas_1, representando la cantidad de monedas de 1 necesarias.
    coins_1 = amount

#return monedas_1, monedas_5, monedas_10: La función devuelve una tupla con las cantidades de monedas de 1, 5 y 10, respectivamente.
    return coins_1, coins_5, coins_10

#Se establece el valor que se desea descomponer en monedas.
entered_value = 28
#Llama a la función calcular_monedas con el valor dado y almacena el resultado en la variable resultado.
result = calculate_coins(entered_value)

#Imprime el resultado en una cadena formateada utilizando f-strings, mostrando las cantidades de monedas de 1, 5 y 10 necesarias para representar el valor dado.
print(f"For {entered_value} you need {result[0]} coins of 1, {result[1]} coins of 5, y {result[2]} coins of 10.")
coins_1, coins_5, coins_10 = entered_value % 10, (entered_value % 100) // 5, entered_value // 10

print("")
print(f"Input = {entered_value}")
print("")
print("            $1   $5   $10")
print(f"Output= {entered_value} = {result[0]} + {result[1]} + {result[2]}")

## Desarrollado por Hernan Mendez Guerrero - 1101685607 
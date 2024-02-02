## ---- Ejercicio 1 ----
import Modulo1
Modulo1.Hola_mundo()


# ---- Datos primitivos ----
#String

Modulo1.Texto()


#Int
import Modulo1
Modulo1.NumEntero(5)

#Float
NumeroDecimal = 11,3
print(NumeroDecimal)
print(type(NumeroDecimal))

#Double
NumeroDecimalLargo = 3.14167582737283
print(NumeroDecimalLargo)
print(type(NumeroDecimalLargo))

#Boolean
Boolean = True
print(Boolean)

# ---- Entradas parte de usuario ----
EntradaUsuario = input("Ingresa tu nombre ")
print("Tu nombre es: ", EntradaUsuario)

EntradaUsuarioEdad = input("Ingresa tu edad: ")
UsuarioEdad = int(EntradaUsuarioEdad)
print("Tu edad  es: ", UsuarioEdad)

# ---- Ciclos ----
# Ciclo for
for i in range(5): #For, contador in range(Desde, Hasta, Pasos):
    print (i)

#Ciclo while
booleanito = True
while booleanito == True: #While, condición a cumplir
    print("Sigo vivo")
    booleanito = False

# ---- Condicionales ----
Texto1 = "Campus"
if Texto1 == "Campus":
    print("Soy campus")
else:
    print("No soy campus")


## Desarrollado por Hernan Mendez Guerrero - 1101685607

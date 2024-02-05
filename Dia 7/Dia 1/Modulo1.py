def imprimir():
    print("Hello World")

def textito():
    Texto = "Campus"
    print(Texto)
    print(type(Texto))

def numerito():
    NumeroEntero = 7
    print(NumeroEntero)
    print(type(NumeroEntero))

def numdecimal():
    NumeroDecimal = 11,3
    print(NumeroDecimal)
    print(type(NumeroDecimal))

def numdecimallargo():
    NumeroDecimalLargo = 3.14167582737283
    print(NumeroDecimalLargo)
    print(type(NumeroDecimalLargo))   

def bool():
    Boolean = True
    print(Boolean) 

def entrada():
    EntradaUsuario = input("Ingresa tu nombre ")
    print("Tu nombre es: ", EntradaUsuario)

def entrada2():
    EntradaUsuarioEdad = input("Ingresa tu edad: ")
    UsuarioEdad = int(EntradaUsuarioEdad)
    print("Tu edad  es: ", UsuarioEdad)

def cic():
    for i in range(5): 
        print (i)

def whil():
    booleanito = True
    while booleanito == True: 
        print("Sigo vivo")
        booleanito = False    

def condicion():
    Texto1 = "Campus"
    if Texto1 == "Campus":
        print("Soy campus")
    else:
        print("No soy campus")    
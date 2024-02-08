import json

#1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la 
#   fecha de realización, mostrando en primer lugar los pedidos más recientes.
print("1\n")
importar1 = open('data.json')
Myjson = json.load(importar1)

def ListaApellidos(Lista):
    return Lista ["fecha"]
Pedidos = (Myjson["ventas"]["pedidos"])
Pedidos_Ordenados = sorted(Pedidos, key=ListaApellidos, reverse=True)
for i in Pedidos_Ordenados:
    print(i)
print("")

#2. Devuelve todos los datos de los dos pedidos de mayor valor.
print("2\n")
def ValorPedido(Valor):
    return Valor["total"]
MayorPedido = sorted(Pedidos, key=ValorPedido, reverse=True)
print(MayorPedido[0])
print(MayorPedido[1])
print("")

#3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga 
#   en cuenta que no debe mostrar identificadores que estén repetidos.
print("3\n")
Listado = []
for j in Pedidos:
    Listado.append(i["id_cliente"])
    SinRepetir = set(Listado)
    print(j)
print("")

#4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.

print("4\n")
count = 0
Lista2017 = []
for p in Myjson["ventas"]["pedidos"]:
    if "2017" in Myjson["ventas"]["pedidos"][count]["fecha"]:
        if Myjson["ventas"]["pedidos"][count]["total"] > 500:
            Lista2017.append(p)
        count  += 1
    else:
        count  += 1
print(p)
print("")

#5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.

print("5\n")
Comerciales = []
for k in Myjson ["ventas"]["comerciales"]:
    if 0.05 <= k["comisión"] <= 0.11:
        Comerciales.append(k)

NombreApellido = set()
for comercial in Comerciales:
    NombreApellido.add(f"{comercial["nombre"]} {comercial["apellido1"]}")
    for NombreApellidos in NombreApellido:
        print(NombreApellidos)
print("")

#6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.

print("6\n")
ValorMax = []
for x in Myjson ["ventas"]["comerciales"]:
    ValorMax.append(x["comisión"])
ValorMax.sort
ValorMax.reverse
print(ValorMax[0])    
print("")

#7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo 
#   ciudad sea "Sevilla". El listado deberá estar ordenado alfabéticamente por apellidos y nombre.

print("7\n")

contador = 0
ListaSevilla = []

def OrdenarDatos(client):
    return client ["apellido1"], client["nombre"]

for e in Myjson ["ventas"]["clientes"]:
    if "Sevilla" in Myjson["ventas"]["clientes"][contador]["ciudad"]:
        ListaSevilla.append(e)
        ListaSevilla = sorted(ListaSevilla, key = OrdenarDatos )
        contador += 1
    else:
        contador += 1
Ordenar = []
for comision in ListaSevilla:
    Ordenar.append(f"{comision["id"]},{comision["apellido1"]}, {comision["nombre"]}")
    print(Ordenar)
    print("")


#8. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente
    
print("8\n")
Contad = 0
ListaNombres = []
for l in Myjson["ventas"]["clientes"]:
    if l["nombre"].startswith("A") and l["nombre"].endswith("n") or l["nombre"].startswith("P"): 
        ListaNombres.append(l["nombre"])
        Contad += 1
    else:
        Contad += 1    

N_condicion_orden = sorted(ListaNombres)
print(N_condicion_orden)

#9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.

print("9\n")
Cuenta = 0
NombresA = []
for s in Myjson["ventas"]["clientes"]:
    if s["nombre"].startswith("A"):
        NombresA.append(s["nombre"])
        Cuenta += 1
    else:
        Cuenta += 1

NombreOrden = sorted(NombresA)
print(NombreOrden)
print("")

#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz".
#    Tenga en cuenta que se deberán eliminar los nombres repetidos.

print("10\n")   
Cuentamela = 0
NombresB = []
for v in Myjson["ventas"]["comerciales"]:
    if "Ruiz" in v["apellido1"]:
        NombresB.append(v["nombre"])
        Cuentamela += 1
    else:
        Cuentamela += 1

NombresAB = set(NombresB)
print(NombresAB)           

# Hecho por Hernan Mendez Guerrero 1101685607
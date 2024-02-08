import json

with open('data.json', 'r') as Negocios:
    diccionario = json.load(Negocios)

pedidos = diccionario["ventas"]["pedidos"]
comerciales = diccionario["ventas"]["comerciales"]
clientes = diccionario["ventas"]["clientes"]

while True:

    print("Que desea ver?")
    print("1. Los pedidos en orden de fecha (comenzando desde el más reciente)\n2. Los pedidos de mayor valor\n3. Los clientes que han realizado compras\n4. Los pedidos realizados en 2017, cuya cantidad total es superior a 500€\n5. Los comerciales con comisión entre 0.05 y 0.11\n6. El valor de la comisión más alto en la tabla comercial\n7. Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre\n8. Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P\n9. Listado de nombres de clientes que empiezan por A\n10. Listado de nombres de comerciales con apellido 'Ruiz  ")
    decision=int(input("Orden: "))

#1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la 
#   fecha de realización, mostrando en primer lugar los pedidos más recientes.
    

    if decision == 1:
        pedidos_ordenados = sorted(pedidos, key=lambda x: x['fecha'], reverse=True)
        print("Los pedidos en orden de fecha (comenzando desde el más reciente) son:")

        for i in pedidos_ordenados:
            print(i)



#2. Devuelve todos los datos de los dos pedidos de mayor valor.
            
    elif decision ==2:
        pedidos_mayorvalor=sorted(pedidos, key=lambda x: x['total'], reverse=True)
        print("Los pedidos de mayor valor son:")

        for i in pedidos_mayorvalor[:2]:
            print(i)



#3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga 
#   en cuenta que no debe mostrar identificadores que estén repetidos.
    elif decision==3:
        lista_ids_clientes = []

        for pedido in pedidos:
            id_cliente = pedido["id_cliente"]

            if id_cliente not in lista_ids_clientes:
                lista_ids_clientes.append(id_cliente)

        print("Los clientes que han realizado compras son:")
        print(lista_ids_clientes)



#4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
        
    elif decision==4:
        pedidos_2017_mayor_500 = [pedido for pedido in pedidos if pedido["fecha"].startswith("2017") and pedido["total"] > 500]    
        print("Los pedidos realizados en 2017, cuya cantidad total es superior a 500€ son:")

        for i in pedidos_2017_mayor_500:
            print(i)

#5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
    elif decision==5:
        comerciales_seleccionados = [comercial for comercial in comerciales if 0.05 <= comercial["comisión"] <= 0.11]
        print("Los comerciales con comisión entre 0.05 y 0.11 son:")

        for comercial in comerciales_seleccionados:
            nombre = comercial["nombre"]
            apellido1 = comercial["apellido1"]
            apellido2 = comercial.get("apellido2", "") 
            print(f"{nombre} {apellido1} {apellido2}")



#6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
            
    elif decision==6:
        max_comision = float('-inf') 

        for comercial in comerciales:
            comision = comercial.get("comision", 0) 
            if comision > max_comision:
                max_comision = comision
        print("El valor de la comisión más alto en la tabla comercial es:", max_comision)



#7. Devuelve el identificador, nombre y primer apellido de aquellos 
#   clientes cuyo ciudad sea "Sevilla". El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
        
    elif decision==7:
        clientes_sevilla = [cliente for cliente in clientes if cliente.get("ciudad", "") == "Sevilla"]
        clientes_sevilla_ordenados = sorted(clientes_sevilla, key=lambda x: (x["apellido1"], x["nombre"]))
        print("Clientes de Sevilla ordenados alfabéticamente por apellidos y nombre:")

        for cliente in clientes_sevilla_ordenados:
            identificador = cliente["id"]
            nombre = cliente["nombre"]
            apellido1 = cliente["apellido1"]
            print(f"ID: {identificador}, Nombre: {nombre}, Apellido: {apellido1}")



#8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y 
#   también los nombres que empiezan por P. El listado deberá estar ordenado alfabéticamente.
            
    elif decision==8:
        nombres_A_n = [cliente["nombre"] for cliente in clientes if cliente["nombre"].startswith("A") and cliente["nombre"].endswith("n")]
        nombres_P = [cliente["nombre"] for cliente in clientes if cliente["nombre"].startswith("P")]
        nombres_ordenados = sorted(nombres_A_n + nombres_P)
        print("")
        print("Listado de nombres de clientes que empiezan por A y terminan por n, o empiezan por P:")

        for nombre in nombres_ordenados:
            print(nombre)
        nombres_A_n = [cliente["nombre"] for cliente in clientes if cliente["nombre"].startswith("A")]



#9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.
        
    elif decision==9:
        print("")
        print("Listado de nombres de clientes que empiezan por A ")
        for nombre in nombres_A_n:
            print(nombre)
        nombres_ruiz = {comercial["nombre"] for comercial in comerciales if comercial.get("apellido1", "") == "Ruiz"}



#10. Devuelve un listado con los nombres de los comerciales que tienen como apellido "Ruiz".
#    Tenga en cuenta que se deberán eliminar los nombres repetidos.
        
    elif decision==10:
        print("Listado de nombres de comerciales con apellido 'Ruiz':")
        for nombre in nombres_ruiz:
            print(nombre)
    print("Desea continuar?(Si/No)")
    decision2=str(input("--> "))
    if decision2=="Si" or decision2=="si":
        print("")
    else:
        break

# Desarrollado por Hernan Mendez Guerrero 1101685607
"""
#Crear lista vacia
listas_nombres =[]

while True:
    variable_nombre = input("Ingrese su nombre: ")

    if variable_nombre != "salir":
        listas_nombres.append(variable_nombre)

    if variable_nombre == "salir":
        print("Nombres Guardados: ")
        print(listas_nombres)
        break
"""


"""
nombre = input("Ingrese nombre: ")
print(f"Nombre en Mayuscula {nombre.upper()}")
print(f"Nombre en Minuscula {nombre.lower()}")

if nombre.lower()=="cris":
    print("Hola Cris")
else:
    print("Tu no eres Cris")
"""
 
lista_perros =[]
lista_gatos =[]

while True:
    try:
        pregunta =int(input("""
        seleccion opcion:
        1: Resgistrar perro
        2: Registrar gato
        3: Mostrar listado de perros
        4: Mostrar listado de gatos
        5: Salir
        """))

        #Validar que opcion escogio el usuario

        if pregunta ==1:
            perro=input("Cual es el onombre del perro: ")
            lista_perros.append(perro)

        elif pregunta ==2:
            gato=input("Cual es el nombre del gato: ")
            lista_gatos.append(gato)

        elif pregunta ==3:
            print("Listado de perros")
            print(lista_perros)

        elif pregunta ==4:
            print("Listado de gatos")
            print(lista_gatos)

        elif pregunta ==5:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion Invalida")



    except ValueError:
        print("Ingrese una opcion valida")
    
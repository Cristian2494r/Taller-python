nombre= "Cristian"
documento= 1034922855
direccion= "Medellin"
tiene_deudas= True

print(nombre)

print("CONCATENACION USANDO +")
print("="* 30)

print("Mi nombre es: " + " y mi documento es: " + str(documento))

print("\nCONCATENACION USANDO ,")
print("="* 30)

print("Mi nombre es: " + " y mi documento es: ", documento)

print("\nCONCATENACION USANDO F-STRINGS")
print("="* 30)

print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("="* 30)

print(f"""
Nombre:     {nombre}
Documento:  {documento}
Direccion   {direccion}
¿tiene deudas?: {tiene_deudas}
""")

print("="* 30)

print(f"""
Nombre:     {nombre}
Documento:  {documento}
Direccion   {direccion}
¿tiene deudas?: {tiene_deudas}
""")

print(f"\n Hola, {nombre}!")

print(f"Bienvenido {nombre} a Python.\n")
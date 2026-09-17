#Solicitar Variables.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

#Validar si la edad es Negativa
if edad <0:
    print(f"Error:La edad {edad} es Invalidar")

#Validar si la edad es menor a 18 y calcular cuantos años le falta
else:
    faltan = 18 - edad
    print("Resultado: Es menor de edad.")
    print("Le faltan", faltan, "años para cumplir la mayoria de edad")


# Ejercicio 4
nombre_ciudad = input("Ingrese nombre de la ciudad: ")
Temperatura = float(input("La temperatura en grados celsius (10° a 32°:)"))

if Temperatura >= 32:
    print("Muy caliente")
elif Temperatura >= 26:
    print("Caliente")
elif Temperatura >= 18:
    print("Templado")
elif Temperatura >= 10:
    print("Fria")
elif Temperatura <= 10:
    print("Muy fria")

if Temperatura <18:
    print(f"Temperatura baja: llevar abrigo")    
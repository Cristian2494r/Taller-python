#Adivina numero Secreto
import random

numero_secreto = random.randint(1,10)
intentos = 5

for i in range(intentos):
    numero = int(input("Adivina el numero secreto (1-100): "))

    if numero == numero_secreto:
        print("que pro adivinaste👻")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"😒 te quedan {intentos_restantes} Intentos")




numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



n = 0
for i in range(1, n + 1):
    suma = suma + i
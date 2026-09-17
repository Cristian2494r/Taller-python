print("Ejercicio 1: Sumar dos numeros")
print("*"*20)

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segunndo numero: "))

suma = numero1 + numero2

print(f"La suma es: {suma}")


print("ejercicio 2: area de rectangulo")
print("*"*20)

base = float(input("Ingresa la base del rectangulo"))
altura = float(input("Ingrese la altura del rectangulo"))

area = base * altura

print(f"El area de rectangulo es: {area}")


print("ejercicio 3: Conversion de minutos a horas y minutos")
print("*"*20)

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")


print("ejercicio 4: calculo del precio con descuento")
print("*"*20)

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento/ 100)
precio_final = precio - valor_descuento

print(f"El precio final a pagar es: {precio_final}")


print("ejercicio 5: Intercambio de valores entre dos variables")
print("*"*20)

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a 
a = b
b = auxiliar

print(f"Despues del intercambio: a = {a} , b = {b}")


print("taller, ejerciicio 1")

base = float(input("Ingresa el largo del terreno en metros: "))
altura = float(input("Ingrese el ancho del terreno en metros: "))
print(f"el perimetro del terreno rectangular es: {(base*2)+(altura*2)} ")

print("="*80)
print("="*80)

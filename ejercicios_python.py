# -*- coding: utf-8 -*-
"""Ejercicios python



Ejercicios Tipo de Datos Simples
"""

#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2
saludo = "Hola Mundo"
print(saludo)

#Ejercicio 3
nombre = input("Ingrese su nombre:")
print("¡Hola " + nombre + "!")

#Ejercicio 4
operacion = (((3+2)/(2*5))**2)
print(operacion)

#Ejercicio 5
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
costo_horas = float(input("Ingrese el monto por hora: "))

salario = horas_trabajadas * costo_horas
print(f"""Su salario es: {salario}""")

#Ejercicio 6
n = int(input("Ingrese un entero positivo: "))

suma = n * (n+1) / 2

print(f"""El resultado es: {suma}""")

#Ejercicio 7
peso = float(input("Ingresse su peso en Kg: "))
altura = float(input("Ingrese su altura en metro: "))

imc = peso / altura

print(f"""Su indice de masa corporal es: {imc: .2f}""")

#Ejercicio 8
n = int(input("Ingrese un numero entero: "))
m = int(input("Ingrese otro numero entero: "))

c = n // m
r = n % c

print(f"""El cociente es: {c}""")
print(f"""El residuo es: {r}""")

#Ejercicio 9
cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
años = float(input("Ingrese los años: "))

capital_obtenido = cantidad_invertir * (interes_anual / 100 + 1) ** años

print(f"""El capital obtenido es: {capital_obtenido: .2f}""")

#Ejercicio 10
peso_payaso = 112
peso_muñeca = 75

payasos = int(input("Ingrese la cantidad de payasos: "))
muñecas = int(input("Ingrese la cantidad de muñecas: "))

peso_total = peso_payaso * payasos + peso_muñeca * muñecas

print(f"""El peso total es de: {peso_total} gramos""")

#Ejercicio 11
interes_anual = 0.04

cantidad_depositada = float(input("Ingrese la cantidad a depósitar: "))

primer_año = cantidad_depositada * (1 + interes_anual)
print(f"""El monto del primer año es: {primer_año: .2f}""")
segundo_año = primer_año * (1 + interes_anual)
print(f"""El monto del segundo año es: {segundo_año: .2f}""")
tercer_año = segundo_año * (1 + interes_anual)
print(f"""El monto del tercer año es: {tercer_año: .2f}""")

#Ejercicio 12
precio_pan = 3.49
descuento = 0.6

pan_vendido = int(input("Ingrese los panes vendidos: "))

precio_final = (precio_pan * (1 - descuento)) * pan_vendido

print(f"""El precio del pan fresco es de: ${precio_pan}, tiene un descuento por pan no fresco de {descuento * 100}%, el precio final es de: {precio_final: .2f}""")

"""Ejercicios de Cadenas"""

#Ejercicio 1
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese un numero entero: "))

for i in range(0, numero):
    print(nombre)

#Ejercicio 2
nombre_completo = input("Ingrese su nombre completo: ")

print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
n = len(nombre.replace(" ", ""))

print(f"""El nombre {nombre} tiene {n} letras""")

#Ejercicio 4
numero_telefono = input("Ingrese un numero de telefono con el formato (+xx-xxxxxxxxx-xx): ")

print(numero_telefono[4:-3])

#Ejercicio 5
frase = input("Ingrese una frase: ")

print(frase[::-1])

#Ejercicio 6
frase = input("Ingrese una frase:")
vocal = input("Ingrese una vocal en minuscula: ")

print(frase.replace(vocal, vocal.upper()))

#Ejercicio 7
correo = input("Ingrese su correo electronico: ")

print(correo[:correo.find('@')] + '@ceu.es')

"""Condicionales"""

#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
  print("Es mayor de edad")
else:
  print("Es menor de edad")

#Ejercicio 2
contraseña = "contraseña"

contraseña_ingresada = input("Ingrese su contraseña: ")

if contraseña == contraseña_ingresada.lower():
  print("Contraeña correcta")
else:
  print("Contraseña incorrecta")

#Ejercicio 3

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
resultado = num1 / num2

if num1 == 0:
  print("No es posible dividir entre cero")
else:
  print(f"""El resultado es: {resultado: .2f}""")

#Ejercicio 4
numero = int(input("Ingrese un numero entero:"))

if numero % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")

#Ejercicio 5
ingresos = float(input("Ingrese sus ingresos mensuales: "))
edad = int(input("Ingrese su edad: "))

if ingresos >= 1000 and edad >= 16:
  print("Debes pagar impuestos")
else:
  print("No debes pagar impuestos")

#Ejercicio 6
nombe = input("Ingrese su nombre: ")
genero = input("Ingrese su genero (M/F): ")

if (genero == "f" and nombre.lower() < 'm') or (genero == "m" and nombre.lower() > 'n'):
  grupo = "A"
else:
    grupo = "B"

print(f"""Tu grupo es: {grupo}""")

#Ejercicio 7
renta_anual = int(input("Ingrese su renta anual: "))

if renta_anual == 10000:
  print("Su tipo de impositivo es de 5%")
elif renta_anual > 10000 and renta_anual <= 20000:
  print("Su tipo de impositivo es de 15%")
elif renta_anual > 20000 and renta_anual <= 35000:
  print("Su tipo de impositivo es de 20%")
elif renta_anual > 35000 and renta_anual <= 60000:
  print("Su tipo de impositivo es de 30%")
else:
  print("Su tipo de impositivo es de 45%")
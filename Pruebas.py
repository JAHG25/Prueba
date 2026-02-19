#Pruebas

renta_anual = int(input("Ingrese su renta anual: "))

if renta_anual == 10000:
  print("Su tipo de impositivo es de 5%")
elif 10000 < renta_anual <= 20000:
  print("Su tipo de impositivo es de 15%")
elif 20000 < renta_anual <= 35000:
  print("Su tipo de impositivo es de 20%")
elif 35000 < renta_anual <= 60000:
  print("Su tipo de impositivo es de 30%")
else:
  print("Su tipo de impositivo es de 45%")

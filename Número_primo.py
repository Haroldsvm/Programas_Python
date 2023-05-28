valor=int(input("Ingrese un número: "))
rango=range(1,valor+1)
contador=0
for i in rango:
  if valor%i==0:
    contador=contador+1
  else:
    contador=contador+0
if contador<=2:
  print(valor,"Es un número primo")
else:
	print(valor,"No es un número primo")
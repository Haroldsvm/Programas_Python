lista=[1,2,3,4,5,6,7,8,9,4,5,6,1,2,3,43,10,5]
contar=0
for i in lista:
  contar=contar+1
print(contar)
mediana=int(contar/2)
posicion=lista[mediana]
print(posicion)
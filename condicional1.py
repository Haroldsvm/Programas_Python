a=int(input("Escriba un número: "))
b=int(input("Escriba otro número: "))

if(a==b):
    print("Los dos números son iguales")
else:
    if(a<b):
        print(b," Es el número mayor")
    else:
        print(a," Es el número mayor")
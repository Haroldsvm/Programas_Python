numero=(int(input("Digite un número: ")))
divisibleen5=numero%5
divisibleen11=numero%11

if divisibleen5==0 and divisibleen11==0:
    print(numero," Es divisible en 5 y en 11")
else:
    print(numero,"No es divisible en 5 y en 11")
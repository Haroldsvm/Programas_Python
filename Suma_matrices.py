a=[[8,6,-3],[2,1,4],[3,1,9]]
b=[[1,2,5],[-2,3,-6],[-3,5,-2]]

def suma_matrices(M,M2):
  if len(M)==len(M2) and len(M[0])==len(M2[0]):
    M3=[]
    for i in range(len(M)):
      M3.append([])
      for j in range(len(M[0])):
        M3[i].append(M[i][j]+M2[i][j])
    return M3
  else:
    return None
c=suma_matrices(a,b)
if c==None:
  print("No se pueden sumar las matrices")
else:
  for fila in c:
    print("[",end=" ")
    for elemento in fila:
      print(elemento,end=" ")
    print("]")
#programa que multiplica dos matrices
#tenemos la matriz X de 3x3 
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
#tenemos la matriz 3x4
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
#se tendra la matriz multiplicada en resultado la cual es 3x4
resultado = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

#se procesan las filas de X
for i in range(len(X)):
   #se procesan las columnas de Y
   for j in range(len(Y[0])):
       #se procesan las filas de Y
       for k in range(len(Y)):
           resultado[i][j] += X[i][k] * Y[k][j]

for r in resultado:
   print(r)
from numpy import *
arreglo = array([[2,7,11],[9,5,1],[4,3,8]])

print(arreglo)

x = arreglo.sum(0)
y = arreglo.sum(1)
z = diag(arreglo).sum()
w = arreglo [0,2] + arreglo [1, 1]+ arreglo [2, 0]

if all (x == y) and x [0] == z and z == w:
    print("El cubo es magico")
else:
    print("El cubo no tiene magia")
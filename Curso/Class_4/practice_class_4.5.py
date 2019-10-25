def pares (number):
    par = {n for n in number if n % 2 == 0}
    print("Pares = ",par)

numeros = {2,3,4,5,6,7,8,9,6,8,6,5,4,3,21,1}
pares(numeros)
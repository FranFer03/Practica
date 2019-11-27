students = [["alumno1", ["ex1", 7], ["ex2", 2], ["ex3", 7.5]],
            ["alumno2", ["ex1", 3], ["ex2", 5], ["ex3", 8]],
            ["alumno2", ["ex1", 5], ["ex2", 6], ["ex3", 9]]]
def columna():
    mostrar = 0
    for column in students:
        if mostrar == 0:
            print(column[1][0], "\t", column[2][0], "\t", column[3][0])
            mostrar = 1
        print(column[1][1], "\t", column[2][1], "\t", column[3][1])
def alumno():
    for alum in students:
        print("\t", alum[0])
        print(alum[1][1], "\n", alum[2][1], "\n", alum[3][1])

def promedio():
    for alum in students:
        print("El promedio del ", alum[0], "es : ", (alum[1][1] + alum[2][1] + alum[3][1])/3 )

promedio()
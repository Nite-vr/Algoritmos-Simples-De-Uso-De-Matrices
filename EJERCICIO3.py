def multiplicarMatrices(A, B):
    filasA = len(A)
    colA = len(A[0])
    filasB = len(B)
    colsB = len(B[0])

    if colA != filasB:
        print("Error: Dimensiones incorrectas. No se pueden multiplicar.")
        return None

    matrizC = []
    for i in range(filasA):
        fila = [0] * colsB
        matrizC.append(fila)
   
    for i in range(filasA):
        for j in range(colsB):
            suma = 0
            for k in range(colA):
                suma += A[i][k] * B[k][j]
            matrizC[i][j] = suma

    return matrizC

matriz1 = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]
matriz2 = [
    [1, 0, 2, 1],
    [3, 1, 0, 2],
    [2, 3, 1, 0],
    [0, 2, 3, 1]
]

matrizC = multiplicarMatrices(matriz1, matriz2)

print("Resultado:")
if matrizC:
    for row in matrizC:
        print(row) 
def shift_rows(A):
    FA = len(A)
    ColA = len(A[0])
    C = []
    for i in range(FA):
        d= i % ColA
        fila = A[i]
        new = fila[d:] + fila[0:d]
        C.append(new)

    return C

A = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],  
    [1, 2, 3, 4],  
    [1, 2, 3, 4],    
    
]

print("Matriz Original:")
print(A)
C = shift_rows(A)
print("\nMatriz recorriendo elementos:")
print(C)
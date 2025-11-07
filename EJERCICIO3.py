A = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

def dimension(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

def imprimir(A):
    f, c = dimension(A)
    for i in range(0, f):
        print("| ", end = "")
        for j in range(0, c):
            print("{:>5} |".format(str(A[i][j])), end = "")
        print("")

def Mensaje(mensaje):
    ascii_valores = [ord(c) for c in mensaje]
    bloques = []
   
    TAMANO_BLOQUE = 16
   
    num_bloques = (len(ascii_valores) + TAMANO_BLOQUE - 1) // TAMANO_BLOQUE

    for k in range(num_bloques):
        inicio = k * TAMANO_BLOQUE
        fin = (k + 1) * TAMANO_BLOQUE
        bloque_bytes = ascii_valores[inicio:fin]
       
        while len(bloque_bytes) < TAMANO_BLOQUE:
            bloque_bytes.append(0)

        matriz = []
        for i in range(0, TAMANO_BLOQUE, 4):
            matriz.append(bloque_bytes[i:i+4])
       
        bloques.append(matriz)
       
    return bloques

def suma_matrices(m1, m2):
    n = len(m1)
    m = len(m1[0])
    c = []
    for i in range(n):
        fila = []
        for j in range(m):
            r = m1[i][j] + m2[i][j]
            fila.append(r)
        c.append(fila)
    return c

def cifrar_mensaje(mensaje, a):
    nueva = Mensaje(mensaje)
    resultado = []

    for matriz in nueva:
        c = suma_matrices(matriz, a)
        resultado.append(c)

    return resultado, nueva

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

if __name__ == "__main__":
   
    texto = input("Ingresa el mensaje: ")
   
    resultado_suma, bloques_mensaje = cifrar_mensaje(texto, A)
   
    if not bloques_mensaje:
        print("El mensaje no generó bloques para procesar.")
    else:
        matriz_mensaje = bloques_mensaje[0]
        matriz_final = resultado_suma[0]

        print("\n==============================================")
        print("1. MATRIZ FIJA (A):")
        imprimir(A)
       
        print("\n2. MATRIZ DEL MENSAJE (Bloque 1):")
        imprimir(matriz_mensaje)
       
        print("\n3. MATRIZ FINAL (Suma Aritmética) del Bloque 1:")
        imprimir(matriz_final)
       
        if len(bloques_mensaje) > 1:
            print(f"\nNota: Se generaron {len(bloques_mensaje)} ")
        print("==============================================")


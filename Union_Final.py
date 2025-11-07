A = [
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
]

MIX_MATRIX = [
    [1, 0, 2, 1],
    [3, 1, 0, 2],
    [2, 3, 1, 0],
    [0, 2, 3, 1]
]

SBOX = [
 [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76],
 [0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0],
 [0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15],
 [0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75],
 [0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84],
 [0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf],
 [0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8],
 [0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2],
 [0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73],
 [0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb],
 [0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79],
 [0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08],
 [0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a],
 [0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e],
 [0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf],
 [0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]
]


def dimension(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

def imprimir_decimal(A):
    f, c = dimension(A)
    for i in range(0, f):
        print("| ", end = "")
        for j in range(0, c):
            print("{:>5} |".format(str(A[i][j])), end = "")
        print("")

def imprimir_hex(m):
    for row in m:
        print("| " + " | ".join(f"0x{x:02x}".ljust(5) for x in row) + " |")

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

def substitute(m):
    try:
        return [[SBOX[(b % 256) >> 4][(b % 256) & 0xF] for b in row] for row in m]
    except IndexError:
        print("Error: Valor fuera del rango para SBOX.")
        return None

def shift_rows(A):
    FA = len(A)
    if FA == 0:
        return []
    ColA = len(A[0])
    C = []
    for i in range(FA):
        d = i % ColA
        fila = A[i]
        new = fila[d:] + fila[0:d]
        C.append(new)
    return C

if __name__ == "__main__":
    
    texto = input("Ingresa el mensaje a cifrar (16 caracteres recomendados): ")
    
    bloques_mensaje = Mensaje(texto)
    
    if not bloques_mensaje:
        print("El mensaje no generó bloques para procesar.")
    else:
        matriz_estado = bloques_mensaje[0]
        
        print("\nMatriz ASCII:")
        imprimir_decimal(matriz_estado)
        
        print("\nMatriz Sumada:")
        estado_1 = suma_matrices(matriz_estado, A)
        imprimir_decimal(estado_1)
        
        print(f"\nSubstitución SBOX (Hex):")
        estado_2 = substitute(estado_1)
        
        if estado_2 is None:
            print("Error durante la substitución.")
        else:
            imprimir_hex(estado_2)
            
            print(f"\nFilas Desplazadas (Hex):")
            estado_3 = shift_rows(estado_2)
            imprimir_hex(estado_3)

            print(f"\nMultiplicación (Hex):")
            
            estado_4 = multiplicarMatrices(MIX_MATRIX, estado_3)
            
            if estado_4:
                imprimir_hex(estado_4)
            
            if len(bloques_mensaje) > 1:
                print(f"\nNota: El mensaje original generó {len(bloques_mensaje)} bloques,")
                print("pero solo se ha procesado el primero para esta demostración.")
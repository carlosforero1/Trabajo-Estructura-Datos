def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1, columnas_matriz1 = len(matriz1), len(matriz1[0])
    filas_matriz2, columnas_matriz2 = len(matriz2), len(matriz2[0])

    # Verifica si las matrices son multiplicables
    if columnas_matriz1 != filas_matriz2:
        return None

    # Inicializa la matriz resultante con ceros
    resultado = [[0] * columnas_matriz2 for _ in range(filas_matriz1)]

    # Realiza la multiplicación de matrices
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

# Ejemplo de uso:
matriz_a = [[1, 2, 3], [4, 5, 6]]
matriz_b = [[7, 8], [9, 10], [11, 12]]

resultado_multiplicacion = multiplicar_matrices(matriz_a, matriz_b)

if resultado_multiplicacion is not None:
    print("Resultado de la multiplicación:")
    for fila in resultado_multiplicacion:
        print(fila)
else:
    print("Las dimensiones de las matrices no son adecuadas para la multiplicación.")
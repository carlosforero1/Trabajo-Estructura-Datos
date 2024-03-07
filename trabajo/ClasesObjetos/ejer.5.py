def ordenamiento_seleccion(arreglo):
    n = len(arreglo)

    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[indice_minimo]:
                indice_minimo = j
        arreglo[i], arreglo[indice_minimo] = arreglo[indice_minimo], arreglo[i]
numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Arreglo original: {numeros}")

ordenamiento_seleccion(numeros)

print(f"Arreglo ordenado: {numeros}")
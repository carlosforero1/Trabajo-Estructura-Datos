def ordenamiento_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Arreglo original: {numeros}")

ordenamiento_burbuja(numeros)

print(f"Arreglo ordenado: {numeros}")
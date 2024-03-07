def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivot = arreglo[0]
        menores = [x for x in arreglo[1:] if x <= pivot]
        mayores = [x for x in arreglo[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Ejemplo de uso:
numeros = [64, 34, 25, 12, 22, 11, 90]
resultado_ordenado = quicksort(numeros)

print(f"Arreglo original: {numeros}")
print(f"Arreglo ordenado con Quicksort: {resultado_ordenado}")
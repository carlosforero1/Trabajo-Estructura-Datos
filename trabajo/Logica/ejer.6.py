
def eliminar_duplicados(arreglo):
    return list(set(arreglo))

# Ejemplo de uso:
numeros = [1, 2, 3, 2, 4, 5, 1, 6]
resultado_sin_duplicados = eliminar_duplicados(numeros)

print(f"Arreglo original: {numeros}")
print(f"Arreglo sin duplicados: {resultado_sin_duplicados}")
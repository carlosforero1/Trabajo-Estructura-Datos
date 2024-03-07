def encontrar_maximo(arreglo):
    if not arreglo:
        return None
    else:
        return max(arreglo)
numeros = [7, 2, 9, 1, 5, 3]
maximo = encontrar_maximo(numeros)

print(f"El elemento máximo en el arreglo es: {maximo}")

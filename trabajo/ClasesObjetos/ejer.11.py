def contar_ocurrencias(arreglo):
    ocurrencias = {}

    for elemento in arreglo:
        if elemento in ocurrencias:
            ocurrencias[elemento] += 1
        else:
            ocurrencias[elemento] = 1

    return ocurrencias

numeros = [1, 2, 3, 2, 4, 5, 1, 6]
resultado_ocurrencias = contar_ocurrencias(numeros)

print(f"Arreglo original: {numeros}")
print(f"Ocurrencias de cada elemento: {resultado_ocurrencias}")
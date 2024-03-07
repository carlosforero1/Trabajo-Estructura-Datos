def invertir_arreglo(arreglo):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio < fin:

        arreglo[inicio], arreglo[fin] = arreglo[fin], arreglo[inicio]


        inicio += 1
        fin -= 1

numeros = [1, 2, 3, 4, 5]
print(f"Arreglo original: {numeros}")

invertir_arreglo(numeros)

print(f"Arreglo invertido: {numeros}")
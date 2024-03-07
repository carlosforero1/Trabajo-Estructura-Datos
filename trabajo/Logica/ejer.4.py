def fibonacci(n):
    if n <= 0:
        return "El valor de n debe ser un entero positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
n_valor = 7
resultado = fibonacci(n_valor)

print(f"El término {n_valor} de la secuencia de Fibonacci es: {resultado}")
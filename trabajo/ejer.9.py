def encontrar_subcadena(cadena, subcadena):
    if subcadena in cadena:
        return cadena.find(subcadena)
    else:
        return -1

# Ejemplo de uso:
texto_principal = "Hola, ¿cómo estás?"
subcadena_buscar = "cómo"

posicion = encontrar_subcadena(texto_principal, subcadena_buscar)

if posicion != -1:
    print(f"La subcadena '{subcadena_buscar}' se encuentra en la posición {posicion} de la cadena principal.")
else:
    print(f"La subcadena '{subcadena_buscar}' no se encuentra en la cadena principal.")
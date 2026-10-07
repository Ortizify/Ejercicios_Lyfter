def ordenar_palabras(texto):
    # Convertir el string en una lista
    palabras = texto.split("-")

    # Ordenar la lista alfabéticamente
    palabras.sort()

    # Convertir la lista nuevamente en un string
    resultado = "-".join(palabras)

    return resultado


cadena = "python-variable-funcion-computadora-monitor"

print(ordenar_palabras(cadena))
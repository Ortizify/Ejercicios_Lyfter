def sumar_lista(lista):
    suma = 0

    for numero in lista:
        suma += numero

    return suma


numeros = [4, 6, 2, 29]

resultado = sumar_lista(numeros)

print(resultado)
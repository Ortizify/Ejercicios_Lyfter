def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def obtener_primos(lista):
    primos = []

    for numero in lista:
        if es_primo(numero):
            primos.append(numero)

    return primos


numeros = [1, 4, 6, 7, 13, 9, 67]

print(obtener_primos(numeros))
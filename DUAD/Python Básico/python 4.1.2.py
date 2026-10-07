def invertir_texto(texto):
    texto_invertido = ""

    for letra in texto:
        texto_invertido = letra + texto_invertido

    return texto_invertido


frase = "Hola mundo"

resultado = invertir_texto(frase)

print(resultado)    
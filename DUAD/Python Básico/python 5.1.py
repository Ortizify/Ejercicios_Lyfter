def contar_mayusculas_minusculas(texto):
    mayusculas = 0
    minusculas = 0

    for letra in texto:
        if letra.isupper():
            mayusculas += 1
        elif letra.islower():
            minusculas += 1

    print(f"There's {mayusculas} upper cases and {minusculas} lower cases")


frase = "I love Nación Sushi"

contar_mayusculas_minusculas(frase)
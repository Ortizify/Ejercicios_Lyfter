numero = 10

def cambiar_numero():
    global numero
    print("Valor antes de cambiar:", numero)

    numero = 20

    print("Valor después de cambiar:", numero)

cambiar_numero()

print("Valor fuera de la función:", numero)
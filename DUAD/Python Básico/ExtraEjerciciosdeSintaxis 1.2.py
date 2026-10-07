# Pedimos el tiempo en segundos
segundos = int(input("Ingrese el tiempo en segundos: "))
# Comparamos con 600 segundos (10 minutos)
if segundos < 600:
    faltante = 600 - segundos
    print(faltante)
elif segundos > 600:
    print("Mayor")
else:
    print("Igual")
my_list = [3, 6, 0, -2, 4]
all_positive = True
for i in range(len(my_list)):
    if my_list[i] <= 0:
        all_positive = False
        break
if all_positive:
    print("Todos los numeros son positivos")
else:
    print("Hay almenos un numero negativo o cero")

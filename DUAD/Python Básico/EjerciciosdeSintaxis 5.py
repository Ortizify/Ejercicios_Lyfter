# Pedimos al usuario cuantas notas va a ingresar
n = int(input("How many grades do you want to enter? "))
# Creamos listas vacias para guardar las notas
grades = []
# Le pedimos al usuario que ingrese las notas
for i in range(n):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)
# Inicializamos contadores y sumas
approved_count = 0
disapproved_count = 0
approved_sum = 0
disapproved_sum = 0
total_sum = 0
# Revisamos cada nota
for grade in grades:
    total_sum += grade
    if grade >= 70:
        approved_count += 1 
        approved_sum += grade
    else:
        disapproved_count += 1
        disapproved_sum += grade
# Calculamos promedios
total_avg = total_sum / n if n > 0 else 0
approved_avg = approved_sum / approved_count if approved_count > 0 else 0
disapproved_avg = disapproved_sum / disapproved_count if disapproved_count > 0 else 0
# Mostramos resultados 
print("\nResults:")
print("Number of approved grades:", approved_count)
print("Number of disapproved grades:", disapproved_count)
print("Average of all grades:", total_avg)
print("Average of approved grades:", approved_avg)
print("Average of disapproved grades:", disapproved_avg)






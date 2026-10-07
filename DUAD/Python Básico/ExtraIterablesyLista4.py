my_list = [10, 20, 30, 40, 50,]
#calculate the sum
total = 0 
for i in range(len(my_list)):
    total += my_list[i]
#calculate the average
average = total / len(my_list)
print("Promedio:", average)
#Create a new list with values greater than the average
new_list = []
for i in range(len(my_list)):
    if my_list[i] > average:
        new_list.append(my_list[i])
print("Nueva lista:", new_list)
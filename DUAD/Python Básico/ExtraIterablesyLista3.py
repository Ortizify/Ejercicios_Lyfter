my_list = [9, 8, 7, 45, 5,]
#start assuming the first element is the smallest 
smallest = my_list[0]
#compare with the rest
for i in range(1, len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]
print("El menor valor es", smallest)

numbers = []
for i in range(7):
    num = int(input("Enter a number: "))
    numbers.append(num)
search = int(input("Enter the number to search: "))
count = 0
for i in range(len(numbers)):
    if numbers[i] == search:
        count += 1  
print("El numero", search, "aparece", count, "veces")



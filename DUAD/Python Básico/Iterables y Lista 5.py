numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
highest = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > highest:
        highest = numbers[i]
print(numbers)
print("The highest was", highest)
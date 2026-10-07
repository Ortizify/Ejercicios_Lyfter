# Ask the user for the three numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Assume the first number is the largest
largest = num1
# Compare with the second number
if num2 > largest:
    largest = num2
# Compare with the third number
if num3 > largest:
    largest = num3
# Display the result 
print("The largest number is:", largest)

print("The largest number is:", max(num1, num2, num3))


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the thrid number: "))
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print("The largest number is:", largest)

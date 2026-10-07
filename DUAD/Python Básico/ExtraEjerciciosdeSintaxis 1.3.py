# Ask the user for a number
number = int(input("Enter a number: "))
# Initialize total sum
total = 0
# Loop from 1 to the entered number
for i in range(1, number + 1):
    total += i # Add current number to total
#Show the result 
print("The sum of numbers from 1 to ", number, "is:", total)

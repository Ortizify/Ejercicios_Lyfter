# Ask the user for a number between 1 and 10 
number = int(input("Enter a number (1-10): "))
# Display the multiplication table from 1 to 12
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")



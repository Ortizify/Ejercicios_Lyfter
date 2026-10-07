# Ask the user for three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("ENter the second number: "))
num3 = int(input("Enter the third number: "))
# Check the condition 
if num1 == 30 or num2 == 30 or num3 == 30 or (num1 + num2 + num3 == 30):
    print("Correct")
else:
    print("Incorrect")

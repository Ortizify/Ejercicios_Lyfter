#TASK 1 
#1 string1 + string2
string1 = "Hola"
String2 = " Mundo"
result1 = string1 + String2
print("string1 + string2:", result1)

#2 string3 + number1 (string + int)
string3 = "Age: "
number1 = 33
# result2 = string3 + number1 # ERROR
print("string3 + number1: ERROR (cannot add text with a number)")

#3 number2 + string4 (int + string)
number2 = 33
string4 = "Years"
#result3 = number2 + string4 #ERROR
print("number2 + string4: ERROR (cannot add a number with a text)")

#4 list1 + list2
list1 = [1,2]
list2 = [3,4]
result4 = list1 + list2
print("list1 + list2:", result4)

#5 string5 + list3
string5 = "Hola"
list3 = [1, 2]
#result5 = string5 + list3 # ERROR
print("string5 + list3: ERROR (cannot add text with list)")

#6 float1 + int1
float1 = 5.5
int1 = 2
result6 = float1 + int1
print("float1 + int1:", result6)

#7 bool1 + bool2
bool1 = True
bool2 = True
result7 = bool1 + bool2
print("bool1 + bool2:", result7)

#TASK 2
#Cree un programa que le pida al usuario su nombre,\n
# apellido, y edad, y muestre si es un bebé, niño, preadolescente,/n
# adolescente, adulto joven, adulto, o adulto mayor.
# Ask for data to the user
name = input("Add your name")
last_name = input("Add your last name")
age = int(input("Add your age:"))
#Age classification
if age < 2:
    category = "baby"
elif age < 12:
    category = "boy"
elif age < 15:
    category = "preteenager"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult" 
elif age < 60:
    category = "adult"
else:
    category = "older adult"
#Show results
print(f"{name} {last_name}, you are a {category}.")

#Task 3
#Cree un programa con un numero secreto del 1 al 10.\n
#El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
import random
#Generate a secreat number between 1 and 10
secret_number = random.randint(1, 10)
print("I have chosen a number between 1 and 10.                                                                                                                         ")
#keep running until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    if guess ==secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low. Try again!")
    else:
        print("Too high. Try again!")
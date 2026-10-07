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
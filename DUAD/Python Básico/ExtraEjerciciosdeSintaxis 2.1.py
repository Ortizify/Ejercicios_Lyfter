# Para generar un numero aleatorio 
import random
# Generar el numero secreto del 1 al 10 
secreat_number = random.randint(1, 10)
# Iniciamos la Variable de adivinanza 
guess = 0 
# Mientras el usuario no adivine 
while guess != secreat_number:
    guess = int(input("Guess the secreat number (1,10): "))
    if guess != secreat_number:
        print("Wrong! Try again...")
# Si sale del bucle, es porque acerto
print(f"Congratulation! The secret number was {secreat_number}")

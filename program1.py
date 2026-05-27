# number guesing game
from random import random


user_name = input("What is your name? "),
print("Hello " + user_name[0] + ", welcome to the number guessing game!")

#importing the random number generator
num1 = int(random() * 100) + 1


attempts = 1
max_attempts = 5
won = False



print("think of a number between 1 and 100.")
guess = int(input("What is your guess? "))
while guess != num1 and max_attempts > 0 and attempts < 7:
    max_attempts -= 1
    if guess < num1:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    guess = int(input("What is your guess? "))
    attempts += 1
   
for i in range(1, 5):
    if guess == num1:
        print("Congratulations! You guessed the number!")
        break
print("number of  guesses: " + str(i))
print("The correct number was: " + str(num1))
# summary of the game
print("\n==========Game Summary:=======")
print(f"Player Name: {user_name[0]}")
print(f"Total Attempts: {attempts}")
print(f"Final Guess: {guess}")
if guess == num1:
    print("You won congrats the game in " + str(attempts) + " attempts!")
else:
    print("Sorry, you lost the game. Better luck next time!")

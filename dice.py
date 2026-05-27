  #!/usr/bin/env python3
# dice game for the user to solve
def solve_dice():
    print(f"=========WELCOME TO THIS INTERESTING GAME==========")
    print(" ")
    print("*" *20)
    name = input("enter your name :")
    print(" ")
    print("*" *20)
    print(f"Hello, {name}! welcome to this my interesting game.")
    print(""),
    print("*" *20)
solve_dice()
# inputing the number of sides the dice have
print("*.." * 20)
print("")
while True:
    try:
        sides = int(input("Enter the number of sides on the dice (or '0' to quit): "))
        if sides == 0:
            print("Thanks for playing!")
            exit()
        elif sides <= 0 or sides > 100:
            print(f"Invalid input. please enter a positive integer between 1 and 100. ")
            continue
        print("*,,")
        print("")
    except ValueError:
        print(f"Invalid input. please enter a positive integer between 1 and 100. ")
        continue    
    else:
        break

# rolling the dice and generating the random number
from os import name
import random
roll = random.randint(1, sides)
print(f"You rolled a roll of {roll} on a {sides}-sided dice.")
print("")
print("*" *20)

print("==========THANK YOU FOR PLAYING THIS GAME==========")


print(f"=============RECIPT FOR YOUR GAME=============")
print(f"player name: {name}")
print(f"Number of Sides: {sides}")
print(f"Roll Result: {roll}")
print(f"=============================================")
  #!/usr/bin/env python3
# dice game for the user to solve
def solve_dice():
    print(f"=========WELCOME TO THIS INTERESTING GAME==========")
    name = input("enter your name :")
    print(f"Hello, {name}! welcome to this my interesting game.")
solve_dice()
# inputing the number of sides the dice have
while True:
    try:
        sides = int(input("Enter the number of sides on the dice (or '0' to quit): "))
        if sides == 0:
            print("Thanks for playing!")
            exit()
        elif sides <= 0 or sides > 100:
            print(f"Invalid input. please enter a positive integer between 1 and 100. ")
            continue
    except ValueError:
        print(f"Invalid input. please enter a positive integer between 1 and 100. ")
        continue    
    else:
        break

# rolling the dice and generating the random number
import random
roll = random.randint(1, sides)
print(f"You rolled a roll of {roll} on a {sides}-sided dice.")


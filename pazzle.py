#!/usr/bin/env python3
# pazzle for the user to solve
def solve_puzzle():
    print("=========WELCOME TO PUZZLE GAME========== !")
    name = input("Enter Your Name: ")
  
    print(f"Hello, {name}! Let's start the game.")
    print("=======Here We Go!=========")
solve_puzzle()

# import the random number to be used in the puzzle
n = int(input("Enter a positive integer: "))

# check if random number is even or odd
even = n % 2 == 0
odd = n % 2 != 0


while n != 1:
    if n % 2 == 0: # check if even
        
        print(f"{n} is even, so we divide it by 2: {n // 2}")
        n = n // 2

    else: # odd case
        print(f"{n} is odd, so we multiply it by 3 and add 1: {n * 3 + 1}")
        n = 3 * n + 1
print(f"the number of time it took to reach 1 is: {1}")
solve_puzzle()
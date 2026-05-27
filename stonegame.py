#!/usr/bin/env python3
#  2 players of the game
# player 1
name1 = input("player 1 name: ") 
# player 2
name2 = input("player 2 name: ") 

print(" ")
print("welcome to the stone game, {name1} and {name2}!".format(name1=name1, name2=name2))
print(" ")
# rules of the game
print(f"the rules of the game are simple, {name1} and {name2}. you will take turns to remove 1 or 2 stones from the pile. the player who removes the last stone loses the game.".format(name1=name1, name2=name2))
# number of stones
num_stones = int(input("number of stones: "))
# player 1 starts first
current_player = name1
while num_stones > 0:
    print(f"there are {num_stones} stones left.".format(num_stones=num_stones))
    # ask the current player to remove 1 or 2 stones
    while True:
        try:
            stones_to_remove = int(input(f"{current_player}, how many stones do you want to remove (1 or 2)? ".format(current_player=current_player)))
            if stones_to_remove in [1, 2] and stones_to_remove <= num_stones:
                break
            else:
                print("invalid input. please enter 1 or 2, and make sure you don't remove more stones than are left.")
        except ValueError:
            print("invalid input. please enter a number.")
    
    # update the number of stones
    num_stones -= stones_to_remove
    
    # check if the current player has lost
    if num_stones == 0:
        print(f"{current_player} removed the last stone and loses the game. {name1 if current_player == name2 else name2} wins!".format(current_player=current_player, name1=name1, name2=name2))
        break
    
    # switch to the other player
    current_player = name1 if current_player == name2 else name2


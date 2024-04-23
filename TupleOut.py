#Importing Random
import random

p1 = 0
p2 = 0
dice_face = (1, 2, 3, 4, 5, 6)

#Code for game 
while p1 < 50:
    start = input("Player 1, press 'ENTER' to start your turn:")

    #Generates dice roll for player 1
    p1d1 = random.choice(dice_face)
    p1d2 = random.choice(dice_face)
    p1d3 = random.choice(dice_face)
    print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3} \n")

    #Checks for tuple out
    if p1d1 == p1d2 and p1d1 == p1d3:
        print("You have Tupled Out! You lose. \n")
        break
    
    #Checks fir fixed dice and option to re-roll
    if p1d1 == p1d2 or p1d1 == p1d3 or p1d2 == p1d3:
        while p1d1 == p1d2:
            roll = input("Do you want to re-roll your 3rd dice? (Y/N) ")
            if roll.upper() == 'Y':
                p1d3 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3} \n")
            else:
                break
        while p1d1 == p1d3:
            roll = input("Do you want to re-roll your 2nd dice? (Y/N) ")
            if roll.upper() == 'Y':
                p1d2 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3} \n")
            else:
                break
        while p1d2 == p1d3:
            roll = input("Do you want to re-roll your 1st dice? (Y/N) ")
            if roll.upper() == 'Y':
                p1d1 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3} \n")
            else:
                break
    


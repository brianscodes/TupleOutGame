#Importing Random
import random

p1 = 0
p2 = 0
dice_face = (1, 2, 3, 4, 5, 6)
game_end = False

#Code for game 
for index in range(5):
    #Player 1
    start = input("Player 1, press 'ENTER' to start your turn:")

    #Generates dice roll for player 1
    p1d1 = random.choice(dice_face)
    p1d2 = random.choice(dice_face)
    p1d3 = random.choice(dice_face)
    print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3}")

    #Checks for tuple out
    if p1d1 == p1d2 and p1d1 == p1d3:
        print("You have Tupled Out! You lose.")
        game_end = True
        break
    
    #Checks fir fixed dice and option to re-roll
    while p1d1 == p1d2 or p1d1 == p1d3 or p1d2 == p1d3:
        if p1d1 == p1d2:
            roll = input("Do you want to re-roll your 3rd dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p1d3 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3}")
                if p1d1 == p1d2 and p1d1 == p1d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break
        if p1d1 == p1d3:
            roll = input("Do you want to re-roll your 2nd dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p1d2 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3}")
                if p1d1 == p1d2 and p1d1 == p1d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break
        if p1d2 == p1d3:
            roll = input("Do you want to re-roll your 1st dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p1d1 = random.choice(dice_face)
                print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3}")
                if p1d1 == p1d2 and p1d1 == p1d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break

    #Displaying score for P1
    p1 += p1d1 + p1d2 + p1d3
    print(f"Player 1's score is {p1} \n")
    
    #Player 2
    start = input("Player 2, press 'ENTER' to start your turn:")

    #Generates dice roll for player 2
    p2d1 = random.choice(dice_face)
    p2d2 = random.choice(dice_face)
    p2d3 = random.choice(dice_face)
    print(f"Your dice roll is: {p2d1}, {p2d2}, {p2d3}")

    #Checks for tuple out
    if p2d1 == p2d2 and p2d1 == p2d3:
        print("You have Tupled Out! You lose.")
        game_end = True
        break
    
    #Checks fir fixed dice and option to re-roll
    while p2d1 == p2d2 or p2d1 == p2d3 or p2d2 == p2d3:
        if p2d1 == p2d2:
            roll = input("Do you want to re-roll your 3rd dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p2d3 = random.choice(dice_face)
                print(f"Your dice roll is: {p2d1}, {p2d2}, {p2d3}")
                if p2d1 == p2d2 and p2d1 == p2d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break
        if p2d1 == p2d3:
            roll = input("Do you want to re-roll your 2nd dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p2d2 = random.choice(dice_face)
                print(f"Your dice roll is: {p2d1}, {p2d2}, {p2d3}")
                if p2d1 == p2d2 and p2d1 == p2d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break
        if p2d2 == p2d3:
            roll = input("Do you want to re-roll your 1st dice? (Y/N) \n")
            if roll.upper() == 'Y':
                p2d1 = random.choice(dice_face)
                print(f"Your dice roll is: {p2d1}, {p2d2}, {p2d3}")
                if p2d1 == p2d2 and p2d1 == p2d3:
                    print("You have Tupled Out! You lose.")
                    game_end = True
                    break
            else:
                break

    #Displaying score for P2
    p2 += p2d1 + p2d2 + p2d3
    print(f"Player 2's score is {p2} \n")

if game_end == False:
    if p1 > p1:
        print(f"Player 1 wins! Your score is {p1}")
    else:
        print(f"Player 2 wins! Your score is {p2}")

    



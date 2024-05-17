#Importing Random
import random

p1Name = input("Enter a name for player 1: \n")
p2Name = input("Enter a name for player 2: \n")
p1 = 0
p2 = 0
dice_face = (1, 2, 3, 4, 5, 6)
game_end = False
count = 1

r1 = 0
r2 = 0
betAmount1 = 0
betAmount2 = 0


for index in range(3):
    print(f"Round {count}: \n")

    #implementing bets per round
    print("Lets bet on who you think will win this round!")
    placeHolder1 = print(f"{p1Name}, how much money do you want to put in your bet? \n$")
    placeHolder2 = print(f"{p2Name}, how much money do you want to put in your bet? \n$")

    #Code for game 
    for index in range(5):
        #Player 1
        start = input(f"{p1Name}, press 'ENTER' to start your turn:")

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
        if game_end == True:
            break

        #Displaying score for P1
        p1 += p1d1 + p1d2 + p1d3
        print(f"{p1Name}'s score is {p1} \n")
        
        #Player 2
        start = input(f"{p2Name}, press 'ENTER' to start your turn:")

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
        if game_end == True:
            break

        #Displaying score for P2
        p2 += p2d1 + p2d2 + p2d3
        print(f"{p2Name}'s score is {p2} \n")

    if p1 > p2:
        print(f"{p1Name} wins this round! \n {p1Name}'s score is {p1} \n {p2Name}'s score is {p2} \n")
        r1 += 1
        betAmount1 += placeHolder1
        betAmount2 -= placeHolder2
        print(f"{p1Name}, your current balance is {betAmount1} \n {p2Name}, your current balance is {betAmount2}")

    else:
        print(f"{p2Name} wins this round! \n {p1Name}'s score is {p1} \n {p2Name}'s score is {p2} \n")
        r2 += 1
        betAmount2 += placeHolder2
        betAmount1 -= placeHolder1
        print(f"{p1Name}, your current balance is {betAmount1} \n {p2Name}, your current balance is {betAmount2}")

    count += 1

if r1 > r2:
    print(f"{p1Name} has won the game! \n")
else:
    print(f"{p2Name} has won the game! \n")
    



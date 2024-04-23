#Importing Random
import random

p1 = 0
p2 = 0
dice_face = (1, 2, 3, 4, 5, 6)

#Code for game 
while p1 < 50:
    

    p1d1 = random.choice(dice_face)
    p1d2 = random.choice(dice_face)
    p1d3 = random.choice(dice_face)
    print(f"Your dice roll is: {p1d1}, {p1d2}, {p1d3} \n")

    if p1d1 == p1d2 and p1d1 == p1d3:
        print("You have Tupled Out! You lose. \n")
        break

    #if p1d1 == p1d2 or p1d1 == p1d3 or p1d2 == p1d3:

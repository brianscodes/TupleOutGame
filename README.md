# TupleOutGame
This code is for the game "Tuple Out".

This code holds a game for 2 players who each take turns rolling 3 dice. The game lasts 5 rounds for each player. The goal of the game is to get the highest amount of points after 5 rounds without tupling out.

The code starts by setting each player's score to 0 and setting up the range for the dice, 1 to 6. Once the game begins, the code will ask the player to press "ENTER" to start their turn. Each turn consists of 3 dice being rolled. If the dice that are rolled are all different numbers, the game will go to the next player's turn. If 2 of the dice the player rolled are the same, the game will ask the player if they want to re-roll the dice that are not the same. The code checks this by using if statements and a while loop to break when the player doesn't want to re-roll. After every roll, the code will check with an if statement if the dice are all the same number. If they are, the player has tupled out and has lost the game. If the player has not tupled out, their scores are added every turn. If none of the players tuple out during the whole game, their scores are then compared against each other and the player with the highest score wins. 

This code does not stop after a certain player has reached a certain number of points. Rather, it stops after both players have had 5 turns. This code also does not allow the user to re-roll their dice if their initial role consists of 3 different numbers, instead it ends the game and the other player wins. 

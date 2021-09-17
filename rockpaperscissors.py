import random
import time

name = str(input("Input your name"))
while name == "ai":
    name = str(input("Input a new name"))
loop = 1

while loop == 1:
    player_choice = str(input("Rock, Paper, or Scissors\n"))
    player_choice.lower()
    ai_choice = random.randint(1, 3)
    time.sleep(1)
    print("\nRock!")
    time.sleep(.5)
    print("Paper!")
    time.sleep(.5)
    print("Scissors!")
    time.sleep(.5)
    print("Shoot!")
    time.sleep(1)
    if player_choice == "rock":
        player_choice = 1
        print(name + " Picked Rock!")
    if player_choice == "paper":
        player_choice = 2
        print(name + " Picked Paper!")
    if player_choice == "scissors":
        player_choice = 3
        print(name + " Picked Scissors!")
    if ai_choice == 1:
        print("Ai Picked Rock!")
    if ai_choice == 2:
        print("Ai Picked Paper!")
    if ai_choice == 3:
        print("Ai Picked Scissors")
    
    time.sleep(.5)
    
    if player_choice == 1 and ai_choice == 3 or player_choice == 2 and ai_choice == 1     or player_choice == 3 and ai_choice == 2:
        print(name + " Wins.")
    elif ai_choice == player_choice:
        print("Its a draw!")
    else:
        print(name + " lost. GIT GUD")
    time.sleep(.5)
    loop2 = input("Play Again?(y/n)")
    if loop2 != "y":
        loop = 2
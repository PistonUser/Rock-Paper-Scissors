import random

name = str(input("What's your name?"))
#asks for name and sets as varible for later
loop = 1
#helps you to play the game over and over
while loop == 1:
    player_choice = int(input("Rock(1), Paper(2), or scissors(3)"))
    #asks for your choice
    bot_choice = random.randint(1, 3)
    #get a random choice for bot and sets as a varible
    choices = {1 : "Rock", 2 : "Paper", 3 : "Scissors",}
    #makes a dictonary to use for displaying
    print(name + " picked " + choices[player_choice])
    #displays player name and choice
    print("bot picked " + choices[bot_choice])
    #shows bot choice
    if player_choice == 1 and bot_choice == 3 or player_choice == 2 and bot_choice == 1 or player_choice == 3 and bot_choice == 2:
        print(name + " Wins.")
    elif bot_choice == player_choice:
        print("Its a draw!")
    else:
        print(name + " lost. GIT GUD")
    #says who wins based on the player choice and bot choice
    loop2 = input("Play Again?(y/n)")
    #asks if you want to play again and makes a varible
    if loop2 == "n":
        loop = 2
    #if you say no it changes the looping varible from the beginning to stop it
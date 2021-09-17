import random
name = str(input("What's your name?"))
loop = 1
while loop == 1:
    player_choice = int(input("Rock(1), Paper(2), or scissors(3)"))
    bot_choice = random.randint(1, 3)
    choices = {1 : "rock",2 : "paper",3 : "scissors",}
    print(name + " picked " + choices[player_choice])
    print("bot picked " + choices[bot_choice])
    if player_choice == 1 and bot_choice == 3 or player_choice == 2 and bot_choice == 1 or player_choice == 3 and bot_choice == 2:
        print(name + " Wins.")
    elif bot_choice == player_choice:
        print("Its a draw!")
    else:
        print(name + " lost. GIT GUD")
    loop2 = input("Play Again?(y/n)")
    if loop2 == "n":
        loop = 2
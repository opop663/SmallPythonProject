from random import randint

# Option
t = ["Rock", "Paper", "Scissors"]

# Computer choice
comp = t[randint(0,2)]

replay = True
player = ""
player_status = "tie"

while replay == True:
    player = input("Rock, Paper, Scissors?")
    if comp == player:
        print("Tie")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose!", comp, "covers", player)
        else:
            print("You win!", player, "smashes", comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You lose!", comp, "cut", player)
        else:
            print("You win!", player, "covers", comp)
    elif player == "Scissors":
        if comp == "Rock":
            print("You lose!", comp, "smashes", player)
        else:
            print("You win!", player, "cut", comp)
    else:
        print("Not valid play. Check your spelling.")

    replay = True
    computer = t[randint(0,2)]

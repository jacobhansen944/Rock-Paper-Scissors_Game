#A simple rock paper scisors game played against the AI
from random import randint

options = ["rock", "paper", "scissors"]

print("Let's play Rock, Papcer, Scissors!")
print("Best two our of three!")

player_victories = 0
npc_victories = 0

while True:
    print("Make your choice: rock\tpaper\tscissors")

    player_choice = str(input()).lower()

    if player_choice in options:
        npc_choice = options[randint(0, 2)]
        print("Good choice!")
        print("You \t vs \t NPC")
        print(player_choice + "\t \t" + npc_choice)

        #player victory
        if player_choice == "rock" and npc_choice == "scissors" or player_choice == "paper" and npc_choice == "rock" \
                or player_choice == "scissors" and npc_choice == "paper":
            player_victories += 1
            print("You win this round!")
        #npc victory
        elif player_choice == "rock" and npc_choice == "paper" or player_choice == "paper" and npc_choice == "scissors" \
                or player_choice == "scissors" and npc_choice == "rock":
            npc_victories += 1
            print("You lost this round,")
        else:
            print("It's a tie! Nobody wins this round.")

        print()


    else:
        print("Bad input, did you enter rock, paper, or scissors?")

    if player_victories >= 2:
        print("The game is over, the winner is the player!")
        break
    elif npc_victories >= 2:
        print("The game is over, the winner is the npc!")
        break
import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    
    player_choice = input("\nEnter...\n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

    if player_choice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(player_choice)

    computer_choice = random.choice("123")

    computer = int(computer_choice)
    print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("🍾 You win!")            # win + . = Emoji dialogue
    elif player == 2 and computer == 1:
        print("🍾 You win!")
    elif player == 3 and computer == 2:
        print("🍾 You win!")
    elif player == computer:
        
        print("🤝 Tie game!")
    else:
        print("🐍 Python wins!")

    print("\nPlay again?")

    while True:
        play_again = input("\nPlay again?\n Y for Yes or \nQ to quit\n")
        if play_again.lower()not in ["y", "q"]:
            continue
        else:
            break

    if play_again.lower() == "y":
        return play_rps()
    else: 
        print("\n🍾🍾🍾")
        print("Thank you for playing!\n")
        sys.exit("Bye!🙋‍♂️")

play_rps()

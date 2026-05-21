import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True
while play_again:
    player_choice = input("\nEnter...\n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

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
    play_again = input("\nPlay again?\n Y for Yes or \nQ to quit\n\n")

    if play_again.lower() == "Y":
        continue
    else: 
        print("\n🍾🍾🍾")
        print("Thank you for playing!\n")
        break

sys.exit("Bye!🙋‍♂️")

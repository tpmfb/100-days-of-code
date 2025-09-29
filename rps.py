import random

print("It's time for a game of RPS")
player_input = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0, 2)

if player_input == 0 and computer_input == 0:
    print("Tied")
elif player_input == 0 and computer_input == 1:
    print("Computer Wins")
elif player_input == 0 and computer_input == 2:
    print("You Win")
elif player_input == 1 and computer_input == 0:
    print("You Win")
elif player_input == 1 and computer_input == 1:
    print("Tied")
elif player_input == 1 and computer_input == 2:
    print("Computer Wins")
elif player_input == 2 and computer_input == 0:
    print("Computer Wins")
elif player_input == 2 and computer_input == 1:
    print("You Win")
elif player_input == 2 and computer_input == 2:
    print("Tied")
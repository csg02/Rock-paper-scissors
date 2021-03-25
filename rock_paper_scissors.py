import random

def get_random_choice():
    tools = ["Rock", "Paper", "Scissors"]
    return random.choice(tools)


computer_wins = 0
human_wins = 0


while True:
    computer_choice = get_random_choice()
    human_choice = input("Please choose between Rock,Paper and Scissors:")
    human_choice = human_choice.capitalize()
    print(f"The coice of the computer is {computer_choice}")
    if human_choice != "Rock" and human_choice != "Paper" and human_choice != "Scissors":
        print("Invalid choice!")
        break

    if human_choice == computer_choice:
        print(f"It's a draw!")
    elif human_choice == "Rock":
        if computer_choice == "Paper":
            print(f"Computer wins!")
            computer_wins += 1
        else:
            print(f"Human wins!")
            human_wins += 1
    elif human_choice == "Paper":
        if computer_choice == "Rock":
            print(f"Human wins!")
            human_wins += 1
        else:
            print(f"Computer wins!")
            computer_wins +=1
    elif human_choice == "Scissors":
        if computer_choice == "Rock":
            print(f"Computer wins!")
            computer_wins += 1
        else:
            print(f"Human wins!")
            human_wins += 1

    print(f"The score of human is {human_wins}")
    print(f"The score of computer is {computer_wins}")

if human_wins > computer_wins:
    print(f"Human managed to collect most of the wins!")
elif human_wins < computer_wins:
    print(f"Computer managed to collect most of the wins!")
else:
    print(f"Both the human and the computer have the same number pf wins!")
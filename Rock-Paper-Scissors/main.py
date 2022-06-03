import random

choices = ["R", "P", "S"]
while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        print("\nPlease select the letter corresponding to your choice.")
        player = input("'R' for rock, 'P' for paper, or 'S' for scissors: ").upper()
        if player not in choices:
            print("\nInvalid input. Please enter only a single letter eg. R, P, or S. Let's try again.")
        else:
            break
        
    print("\nPlayer (" + player + ") : CPU (" + computer + ")\n")

    if player == computer:
        print("Tie! Let's rematch!")
        continue
    elif player == "R":
        if computer == "P":
            print("The computer wins!")
            break
        if computer == "S":
            print("You win!")
            break
    elif player == "S":
        if computer == "R":
            print("The computer wins!")
            break
        if computer == "P":
            print("You win!")
            break
    elif player == "P":
        if computer == "S":
            print("The computer wins!")
            break
        if computer == "R":
            print("You win!")
            break
            
print("\nLet's play again soon! Bye.")
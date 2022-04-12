import random

userScore = 0`
computerScore = 0
rps = ["rock", "paper", "scissors"]

while True:
    userChoice = input("Enter rock, paper, or scissors here: ")
    if userChoice.lower() not in rps:
        print("Please enter only rock, paper, or scissors.")
        continue
    computerChoice = random.choice(rps)
    if userChoice == computerChoice:
        print("Tie")
    if computerChoice == "rock":
        if userChoice.lower() == "paper":
            print(f"Computer chose {computerChoice}")
            print("You get 1 point")
            userScore += 1
            if userScore == 3:
                print("You win")
                break
        elif userChoice.lower() == "scissors":
            print(f"Computer chose {computerChoice}")
            print("Computer got 1 point")
            computerScore += 1
            if computerScore == 3:
                print("Computer wins")
                break
    if computerChoice == "paper":
        if userChoice.lower() == "scissors":
            print(f"Computer chose {computerChoice}")
            print("You get 1 point")
            userScore += 1
            if userScore == 3:
                print("You win")
                break
        elif userChoice.lower() == "rock":
            print(f"Computer chose {computerChoice}")
            print("Computer got 1 point")
            computerScore += 1
            if computerScore == 3:
                print("Computer wins")
                break
    if computerChoice == "scissors":
        if userChoice.lower() == "rock":
            print(f"Computer chose {computerChoice}")
            print("You get 1 point")
            userScore += 1
            if userScore == 3:
                print("You win")
                break
        elif userChoice.lower() == "paper":
            print(f"Computer chose {computerChoice}")
            print("Computer got 1 point")
            computerScore += 1
            if computerScore == 3:
                print("Computer wins")
                break
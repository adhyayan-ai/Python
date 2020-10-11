name = input("What's your name? ")
import random
RPS = ["r", "p", "s"]
d = {"r": "Rock", "p": "Paper", "s": "Scissors"}
d2 = {"R": "Rock", "P": "Paper", "S": "Scissors"}
beats = {"r": "P", "p": "S", "s": "R"}
vtotal = None
while True:
    user = input("Rock, Paper, or Scissors? (R/P/S) : ")
    user = user.upper()
    AI = random.choice(RPS)
    if user == "QUIT":
        break
        # ohh yeahhh
    elif user == "ADHYAYAN":
        user = beats.get(AI)
    elif user == "R":
        pass
    elif user == "P":
        pass
    elif user == "S":
        pass
    else:
        print('''Please enter "r" for rock,
        "p" for paper,
        or "s" for scissors. 
        Enter "quit" to quit.''')
        continue
    def score():
        print("AI: ", d.get(AI))
        print("You: ", d2.get(user))
    def vd(a, b):
        if user == AI.upper():
            score()
            print("Draw")
        else:
            score()
            if user == "R":
                if AI == "p":
                    print("AI Wins.")
                else:
                    print(name, "WINS!")
            elif user == "P":
                if AI == "s":
                    print("AI wins.")
                else:
                    print(name, "WINS!")
            elif user == "S":
                if AI == "r":
                    print("AI Wins")
                else:
                    print(name, "WINS!")
            
    vd(AI, user)



        






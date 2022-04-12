import random

def add():
    firstNum = random.randint(1, 50)
    secondNum = random.randint(1, 50)
    answer = int(input(f"What's {firstNum} + {secondNum}? "))
    if answer == firstNum + secondNum:
        return True
    else:
        return False

def subtract():
    firstNum = random.randint(1, 50)
    secondNum = random.randint(1, firstNum)
    answer = int(input(f"What's {firstNum} - {secondNum}? "))
    if answer == firstNum - secondNum:
        return True
    else:
        return False

def multiply():
    firstNum = random.randint(1, 10)
    secondNum = random.randint(1, 10)
    answer = int(input(f"What's {firstNum} * {secondNum}? "))
    if answer == firstNum * secondNum:
        return True
    else:
        return False

def divide():
    firstNum = random.randint(1, 100)
    secondNum = random.randint(1, 10)
    answer = int(input(f"What's {secondNum*round(firstNum/secondNum)} ÷ {secondNum} ? "))
    if answer == secondNum*round(firstNum/secondNum) / secondNum:
        return True
    else:
        return False

score = 0
counter = 0

while True:
    userInput = input("What kind of math problem would you like? ")

    if userInput == "addition":
        if add():
            print("Nice job!")
            score += 1
        else:
            print("Nice try, but you got that one wrong! ")

        counter += 1

    elif userInput == "subtraction":
        if subtract():
            print("Nice job!")
            score += 1
        else:
            print("Nice try, but you got that one wrong! ")

        counter += 1

    elif userInput == "multiplication":
        if multiply():
            print("Nice job!")
            score += 1
        else:
            print("Nice try, but you got that one wrong! ")

        counter += 1

    elif userInput == "division":
        if divide():
            print("Nice job!")
            score += 1
        else:
            print("Nice try, but you got that one wrong! ")

        counter += 1

    elif userInput == "done":
        print(f"You got a {round(score/counter*100)}% \nThanks for playing! ")
        break
import random

with open("/home/adhyayanisepic/Adhyayan/Personal/Extra Learning Stuff/Coding/Python/Youtube/Python Exercises/Wordle/wordle.txt") as wordList:
    lines = wordList.readlines()
    words = [word.rstrip() for word in lines]

tries = 6
word = random.choice(words) #Route
print(word)

while tries > 0:
    encrypted = list("-----")
    guess = input("Guess the word: ") #Rules

    for count, letter in enumerate(guess):
        if word[count] == letter:
            encrypted[count] = letter.upper() #Same position
        elif letter in word:
            encrypted[count] = letter.lower() #In the word, but not same position

    print("".join(encrypted))

    if "".join(encrypted).lower() == word:
        print("You won! ")
        break
    else:
        tries -= 1
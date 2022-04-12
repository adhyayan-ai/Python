import words
import random

word = random.choice(words.wordsList) #Orange
encrypted = ["-"]*len(word) #------, O-----
tries = 10

while tries > 0:
    print("".join(encrypted))
    letter = input("Guess a letter: ")

    if letter not in word:
            tries -= 1
            print(f"{letter} is not in the word. You have {tries} tries left. ")
            if tries == 0:
                print(f"You lost. The word was {word}")
                break

    for count, wordLetter in enumerate(word):
        if letter == wordLetter:
            encrypted[count] = wordLetter
            print("Good job! You got that letter correct! ")
    
    if word == "".join(encrypted):
        print("That was the word! You won!")
        break

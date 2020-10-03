#This needs to be able to be run as a command line tool as shown below (not an input statement!)
#Name the python file: scrabble.py
#Include a function called score_word in a separate module. Import this function into your main solution code
#Allow anywhere from 2-7 character tiles (letters A-Z) to be inputted.
#Do not restrict the number of same tiles (e.g., a user is allowed to input ZZZZZQQ).
#Output the total list of valid Scrabble words that can be constructed from the rack as (score, word) tuples, sorted by the score and then by the word alphabetically as shown in the first example below.
#Then output 'Total number of words:' and the total number.
#You need to handle input errors from the user and suggest what that error might be caused by and how to fix it (i.e., a helpful error message)
#Implement wildcards as either * or ?. There can be a total of only two wild cards in any user input (that is, one of each character: one * and one ?). Only use the * and ? as wildcard characters. A wildcard character can take any value A-Z. Replace the wildcard symbol with the letter in your answer (see the second example below).
#Wildcard characters are scored as 0 points, just like in the real Scrabble game. A two wildcard word can be made, should be outputted and scored as 0 points.
#For partial credit, your program should take less than one minute to run with 2 wildcards in the input. For full credit, the program needs to run with 2 wildcards in less than 30 seconds.
#Write docstrings for the functions and puts comments in your code.
#You should only use the Python standard library in this assignment. However, any function in the standard library is allowed.


# Adhu's pseudocode:
#1. Take user input and make it lowercase
#2a. Create 6 lists
#2b. Make (For Loops) that go through each combination append to main_list those who match in valid words.
#3. Calculate points through dictionary.
#4. join 2 lists and create tuple with zip().
#5. print the points-word pairs.

#Mamma's pseudocode:
#steps:
#1) read data from text file and put in a list
#2) A list is created for all the words in txt file.
#3) Restrict user to input word of chars between 2-7. Words can be repeated
#4) check length of each word in the list, If length of word inside the list is between 2 and 7, go to next step
#5) make all combination possible with the characters available and keep matching with words in text file. 
#call function score_word
#If word matches the file, store in a tuple along with the len of the valid word.

#[(len[i], 'ls[i]') for i in len(ls[i]) if len is >2 and <7)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def score_word(word):
  total = 0
  for i in word:
  	total += (scores.get(i)) 
  return total
print(score_word('adhu'))
  
def removed(ls, value):
  replica = list(ls)
  for i in value:
    replica.remove(i)
  return replica


word = input("Enter your word here: ").lower() 
if len(word) < 2 or len(word) > 7:
    print("Please enter a word that's no less than 2 letters and no more than 7 letters. ")
    exit()
infile = open("/Users/vivek/desktop/Adhu_dev/diffculto/sowpods.txt", "r")
raw_input = infile.readlines()
data = [datum.strip('\n') for datum in raw_input]
firstList = list(word)
secondList = []
thirdList = []
fourthList = []
fifthList = []
sixthList = []
seventhList = []
mainList = []
validWordList = []
wordScores = []
for i in firstList: 
  others = removed(firstList, [i])
  for j in others:
    secondList.append(i+j)
for i in secondList:
    others = removed(firstList, [i[num] for num in range(len(i))])
    for j in others:
        thirdList.append(i+j)
for i in thirdList:
    others = removed(firstList, [i[num] for num in range(len(i))])
    for j in others:
        fourthList.append(i+j)

for i in fourthList:
    others = removed(firstList, [i[num] for num in range(len(i))])
    for j in others:
        fifthList.append(i+j)

for i in fifthList:
    others = removed(firstList, [i[num] for num in range(len(i))])
    for j in others:
        sixthList.append(i+j)

for i in sixthList:
    others = removed(firstList, [i[num] for num in range(len(i))])
    for j in others:
        seventhList.append(i+j)

mainList.extend(secondList)
mainList.extend(thirdList)
mainList.extend(fourthList)
mainList.extend(fifthList)
mainList.extend(sixthList)
mainList.extend(seventhList)

print(seventhList)


for i in mainList:
    for j in data:
        if i.upper() == j:
            validWordList.append(j.lower())


validWordList.sort(reverse=True, key=score_word)

wordScores.sort(reverse=True)

print(seventhList)

for i in validWordList:
    wordScores.append(score_word(i))

for word, score in zip(validWordList, wordScores):
    print((score, word))
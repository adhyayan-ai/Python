firstWord = input("Enter the original word: ")
secondWord = input("Enter the scrambled up word: ")

if sorted(firstWord) == sorted(secondWord):
    print("Anagram")
else:
    print("Not an anagram")
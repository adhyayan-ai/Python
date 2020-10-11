word = input("Enter your word here: ")
letters = list(word)
srettel = letters[::-1]
srettel = ("".join(srettel))
if word == srettel:
    print("Yes,", word, "is a palindrome.")
elif word != srettel:
    print("No.")
else:
    print("Something went wrong. Please try again.")
    

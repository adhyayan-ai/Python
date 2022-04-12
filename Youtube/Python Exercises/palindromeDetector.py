word = input("Enter your word here: ")

if word == word[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome!")


#bob -> bob
#bob -> ['b', 'o', 'b']
#['b', 'o', 'b'] -> bob
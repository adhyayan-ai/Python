#With this program, you can replace every instance of a specific value with another in the whole body of the text. For exaple, you can replace every "a" with an 'O', or maybe replace every 'nice'' with a 'kind'.
text = input("Enter your text here: ")
replaced = input("What text do you want to replace? ")

replace = input("What do you want to replace " + replaced + " with? ")

print("Your output text is: \n" + text.replace(replaced, replace))
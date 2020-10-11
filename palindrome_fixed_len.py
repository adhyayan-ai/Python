w = input('Please enter your first name here: ')
if w == "quit":
    quit()
w = w.upper()
count = 1
condition = (len(w) / 2)
while count < condition:
    if w[count - 1] == w[count - (count * 2)]:
        pass
    elif w[count - 1] != w[count - (count * 2)]:
        print(w)
        quit()
    else:
        print("Something else went wrong. Please contact the developers. ")
        quit()
    count += 1
print(w)
print("Palindrome!")

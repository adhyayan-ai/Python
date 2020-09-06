w = input('Please enter your first name here: ')
w = w.lower()
count = len(w)
reverse = ""
while count > 0:
    reverse += (w[count - 1])
    count -= 1
if w == reverse:
    print(w.capitalize())
    print("Palindrome")
elif w != reverse:
    print(reverse.capitalize())

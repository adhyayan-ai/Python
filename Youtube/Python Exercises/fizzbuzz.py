text = ""
num = int(input("Enter your number here: "))

if num%3 == 0:
    text += "Fizz"

if num%5 == 0:
    text += "Buzz"

print(text)
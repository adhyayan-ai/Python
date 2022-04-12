import random

count = int(input("How many passwords would you like? ")) #10
length = int(input("What should the length of the passwords be? ")) #5
word = input("What word do you want the password to contain? ") #Bob
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890_!@#$%^&*"

passwords = []

for pswdCount in range(count):
    password = []
    for char in range(length-len(word)):
        password.append(random.choice(chars))
    password.insert(random.randint(0, length-len(word)), word)
    passwords.append(password)


for password in passwords:
    print("".join(password))

#^Bob%
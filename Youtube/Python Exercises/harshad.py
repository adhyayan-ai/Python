def isHarshad(num):
    sumTotal = 0
    for digit in num:
        sumTotal += int(digit)
    
    if int(num) % sumTotal == 0:
        return "Harshad"
    else:
        return "Not Harshad"

num = input("Enter your number here: ")
print(isHarshad(num))
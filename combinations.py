def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

if factorial(4) != 24:
    exit()   

n = int(input("Enter the number of items you want to choose from: "))
r = int(input("Enter the number items you want to choose: "))

if n < r:
    print("The number of items you want to choose from must be equal to or more than the number of items you are choosing. Please try again. ")
    exit()

def combinations(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

print(combinations(n, r))

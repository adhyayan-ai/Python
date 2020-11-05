def combinations(n, r):
    def factorial(num):
        if num == 1:
            return 1
        return num * factorial(num-1)

    n = int(input("Enter the number of items you want to choose from: "))
    r = int(input("Enter the number items you want to choose: "))
    if n < r:
        print("The number of items you want to choose from must be equal to or more than the number of items you are choosing. Please try again. ")
        exit()
    return factorial(n)/(factorial(r)*factorial(n-r))

print(int(combinations(n, r)))
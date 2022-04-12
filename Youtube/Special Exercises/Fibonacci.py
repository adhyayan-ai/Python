FibNums = [1]
num = int(input("How many numbers of the fibonacci sequence would you like? "))
first = 0
second = 1
for i in range(num-1):
    new = first + second
    FibNums.append(new)
    first = second
    second = new

print(FibNums)
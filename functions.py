#def sayHello():
#    print("hello world")

#sayHello()

def add(*nums):
    count = 0
    for num in nums:
        count += num

    return count

def double(num):
    return num * 2

print(double(add(1, 2, 3)))
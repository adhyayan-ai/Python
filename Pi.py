name = input("Hello there! What's your name? ")

try: 
    digits = int(input(f"So, {name}, how many digits of pi would you like? "))
except:
    print("Please enter a number, not anything else. Please try again.")
numbers = ["3."]


var = (355%113)


for i in range(digits - 1):
    while (var//113) == 0:
        var = var * 10
    numbers.append(str(var//113))
    var = (var%113)




numbers = ("".join(numbers))

print(numbers)


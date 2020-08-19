try:
      num = int(input("How many numbers in the fibonacci sequence would you like? "))
except:
      print("Please enter a number only. Try again.")
      
dvar = 0


first = 0

second = 1

numbers = []


while dvar < num:
      numbers.append(first)
      next = first + second
      first = second
      second = next
      num += 1

numbers.remove(numbers[0])

print(numbers)

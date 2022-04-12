num = int(input("Enter the number here: "))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        break

if prime:
    print("Prime")
else:
    print("Not prime")
    
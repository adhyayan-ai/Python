prime = None
num = int(input("Enter a number here to see if it is a prime number: "))


factors = []

for i in range(2, (num)):
    if num%i == 0:
        factors.append(str(i))

for i in range(2, (num - 1)):

    if num%i != 0:
        prime = ("Yes, " + str(num) + " is prime.")

    else:
        print("No, " + str(num) +  " is not prime.")
        break
    
        




if not prime == None:
    print(prime)

choice = input("Would you also like a list of factors for " + str(num) + " ? ")

choice = choice.upper()

if choice == "YES" or "YEAH":
    if not prime == ("Yes, " + str(num) + " is prime."):
        print(" ,".join(factors))
        #:>)
    else:
        print("1,", str(num))
elif choice == "NO" or "NO THANKS":
    print("Ok then!")

else:
    print("Next time, please say no or yes.")



print("Have a nice day!")

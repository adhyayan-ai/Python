income = int(input("Please enter your income here: "))
if income <= 1000:
    tax = income * 0.05
elif income > 1000 and income <= 2000:
    tax = (50 + ((income - 1000) * 0.1))
elif income > 2000:
    tax = income * 0.15
print("Your tax owed is $" + str(int(tax)))
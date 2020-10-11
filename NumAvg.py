a = int(input("Enter the first number here: "))
b = int(input("Enter the second number here: "))
avg_type = int(input('Enter "1" for an arithmetic mean, enter "2" for a geometric mean, and enter "3" for a root-mean-square: '))
if avg_type == 1:
    avg = (a + b) / 2
elif avg_type == 2:
    avg = (a * b) ** 0.5
elif avg_type == 3:
    avg = (((a**2) + (b**2)) / 2) ** 0.5
print("The average is", avg)



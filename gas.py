gallons = float(input("Enter number of gallons here: "))
liters = gallons * 3.785
liters = round(liters, 4)
print(int(gallons), "Gallons is", liters, "liters.")
barrels = gallons / 19.5
barrels = round(barrels, 3)
print(int(gallons), "Gallons are", barrels, "Barrels.")
price = gallons * 3.65
price = round(price, 2)
print(str(price) + "$ is the price for", int(gallons), "gallons of gas.")

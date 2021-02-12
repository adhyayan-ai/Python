numDict = {"1": "I", "5": "V", "10": "X", "50": "L", "100": "C", "500": "D", "1000": "M"}
num = input("Enter your number here: ")
roman = ""
element = 0

if int(num) == 0:
    print("Sadly, the roman numbers system does not include \"0\". Have a good day! ")
    exit()

for i in num:
    element += 1
    zeroes = "0"*(len(num)-element)
    placeValue = i + zeroes
    if i == 0:
        continue

    if placeValue in numDict:
        roman += numDict.get(placeValue)
        continue
    
    if int(i) < 4:
        roman += "".join([numDict.get("1" + zeroes) for j in range(int(i))])

    elif int(i) > 5 and int(i) < 9:
        roman += numDict.get("5" + zeroes)
        roman += "".join([numDict.get("1" + zeroes) for j in range(int(i)-5)])

    elif int(i) == 4:
        roman += (numDict.get("1" + zeroes) + numDict.get("5" + zeroes))

    elif int(i) == 9:
           roman += (numDict.get("1" + zeroes) + numDict.get("10" + zeroes))
    else:
        print("Something went wrong. Please contact Adhyayan Singh.")

print(num, "in roman numerals is", roman + ". Thank you for using this!")
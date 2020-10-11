name = input("Enter your full name here: ")
name = name.lower()
namels = name.split(" ")
x = ""
for i in namels:
    i = list(i)
    i.append(i[0])
    i.pop(0)
    i.append("ay")
    i[0] = i[0].upper()
    i = "".join(i)
    x += (i)
    if i != namels[-1]:
        x += " "


print(x)
prompt = input("Enter numbers here (seperated by a space): ")
promptls = prompt.split(" ")
ls = []
average = 0
for i in promptls:
    ls.append(float(i))
for x in ls:
    average += x

average = average / len(ls)

print("The average is", round(average, 2))
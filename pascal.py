p = [[1]]
#whichRow
whichRow = int(input("How many rows? "))
print("1")
for x in range(1, whichRow + 1):
    p.append([1]) 
    for y in range(len(p[x-1])-1):
       p[x].append(p[x-1][y]+p[x-1][y+1])
    p[x].append(1) 
    for a in range(1):
        for z in p[x]:
            print(str(z), end=" ")
        print("", "".ljust(whichRow))
#print(p[whichRow - 1])
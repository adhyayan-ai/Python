p = [[1]]
whichRow = int(input("Which row of Pascal's Triangle do you want? "))
if not whichRow > -1:
    print("Please enter a positive number of rows only.")
for x in range(1, whichRow + 1):
    p.append([1]) 
    for y in range(len(p[x-1])-1):
       p[x].append(p[x-1][y]+p[x-1][y+1])
    p[x].append(1) 


print(p[whichRow])
pointsEarned = []
totalPoints = []
denom = 1
numer = 0
earned = None
total = None
lsDenom = []
index = -1
divisions = []
totalPointsOriginal = []
while True:
    print('Enter "quit" to break. ')
    earned = input("Enter points earned: ")
    if earned == "quit":
        break
    else:
        total =  input("Enter total number of points here: ")
        earned = int(float(earned))
        total = int(total)
        pointsEarned.append(earned)
        totalPoints.append(total)

for x in totalPoints:
    denom *= x

lengthTotal = len(totalPoints)

for y in range(lengthTotal):
    lsDenom.append(denom)


totalPointsOriginal = totalPoints
totalPoints.clear()
totalPoints.extend(lsDenom)

for x in totalPointsOriginal:
    divisions.append((denom / x))

for x in range(len(divisions)):
    index += 1
    pointsEarned[index] *= divisions[index]

for i in pointsEarned:
    numer += i

numer /= len(pointsEarned)

print("Your average grade is: " + str(numer) + "/" + str(denom))
    


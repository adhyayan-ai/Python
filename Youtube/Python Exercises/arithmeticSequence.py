sequence = input("Enter your sequence seperated by commas and spaces: ")
sequenceList = sequence.split(", ")
commonDifference = None

for num in sequenceList: #1, 2, 3, 4, 5, 6
    index = sequenceList.index(num)
    if index == 0: 
        commonDifference = int(sequenceList[index+1]) - int(num)
    elif index == len(sequenceList)-1:
        print("Arithmetic Sequence")
        break
    else:
        if int(sequenceList[index+1]) - int(num) != commonDifference:
            print("Not an arithmetic sequence")
            break
else:
    print("Arithmetic Sequence")

def isSame(a, b, c):
    if a == b == c and a != "-":
        return True
    else:
        return False

def turnIndicator(turn):
    if turn % 2 == 1:
        return (1, "X")
    else:
        return (2, "O")

turn = 0

scanner = True

tictactoe = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

while True:
    currentTurn = turnIndicator(turn)[0]
    turn += 1
    print("Player", currentTurn, "chooses")
    coor = input("Enter the row, a space, and then the column. For example, if you wanted to place your X or O at row 2 column 1, you would enter \"2 1\": ")
    try:
        if tictactoe[int(coor[0])-1][int(coor[-1])-1] == "-":
            tictactoe[int(coor[0])-1][int(coor[-1])-1] = turnIndicator(turn)[1]
        else:
            print("Invalid coordinates. Please try again. ")
            turn -= 1
            continue
    except:
        print("Invalid coordinates. Please try again. ")
        turn -= 1
        continue

    #Part 2:

    for i in range(3):
        print(" ".join(tictactoe[i]))

    #["O", "x", "x"]
    #["O", "O", "-"]
    #["O", "-", "O"]

    for x in range(3): #0, 1, 2
        if isSame(tictactoe[0][x], tictactoe[1][x], tictactoe[2][x]): #Checking columns
            print("Player", currentTurn, "wins! ")
            exit()
        elif isSame(tictactoe[x][0], tictactoe[x][1], tictactoe[x][2]): #Checking rows
            print("Player", currentTurn, "wins! ")
            exit()
    if isSame(tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]): #Checking diagonal, \
        print("Player", currentTurn, "wins! ")
        exit()
    elif isSame(tictactoe[2][0], tictactoe[1][1], tictactoe[0][2]): #Checking other diagonal, /
        print("Player", currentTurn, "wins! ")
        exit()

    for a in tictactoe: #Checking status
        for b in a:
            if b == "-":
                scanner = False

    if scanner == True:
        print("Tie")
        exit()
    
    scanner = True

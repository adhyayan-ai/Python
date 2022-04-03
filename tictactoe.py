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
        turn += 1
        print("Player", turnIndicator(turn)[0], "chooses")
        coor = input("Enter the row, a space, and then the column. For example, if you wanted to place your X or O at row 2 column 1, you would enter \"2 1\": ")
        try:
            if tictactoe[int(coor[0])-1][int(coor[-1])-1] == "-":
                tictactoe[int(coor[0])-1][int(coor[-1])-1] = turnIndicator(turn)[1]
            else:
                print("Invalid coordiantes. Please try again. ")
                turn -= 1
                continue
        except:
            print("Invalid coordiantes. Please try again. ")
            turn -= 1
            continue
        for i in range(3):
            print(" ".join(tictactoe[i]))
        for x in range(3):
            if isSame(tictactoe[0][x], tictactoe[1][x], tictactoe[2][x]):
                print("Player", turnIndicator(turn)[0], "wins! ")
                exit()
            elif isSame(tictactoe[x][0], tictactoe[x][1], tictactoe[x][2]):
                print("Player", turnIndicator(turn)[0], "wins! ")
                exit()
            elif isSame(tictactoe[0][0], tictactoe[1][1], tictactoe[2][2]):
                print("Player", turnIndicator(turn)[0], "wins! ")
                exit()
            elif isSame(tictactoe[2][0], tictactoe[1][1], tictactoe[0][2]):
                print("Player", turnIndicator(turn)[0], "wins! ")
                exit()
            for a in tictactoe:
                for b in a:
                    if b == "-":
                        scanner = False
            if scanner == True:
                print("Tie")
                exit()
            
            scanner = True
    
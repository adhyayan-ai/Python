player1 = []
player2 = []
letters = "abcdefghi"
let2num = dict(zip(letters, [i + 1 for i in range(9)]))
num2let = dict(zip([i + 1 for i in range(9)], letters))
turn = 2

def horizontal(playerList):
    horizontalList = []
    for i in playerList:
        horizontalList.append(i[0])
    validation = let2num.get(horizontalList[0])
    for i in horizontalList:
        if let2num.get(i) == validation or let2num.get(i) - 1 == validation:
            validation = let2num.get(i)
        else:
            return False
    return True

def vertical(playerList):
    verticalList = []
    for i in playerList:
        verticalList.append(i[1])
    validation = int(verticalList[0])
    for i in verticalList:
        if int(i) == validation or int(i) - 1 == validation:
            validation = int(i)
        else:
            return False
    return True

player1List = input("Player 1, please enter your 5 adjacent ship nodes here (seperated by a space): ").strip(" ").split(" ")
if len(player1List) != 5:
    print("The length of your ship must be 5 nodes. Please try again. ")
    exit()

if not horizontal(player1List) or not vertical(player1List):
    print("Ship nodes are not connected ")
    exit()

for i in range(110):
    print()

player2List = input("Player 2, please enter your 5 adjacent ship nodes here (seperated by a space): ").strip(" ").split(" ")
if len(player2List) != 5:
    print("The length of your ship must be 5 nodes. Please try again. ")
    exit()

if not horizontal(player2List) or not vertical(player2List):
    print("Ship nodes are not connected ")
    exit()

for i in range(110):
    print()

player1Hits = 0
player2Hits = 0

def turnStep(turn):
    if turn == 1:
        return 2
    elif turn == 2:
        return 1
    else:
        return None

for i in range(9):
    player1.append([])
    player2.append([])
    for j in range(9):
        player1[i].append("- ")
        player2[i].append("- ")

while True:
    turn = turnStep(turn)
    print(f"It is player {turn}'s turn")
    coordinates = input("Enter your coordinates here (e.g. e6, or i8): ")
    if turn == 1: #If it's player1's turn.
        if coordinates in player2List:
            player2[let2num.get(coordinates[0]) - 1][int(coordinates[1]) - 1] = "H "
            player2Hits += 1
            print("Hit! ")
        else:
            player2[let2num.get(coordinates[0]) - 1][int(coordinates[1]) - 1] = "M "
            print("Miss! ")
    elif turn == 2: #If it's player2's turn.
        if coordinates in player1List:
            player1[let2num.get(coordinates[0]) - 1][int(coordinates[1]) - 1] = "H "
            player1Hits += 1
            print("Hit! ")
        else:
            player1[let2num.get(coordinates[0]) - 1][int(coordinates[1]) - 1] = "M "
            print("Miss! ")
    else: #Should not happen.
        print("Wha- ")
        exit()
    
    for i in eval("player" + str(turnStep(turn))):
        print("".join(i))
        print()

    if player1Hits == len(player1List):
        print("Player2 wins! ")
        break
    elif player2Hits == len(player2List):
        print("Player1 wins! ")
        break

#choice = input("Enter 1 to play against a freind. ENter 2 to play against the computer: ")
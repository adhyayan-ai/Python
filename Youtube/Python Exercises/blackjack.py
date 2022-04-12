import random

deck = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]*4
random.shuffle(deck)
#print(deck)

playerHand = []
dealerHand = []

def deal():
    return deck.pop(0)

def total(hand):
    isAce = False
    totalValue = 0
    for card in hand:
        if card != "A":
            totalValue += int(card)
        else:
            isAce = True
            totalValue += 11

    if totalValue > 21 and isAce:
        totalValue -= 10

    return totalValue

#Dealing:

playerHand.append(deal())
dealerHand.append(deal())
playerHand.append(deal())

while True:
    print(f"Dealer's hand:\n{', '.join(dealerHand)}\nTotal:{total(dealerHand)}\n")
    print(f"Player's hand:\n{', '.join(playerHand)}\nTotal:{total(playerHand)}\n")

    #Player's turn:

    action = input("Hit or stand? ")

    if action == "hit":
        playerHand.append(deal())
        print(f"You hit a {playerHand[-1]}\n")
    else:
        print("You stand. ")

    #Dealer's turn:

    if total(dealerHand) >= 17 and total(dealerHand) > total(playerHand):
        print("Dealer stands. ")
    else:
        dealerHand.append(deal())
        print(f"Dealer hit a {dealerHand[-1]}\n")

    #Bust:

    if total(playerHand) > 21:
        print("Bust! Dealer won!")
        break
    elif total(dealerHand) > 21:
        print("Bust! You won!")
        break

    #Winning:

    if total(playerHand) > total(dealerHand):
        print("You win! ")
        break
    elif total(dealerHand) > total(playerHand):
        print("Dealer wins! ")
        break
    else:
        print("Tie! ")
        break

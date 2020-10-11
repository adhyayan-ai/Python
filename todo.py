d1 = {"sunday": [], "monday": [], "tuesday": [], "wednesday": [], "thursday": [], "friday": [], "saturday": []}
running = True
while running:
    prompt = input("Prompt: What would you like to do today? ")
    prompt = prompt.upper()
    if prompt == "QUIT":
        print("Ending program...")
        running = False
    elif prompt == "ADD":
        DOW = input("What day of the week to you want to add to? ")
        DOW = DOW.lower()
        if not DOW in d1:
            if DOW == "quit":
                print("Ending program.. ")
                running = False
                continue
            print("Invalid day of the week. ")
            while not DOW.lower() in d1:
                DOW = input("What day of the week to you want to add to? ")
                DOW = DOW.lower()
                if DOW == "quit":
                    print('Type in "quit" again to exit the program. ')
                    break
                elif DOW.lower() in d1:
                    addvalue = input("What do you want to add to " + DOW + "? ")
                    d1.get(DOW).append(addvalue)
                    print("Successfully added", addvalue, "to", DOW)
                    break

                print("Invalid day of the week. ")
        else:
            addvalue = input("What do you want to add to " + DOW + "? ")
            d1.get(DOW).append(addvalue)
            print("Successfully added", addvalue, "to", DOW)
    elif prompt == "GET":
        DOW = input("What day of the week would you like to see? ")
        DOW = DOW.lower()
        if not DOW in d1:
            if DOW == "quit":
                running = False
                continue
            print("Invalid day of the week. ")
            while not DOW in d1:
                DOW = input("What day of the week to you want to see? ")
                if DOW == "quit":
                    print('Type in "quit" again to exit the program. ')
                    break
                print("Invalid day of the week. Please enter again. ")
                if DOW in d1:
                    print("You have to", ", and ".join(d1.get(DOW)))
        else:
            print("You have to", ", and ".join(d1.get(DOW)))
    
    elif prompt == "PRINT ALL":
        print(d1)
    
    elif prompt == "CHECK":
        DOW = input("What day of the week? ")
        DOW = DOW.lower()
        if not DOW in d1:
            if DOW == "quit":
                running = False
                continue
            print("Invalid day of the week. ")
            while not DOW in d1:
                DOW = input("What day of the week? ")
                if DOW == "quit":
                    print('Type in "quit" again to exit the program. ')
                    break
        else:
            print(DOW + "'s items: " + ", and ".join(d1.get(DOW)))
            checkItem = input("What you you want to check off? ")
            checkItem = checkItem.lower()
            if not checkItem in d1.get(DOW):
                if checkItem == "quit":
                    running = False
                    continue
                print("Invalid entry. " + '"' + checkItem + '"', "not in list. Please try again.")
                while not DOW.lower() in [i.lower() for i in d1.items()]:
                    DOW = input("What day of the week to you want to add to? ")
                    if DOW == "QUIT":
                        print('Type in "quit" again to exit the program. ')
                        break
                    elif DOW.lower() in [i.lower() for i in d1.keys()]:
                        (d1.get(DOW)).remove(checkItem)
                        print("Successfully removed", checkItem, "from list.")
            else:
                (d1.get(DOW)).remove(checkItem)
                print("Successfully removed", checkItem, "from list.")

    else:
        print('''Please enter "add" to add,
         "get" to get a value,
          "print all" to print out the whole dictionary,
           or enter "quit" to quit.
           Also, if you want to check off an item, type in "check" ''')
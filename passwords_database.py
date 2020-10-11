tries = 3



passwords = {"AVSingh": "Adhyayan", "JKumari": "Jyoti", "VKumar": "Vivek", "ASingh": "Amaira"}
names = {"AVSingh": "Adhyayan", "JKumari": "Jyoti", "VKumar": "Vivek", "ASingh": "Amaira"}
username = input("Enter your username here: ")
if not username in passwords:
    print("Invalid username. Please try again. ")
    exit()
else:
    pswd = passwords.get(username)
    while True:
        password = input(f"Welcome, {names.get(username)}, please enter your password here: ")
        if pswd == password:
            try:
                service = int(input(f"{names.get(username)}, how can I be at your service? Enter 1 to watch a video. Enter 2 to change your password. Enter 3 to log out."))
            except ValueError:
                print("Please enter a number only. Also, please re-enter your password. ")
                continue
            break
        else:
            print("Wrong password, please try again.")
            tries -= 1
            if tries == 0:
                print("I'm sorry, you ran out of tries. Please try again later. ")
                exit()
            continue


while True:
    try:
        service = int(input(f"{names.get(username)}, how can I be at your service? Enter 1 to watch a video. Enter 2 to change your password. Enter 3 to log out."))
    except ValueError:
        print("Please enter a number only. Also, please re-enter your password. ")
        continue
    if service < 4:
        if service == 1:
            print("https://tiny.cc/cocomelon-yo")
            break
        elif service == 2:
                pswd2 = input("Please enter your current password here: ")
                if pswd2 == pswd:
                    new_pswd = input("Enter you new password here: ")
                    passwords[username] = new_pswd
                    print("All done! You have successfully changed your password. ")
                else:
                    print(f"STOP! It is clear that you are not {username}. Please do this whole process again.")
                    exit()
        else:
            print("You chose to log out. have a good day!! ")
            exit()
    else:
        print("Please enter 1, 2, or 3 only. (For their respective purposes)")
        service = input("Enter 1 to watch a video. Enter 2 to change your password. Enter 3 to log out.")
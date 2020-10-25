class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Quiz:
    def __init__(self, qNADict={"test1": "ans1"}):
        self.questionAndAnswer = qNADict
        self.timer = None
    
    def evaluateQuizAnswer(self):
        ans = True
        if ans:
            return ans
        elif ans == False:
            return False

class QualifyingQuiz(Quiz):
    def __init__(self, qNADict={"test1": "ans1"}):
        self.questionAndAnswer = qNADict

class SurvivalQuiz(Quiz):
    def __init__(self, qNADict={"test2": "ans2"}):
        self.questionAndAnswer = qNADict

class GameWorld:
    time = 1
    user = ""

    def __init__(self, name='gameWorld', typeW='all', city='capitalCity'):
        self.worldName = name
        self.worldType = typeW
        self.capitalCity = city
        self.essentials = []
        self.qualifyingQuiz = QualifyingQuiz()
        self.survivalQuiz1 = SurvivalQuiz()
        self.survivalQuiz2 = SurvivalQuiz()

    def qualifyingQuizMethod(self, questionAndAnswer):
        questionsRight = 0
        for question in questionAndAnswer:
            answer = input(question[0] + "\n: ")
            if answer == question[1]:
                questionsRight += 1
            elif answer.capitalize() == "Quit":
                # User wants to Quit the Game now
                print(f"User wants to quit the game now")
                questionsRight = "Quit"
                break
        
        return questionsRight

    def survivalQuizMethod(self, questionAndAnswer):
        questionsRight = 1
        for question in questionAndAnswer:
            answer = input("Enter the letter of your answer: " + question[0] + "\n: ")
            if answer == question[1]:
                questionsRight *= 1
            elif answer != question[1]:
                questionsRight *= 0
            elif answer.capitalize() == "Quit":
                # User wants to Quit the Game now
                print(f"User wants to quit the game now")
                questionsRight = "Quit"
                break
        
        return questionsRight

    def timercounter(self):
        return 1

    def getEssentialList(self):
       #print(f"Reached {self.worldName}")
       #print(', '.join(self.essentials))
        return self.essentials

    def __str__(self):
        return self.worldName

class Nixoterra(GameWorld):
    #name = "Nixoterra"
    qNADictQ = {
    "What is the freezing point of snow?\n a. 0 degrees celcius\n b. 30 degrees celcius\n c. 100 degrees celcius\n d. -5 degrees celcius": "d",
    "Which ball do we use in the snow ball activity at snow world?\n a. Leather Ball\n b. Foot Ball\n c. Snow Ball\n d. All of the above": "d",
    "Which cartoon character does snow world has?\n a. Penguin\n b. Olaf\n c. Snowman\n d. All of the above": "d"
    }
    qNADictS1 = {
    "Describe a typical workweek for a snowboard instructor\n a. Sleep all week long\n b. Play with Ice\n c. Instruct and provide training to groups/individuals": "c",
    "what's your level of experience with edging, waxing and mounting skis and snowboard?\n a. Novice\n b. Proficient\n c. expert": "c"
    }
    
    qNADictS2 = {
    "What equipment is/are required for working as an experienced snowmaker\n a. Snow guns\n b. hoses\n c. hydrants\n d. All of the above": "d",
    "Can you safely lift 50 lbs\n a. Yes\n b. No": "a" 
    }    
    def __init__(self):
        self.worldName = "Nixoterra"
        self.worldType = "SnowWorld"
        self.essentials = ["Mittens", "Snowboots", "Ski Goggles", "Wool Socks", "Hand warmer"]
        #ToDo: Fill real name of cpital city
        self.capitalCity = "cNTerra"
        self.qualifyingQuiz = QualifyingQuiz(Nixoterra.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Nixoterra.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Nixoterra.qNADictS2)
    
class Silvia(GameWorld):
    #name = "Silvia"
    qNADictQ = {
    "Can you use a GPS device effectively?\n a. Yes\n b. No": "a",
    "Which of the following statement is true?\n a. Forest is on land\n; b. Forest is under water": "a",
    "What not to do in a Forest world?\n a. Start fire\n b. Climb on Tree\n c. Enjoy Nature": "a"
    }
    qNADictS1 = {
    "Name one of the heavy equipments used in the forest operations\n a. Dump trucks\n b. Toycar\n c. Teddybear": "a",
    "Which is NOT one of the 4 forest types?\n a. Temperate\n b. Tropical\n c. Subtropical\n d. Arboreal" : "d"
    }
    qNADictS2 = {
    "Forest soil is a natural water filter\n a. True\n b. False": "a",
    "What is the definition of a forest?\n a. A public green area in a town, used for recreation.\n b. An area rich in biodiversity\n c. A large area of land densely populated by trees\n d. A flat area covered in plants" : "c"
    }

    def __init__(self):
        self.worldName = "Silvia"
        self.worldType = "ForestWorld"
        self.essentials = ["Mosquito Repellent", "Backpack", "Poncho", "Hiking boots", "Trail shoes"]
        self.capitalCity = "cSilvia"
        self.qualifyingQuiz = QualifyingQuiz(Silvia.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Silvia.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Silvia.qNADictS2)

class Aquamundi(GameWorld):
    #name = "Aquamundi"
    qNADictQ = {
    "Spell Water\n a. Water\n b. Waiter": "a",
    "Is water same as wind?\n a.Yes\n b. No": "b",
    "Do you know how to swim?\n a. Yes\n b. No": "a"
    }
    qNADictS1 = {
    "Why do you want to be a Dive instructor?\n a. I like the word Instructor\n b. I love teaching diving": "b",
    "Do you have a Captain's license?\n a. Yes\n b. No": "a"
    }
    qNADictS2 = {
    "In case of any emergency call, what will be your first step?\n a. Ignore\n b. Immediately act on it" : "b",
    "What is a large natural stream of flowing water that ends in a sea?\n a. Lake\n b. Ocean\n c. Glacier\n d. River" : "d"
    }

    def __init__(self):
        self.worldName = "Aquamundi"
        self.worldType = "WaterWorld"
        self.capitalCity = "cAMundi"
        self.essentials = ["Swimcap", "Bandana", "Float suit", "Rash guard", "Alternate Air Source"]
        self.qualifyingQuiz = QualifyingQuiz(Aquamundi.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Aquamundi.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Aquamundi.qNADictS2)

class Montelocus(GameWorld):
    #name = "Montelocus"
    qNADictQ = {
    "Do you know how to use mountain gear?\n a. Yes\n b. No": "a",
    "Are you a wayfinder or a lost sheep?\n a. Wayfinder\n b. Lostsheep": "a",
    "Are you afraid of heights?\n a. Yes\n b. No": "b"
    }
    qNADictS1 = {
    "What would you select to climb in tricky mountain conditions?\n a. Mountaineering boots\n  b. mountains": "a",
    "What would you do if someone calls for help?\n a. It's their problem, I will just ignore\n b. Go and help them": "b"
    }

    qNADictS2 = {
    "Which of the following is the highest part of a mountain?\n a. Peak\n  b. Base\n c. Slope\n d. None of the above": "a",
    "What should you do if you fall off a mountain during Climbing?\n a. Have a quick snack\n b. Make a quick phone call\n c. Take a selfie and post it on instagram\n d. Use a harness": "d"
    }
    def __init__(self):
        self.worldName = "Montelocus"
        self.worldType = "MountainWorld"
        self.capitalCity = "cMlocus"
        self.essentials = ["Climbing Helmet", "Ropes", "Harness", "Mountaineering Boots", "Crampons"]
        self.qualifyingQuiz = QualifyingQuiz(Montelocus.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Montelocus.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Montelocus.qNADictS2)

class User:
    def __init__(self, name, location, system, coins=100):
        self.name = name
        self.location = location
        # not sure if we need it
        self.system = system
        self.coins = coins
        self.gems = 0
        self.assets = []

    def collectGem(self):
        self.gems += 1

    def buyGem(self, amount):
        returnVal = False
        if self.spendCoin(amount=25):
            self.gems += 1
            returnVal = True
        
        return returnVal

    def earnCoin(self, amount):
        self.coins += amount

    def spendCoin(self, amount):
        returnVal = False
        if self.coins >= amount:
            self.coins -= amount
            returnVal = True

        return returnVal

    def getCoins(self):
        return self.coins

    def getGems(self):
        return self.gems

    def buyEssentials(self, amount=5):
        ls = self.location.getEssentialList()
        #print("\n".join(ls))
        outputList = [str(i+1) + ". " + ls[i] for i in range(len(ls))]
        print("\n".join(outputList))
        sizeEssentialList = len(ls)
        essentialsList = []

        #print(f"Currently, Player has {', '.join(self.assets)} in his essentialList")
        choices = input("Input your selection as numbers 1, 2, 3, 4, or 5 separated by comma: ")
        if choices.capitalize() == "Quit":
            #print("Quit")
            # User input "Quit" at this stage. So, just quit the game.
            #self.quitGame()
            return choices
        
        choices = choices.split(',')

        try:
            # Convert input to integer for index in essentialList item
            choices = [int(i) for i in choices]
        except ValueError:
            # If input is not a number, Quit gracefully!
            print("Input is not a number. Quit")
            return essentialsList

        if max(choices) > sizeEssentialList:
            print(f"Invalid input! Input is not in essentialList")
            return essentialsList

        for j in choices:
            if self.spendCoin(amount):
                essentialsList.append(ls[j-1])
            else:
                print(f"You don't have enough money to buy {j}. You only have {self.coins} coins left.")
                break
        self.assets = essentialsList
        print(f"Currently, Player has {', '.join(self.assets)} in their essentialList")

        return self.assets

    def getAssets(self):
        return self.assets

    def takeSurvivalQuiz(self, quiz):
        if quiz == 'survivalQuiz1':
            userSurvival = [(i, self.location.survivalQuiz1.questionAndAnswer.get(i)) for i in self.location.survivalQuiz1.questionAndAnswer.keys()]
        elif quiz == 'survivalQuiz2':
            userSurvival = [(i, self.location.survivalQuiz2.questionAndAnswer.get(i)) for i in self.location.survivalQuiz2.questionAndAnswer.keys()]
        else: 
            # Wrong argument, should not have reached here. Return anyway!
            userSurvival = "Quit"
        survivalResults = self.location.survivalQuizMethod(userSurvival)
        return survivalResults

    def navigateToCapitalcity(self, amount=20):
        navSuccess = False
        if self.spendCoin(amount):
            self.gems += 1
            navSuccess = True
        return navSuccess
        

    # not sure if we need it.
    def quitGame(self):
        self.system.gameQuit(self.name)

    #def quit(self):
    #    exit()PINK

   #def buyTime(self):
   #    return 1

class GameSystem:
   
    def __init__(self, state=False):
        self.gameQuitted = state
        self.coins = 100
        self.name = "Gateway To Adventure"
        self.minCorrectAnswers = 1
        self.minGems = 4
        self.minCoins = 25
        self.minGemCapitalCity = 2
        self.buyGemAmount = 25
        self.minEssentials = 3
        self.maxAssetNum = 5
        self.survivalWinCoins = 10

    def gameStart(self):        
        #if userLocation.capitalize() in ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]:
        #    userQualifying = [(i, eval(userLocation).qualifyingQuiz.questionAndAnswer.get(i)) for i in eval(userLocation).qualifyingQuiz.questionAndAnswer.keys()]
        #    userLocation = eval(userLocation)
                
        print(f"{bcolors.OKGREEN}Hello, and welcome to {bcolors.BOLD}Gateway of Adventure!{bcolors.ENDC}") 
        userName = input(f"{bcolors.OKBLUE}What is your name? {bcolors.ENDC}")
        validInput = False
        gameReturn = False
        
        while validInput is False:
            userLocation = input(f"{bcolors.YELLOW}Choose a world from the following: {bcolors.BOLD}Nixoterra, Silvia, Aquamundi, or Montelocus : {bcolors.ENDC}")
            if userLocation.capitalize() in ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]:
                validInput = True
            else:
                if userLocation.capitalize() == "Quit":
                    validInput = True
                else:
                    print(f"Invalid world name! Please enter a correct World Name")
                    validInput = False
        if userLocation.capitalize() == "Quit":
            self.gameQuit(userName)
            return gameReturn
        
        # Valid User Location found
        # Let's do the Qualifying quiz
        # Let's initialize Classes for World
        if userLocation.capitalize() == "Nixoterra":
            world = Nixoterra()
        elif userLocation.capitalize() == "Silvia":
            world = Silvia()
        elif userLocation.capitalize() == "Aquamundi":
            world = Aquamundi()
        elif userLocation.capitalize() == "Montelocus":
            world = Montelocus()
        else:
            # Should not have reached here!
            self.gameQuit(userName)
            return gameReturn

        userQualifying = [(i, world.qualifyingQuiz.questionAndAnswer.get(i)) for i in world.qualifyingQuiz.questionAndAnswer.keys()]
        qualifyingResults = world.qualifyingQuizMethod(userQualifying)

        print(f"{bcolors.OKGREEN}{userName}, you got {qualifyingResults} questions right. {bcolors.ENDC}")
        
        if str(qualifyingResults).capitalize() == "Quit":
            self.gameQuit(userName)
            return False

        if qualifyingResults < self.minCorrectAnswers:
            # User failed the qualifying quiz
            # Exit the game already :)
            print(f"{bcolors.FAIL}You failed. {bcolors.ENDC}")
            self.gameExit(userName)
            return gameReturn

        # User Qualified the quiz for the world
        # Let's initialize Classes for World and player

        player = User(userName, world, self)

        print(f"worldName: {world.worldName}\nworldType: {world.worldType}\nessentials: {world.getEssentialList()}\n")

        print(f"Player Name: {player.name}\nPlayer Location: {player.location}\nPlayer Coins: {player.getCoins()}\nPlayer Gems: {player.getGems()}\n" )

        essentialsList = player.buyEssentials()

        if not essentialsList:
            # No item selected from the essential list
            # Player can't survive in the world
            # Exit the world with message
            print(f"{bcolors.FAIL}Quitting as {userName} didn't select any essential items to enter the new world.{bcolors.ENDC}")
            self.gameQuit(userName)
            return gameReturn               

        if essentialsList == "Quit":
            self.gameQuit(userName)
            return gameReturn

        #essentialsList = ", ".join(essentialsList)
        print(f"{userName} Assets: ", player.getAssets())
        if len(player.getAssets()) < self.minEssentials:
            print(f"{bcolors.FAIL}You need to select at least {self.minEssentials} from the list.{bcolors.ENDC}")
            self.gameQuit(userName)
            return gameReturn

        print(f"Player current coins: {player.getCoins()}")
        #print(essentialsList)

        if player.buyGem(self.buyGemAmount):
            print(f"{userName} just bought one gem as they enter the world of {world.worldName}")
        
        gameReturn = True
        survival1Results = player.takeSurvivalQuiz('survivalQuiz1')

        if str(survival1Results).capitalize() == "Quit":
            self.gameQuit(userName)
            # User entered Quit exit the loop and return accordingly
            gameReturn = False
            return gameReturn

        if not survival1Results:
            print("You failed. ")
            if len(player.getAssets()) > self.minEssentials:
                survival1Results = player.takeSurvivalQuiz('survivalQuiz1')

                if str(survival1Results).capitalize() == "Quit":
                    self.gameQuit(userName)
                    # User entered Quit exit the loop and return accordingly
                    gameReturn = False

                if not survival1Results:
                    print("You failed again. ")
                else:
                    player.earnCoin(self.survivalWinCoins * survival1Results)
                    player.collectGem()
                    print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")        
        else:
            player.earnCoin(self.survivalWinCoins * survival1Results)
            player.collectGem()
            print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")
        
        survival2Results = player.takeSurvivalQuiz('survivalQuiz2')

        if str(survival2Results).capitalize() == "Quit":
            self.gameQuit(userName)
            # User entered Quit exit the loop and return accordingly
            gameReturn = False
            return gameReturn

        if not survival2Results:
            print("You failed. ")
            if len(player.getAssets()) > self.minEssentials:
                survival2Results = player.takeSurvivalQuiz('survivalQuiz2')

                if str(survival2Results).capitalize() == "Quit":
                    self.gameQuit(userName)
                    # User entered Quit exit the loop and return accordingly
                    gameReturn = False
                    return gameReturn

                if not survival2Results:
                    print("You failed again. ")
                else:
                    player.earnCoin(self.survivalWinCoins * survival2Results)
                    player.collectGem()
                    print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")        
        else:
            player.earnCoin(self.survivalWinCoins * survival2Results)
            player.collectGem()
            print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")

        # Navigate to Capital City  
        if player.getGems() >= self.minGemCapitalCity:
            print(f"{userName} has reached the capital city of {userLocation}")
            if len(player.getAssets()) == self.maxAssetNum :
                player.navigateToCapitalcity(10)
            else:
                player.navigateToCapitalcity()
            
            print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")
            
            response = input(f"Do you want to buy addditional Gem for 25 coins? (y/n) ").lower()
            if response == 'y':
                player.buyGem(25)
                print(f"user bought one gem")
            elif response == 'n':
                print(f"{userName} declined offer")
            else:
                print(f"Invalid argument!")

        # Check if Player has enough gems to win the game
        if player.getGems() >= self.minGems:
            # Check if Player has enough coins to win the game
            if player.getCoins() >= self.minCoins:
                print(f"player {userName} has {player.getCoins()} coins and {player.getGems()} gems!")
                print(f"Player {userName} Won!!")
            else:
                print(f"Player {userName} lost!!")
                print(f"Player {userName} has {player.getCoins()}")
                print(f"You needed {self.minCoins} coins to win the game!")
        else:
            print(f"Player {userName} lost!!")
            print(f"Player {userName} has {player.getCoins()}")
            print(f"You needed {self.minGems} gems to win the game!")
                
        return gameReturn

    def gameQuit(self, name):
        self.gameQuitted = True
        print(f"{bcolors.FAIL}Quitting as {name} wants to quit the game.{bcolors.ENDC}")
    
    def gameExit(self, name):
        print(f"{bcolors.FAIL}{name} failed in Qualifying quiz. {bcolors.ENDC}")
        print(f"{bcolors.FAIL}Exit the Game!{bcolors.ENDC}")

game = GameSystem()

game.gameStart()

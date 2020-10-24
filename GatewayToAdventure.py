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
    capitalCity: ""

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
        return questionsRight

    def survivalQuizMethod(self, questionAndAnswer):
        questionsRight = 0
        for question in questionAndAnswer:
            answer = input(question[0] + "\n: ")
            if answer == question[1]:
                questionsRight += 1
        return questionsRight

    def timercounter(self):
        return 1

    def getEssentialList(self):
        print(f"Reached {self.worldName}")
        print(''.join(self.essentials))
        return self.essentials

    def __str__(self):
        return self.worldName

class Nixoterra(GameWorld):
    #name = "Nixoterra"
    qNADictQ = {'testnq': 'ansnq'}
    qNADictS1 = {'testns1': 'ansns1'}
    qNADictS2 = {'testns2': 'ansns2'}
    def __init__(self):
        self.worldName = "Nixoterra"
        self.worldType = "SnowWorld"
        self.essentials = ["Plough", "Car"]
        self.qualifyingQuiz = QualifyingQuiz(Nixoterra.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Nixoterra.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Nixoterra.qNADictS2)
    
class Silvia(GameWorld):
    #name = "Silvia"
    qNADictQ = {'testsq': 'anssq'}
    qNADictS1 = {'testss1': 'ansss1'}
    qNADictS2 = {'testss2': 'ansss2'}
    def __init__(self):
        self.worldName = "Silvia"
        self.worldType = "ForestWorld"
        self.essentials = ["axe", "fire"]
        self.qualifyingQuiz = QualifyingQuiz(Silvia.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Silvia.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Silvia.qNADictS2)

class Aquamundi(GameWorld):
    #name = "Aquamundi"
    qNADictQ = {'testaq': 'ansaq'}
    qNADictS1 = {'testas1': 'ansas1'}
    qNADictS2 = {'testas2': 'ansas2'}
    def __init__(self):
        self.worldName = "Aquamundi"
        self.worldType = "WaterWorld"
        self.essentials = ["FishHunt", "LifeJacket", "snorkelKit"]
        self.qualifyingQuiz = QualifyingQuiz(Aquamundi.qNADictQ)
        self.survivalQuiz1 = SurvivalQuiz(Aquamundi.qNADictS1)
        self.survivalQuiz2 = SurvivalQuiz(Aquamundi.qNADictS2)

class Montelocus(GameWorld):
    #name = "Montelocus"
    qNADictQ = {'testmq': 'ansmq'}
    qNADictS1 = {'testms1': 'ansms1'}
    qNADictS2 = {'testms2': 'ansms2'}
    def __init__(self):
        self.worldName = "Montelocus"
        self.worldType = "MountainWorld"
        self.essentials = ["rope", "harness"]
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

    def buyGem(self):
        self.coins -= 25
        self.gems += 1

    def earnCoin(self, amount):
        self.coins += amount

    def spendCoin(self, amount):
        self.coins -= amount

    def getCoins(self):
        return self.coins

    def getGems(self):
        return self.gems

    def buyEssentials(self):
        ls = list(self.location.getEssentialList())
        print (ls)
        sizeEssentialList = len(ls)
        essentialsList = []

        print(f"Currently, Player has {', '.join(self.assets)} in his essentialList")
        choices = input("Input your selection as numbers 1, 2, 3, input your choices separated by comma: ")
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

        if max(choices) > len(ls):
            print(f"Invalid input! Input is not in essentialList")
            return essentialsList

        for j in choices:
            if self.coins >= 20:
                essentialsList.append(ls[j-1])
                self.spendCoin(amount=20)
            else:
                print(f"You don't have enough money to buy {j}. You only have {self.coins} coins left.")
                break
        self.assets = essentialsList
        print(f"Currently, Player has {', '.join(self.assets)} in his essentialList")

        return essentialsList

    def takeQuiz(self):
        self.takenQuiz = True

    def navigateToCapitalcity(self):
        self.gems += 1
        self.capitalcity = True

    # not sure if we need it.
    def quitGame(self):
        self.system.gameQuit(self.name)

    #def quit(self):
    #    exit()PINK

   #def buyTime(self):
   #    return 1

class GameSystem:
    coins = 100
    name = ""
    worldType = ""
    timer = 0
    gameQuitted = False
    minCorrectAnswers = 1
    minGems = 4
    minCoins = 100
    minGemCapitalCity = 3
   
    def __init__(self, state=False):
        self.gameQuitted = state

    def gameStart(self):        
        #if userLocation.capitalize() in ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]:
        #    userQualifying = [(i, eval(userLocation).qualifyingQuiz.questionAndAnswer.get(i)) for i in eval(userLocation).qualifyingQuiz.questionAndAnswer.keys()]
        #    userLocation = eval(userLocation)
                
        print(f"{bcolors.OKGREEN}Hello, and welcome to {bcolors.BOLD}Gateway of Adventure!{bcolors.ENDC}") 
        userName = input(f"{bcolors.OKBLUE}What is your name? {bcolors.ENDC}")
        validInput = False
        while (validInput is False):
            userLocation = input(f"{bcolors.YELLOW}Choose a world from the following: {bcolors.BOLD}Nixoterra, Silvia, Aquamundi, or Montelocus : {bcolors.ENDC}")
            if userLocation.capitalize() in ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]:
                validInput = True
            else:
                if userLocation.capitalize() == "Quit":
                    validInput = True
                else:
                    print(f"You input the wrong World Name")
                    validInput = False
        if userLocation.capitalize() == "Quit":
            self.gameQuit(userName)
            return
        
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
            return

        userQualifying = [(i, world.qualifyingQuiz.questionAndAnswer.get(i)) for i in world.qualifyingQuiz.questionAndAnswer.keys()]
        qualifyingResults = world.qualifyingQuizMethod(userQualifying)

        print(f"{bcolors.OKGREEN}{userName}, you got {qualifyingResults} questions right. {bcolors.ENDC}")
        if not qualifyingResults:
            # User failed the qualifying quiz
            # Exit the game already :)
            print(f"{bcolors.FAIL}You failed. {bcolors.ENDC}")
            self.gameExit(userName)
            return

        # User Qualified the quiz for the world
        # Let's initialize Classes for World and player
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
            return

        player = User(userName, world, self)

        print(f"worldName: {world.worldName} worldType: {world.worldType} essentials: {world.getEssentialList()}")

        print(f"Player Name: {player.name} Player Location: {player.location} Player Coins: {player.getCoins()} Player Gems: {player.getGems()}" )

        essentialsList = player.buyEssentials()

        if not essentialsList:
            # No item selected from essential list
            # Player can't survive in the world
            # Exit the world with message
            print(f"{bcolors.FAIL}Quitting as {userName} didn't select any essential items to enter the new world.{bcolors.ENDC}")
            self.gameQuit(userName)
            return                

        if essentialsList == "Quit":
            self.gameQuit(userName)
            return

        essentialsList = ", ".join(essentialsList)
        print(f"Player current coins: {player.getCoins()}")
        print(essentialsList)

        player.buyGem()
        
        while True:
            userSurvival1 = [(i, world.survivalQuiz1.questionAndAnswer.get(i)) for i in world.survivalQuiz1.questionAndAnswer.keys()]
            if userSurvival1[0][0].capitalize() == "Quit":
                self.gameQuit(userName)
                break

            survival1Results = world.qualifyingQuizMethod(userSurvival1)
            if not survival1Results:
                print("You failed. ")
            else:
                player.earnCoin(10 * survival1Results)
                if survival1Results >= self.minCorrectAnswers:
                    player.collectGem()
                print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")
            
            userSurvival2 = [(i, world.survivalQuiz2.questionAndAnswer.get(i)) for i in world.survivalQuiz2.questionAndAnswer.keys()]
            if userSurvival2[0][0].capitalize() == "Quit":
                self.gameQuit(userName)
                break

            survival2Results = world.qualifyingQuizMethod(userSurvival2)
            if not survival2Results:
                print("You failed. ")
            else:
                player.earnCoin(10 * survival2Results)
                if survival2Results >= self.minCorrectAnswers:
                    player.collectGem()
                print(f"Player current coins: {player.getCoins()} current Gems:{player.getGems()}")

            if player.getGems() >= self.minGemCapitalCity:
                player.navigateToCapitalcity()

            # Check if Player has enough gems to win the game
            if player.getGems() >= self.minGems:
                # Check if Player has enough coins to win the game
                if player.getCoins() >= self.minCoins:
                    print(f"Player Won!!")
                    break
                else:
                    print(f"Not enough Coins! /n Play more survival Quiz to get enough Coins")
            else:
                print(f"Not enough Gems! /n Play more survival Quiz to get more Gems")
                    
        return

    def gameQuit(self, name):
        self.gameQuitted = True
        print(f"{bcolors.FAIL}Quitting as {name} wants to quit the game.{bcolors.ENDC}")
    
    def gameExit(self, name):
        print(f"{bcolors.FAIL}{name} failed in Qualifying quiz. {bcolors.ENDC}")
        print(f"{bcolors.FAIL}Exit the Game!{bcolors.ENDC}")



game = GameSystem()

game.gameStart()
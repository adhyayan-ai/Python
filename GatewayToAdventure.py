class Quiz:
    def __init__(self):
        self.quiz = {}
        self.timer = None
    
    def evaluateQuizAnswer(self):
        ans = True
        if ans:
            return ans
        elif ans == False:
            return False

class QualifyingQuiz(Quiz):
    def __init__(self):
        self.questionAndAnswer = {"test1": "ans1"}

class SurvivalQuiz(Quiz):
    def __init__(self):
        self.questionAndAnswer = {"test2": "ans2"}


class GameWorld:
    worldName = ""
    worldType = ""
    time = 1
    user = ""
    essentials = ["Bum", "Dum"]
    capitalCity: ""
    survivalQuiz1 = SurvivalQuiz()
    survivalQuiz2 = SurvivalQuiz()
    qualifyingQuiz = QualifyingQuiz()

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
class Nixoterra(GameWorld):
    worldName = "Nixoterra"

class Silvia(GameWorld):
    worldName = "Silvia"

class Aquamundi(GameWorld):
    worldName = "Aquamundi"

class Montelocus(GameWorld):
    worldName = "Montelocus"

class User:
    name = ""
    location = ""
    coin = 0
    gem = 0
    asset: []

    def collectGem(self):
        self.getCollected = True

    def buyGem(self):
        return 1

    def earnCoin(self, amount):
        self += amount

    def spendCoin(self, amount):
        self -= amount

    def buyEssentials(self, location, joinSym):
        ls = location.essentials
        essentialsList = []
        print(joinSym.join(ls))
        numbers = input("Do seperated by comma: ").lower().split(joinSym)
        if numbers == ["q", "u", "i", "t"]:
            print("Quit")
            return False
        for i in numbers:
            numbers[numbers.index(i)] = int(i)

        for j in numbers:
            essentialsList.append(ls[j-1])
            if GameSystem.coins > 0:
                User.spendCoin(self=GameSystem.coins, amount=20)
            else:
                print("You don't have enough money to buy {i}. You only have {currency} coins left.")
                break

        return essentialsList

    def takeQuiz(self):
        self.takenQuiz = True

    def navigateToCapitalcity(self):
        self.capitalcity = True

    #def quit(self):
    #    exit()

   #def buyTime(self):
   #    return 1

class GameSystem:
    coins = 100
    name = ""
    worldType = ""
    timer = 0
    

    def gameStart(self):
        userName = input("Hello, and welcome to Gateway of Adventure! What is your name? ")
        userLocation = input("Choose a world from the following: Nixoterra, Silvia, Aquamundi, or Monteocus: ")
        if userLocation.capitalize() in ["Nixoterra", "Silvia", "Aquamundi", "Montelocus"]:
            userQualifying = [(i, eval(userLocation).qualifyingQuiz.questionAndAnswer.get(i)) for i in eval(userLocation).qualifyingQuiz.questionAndAnswer.keys()]
            userLocation = eval(userLocation)
        qualifyingResults = userLocation.qualifyingQuizMethod(userQualifying, userQualifying)
        print(f"{userName}, you got {qualifyingResults} questions right. ")
        while True:
            if not qualifyingResults:
                print("You failed. ")
                break
            else:
                essentialsList = ", ".join(User.buyEssentials(self="hi", location=userLocation, joinSym=", "))
                print(GameSystem.coins)
                if not essentialsList:
                    break
                else:
                    print(essentialsList)
                    userSurvival1 = [(i, eval(userLocation).survivalQuiz1.questionAndAnswer.get(i)) for i in eval(userLocation).survivalQuiz1.questionAndAnswer.keys()]
                    survival1Results = userLocation.qualifyingQuizMethod(userSurvival1, userSurvival1)
                    if not qualifyingResults:
                        print("You failed. ")
                        break
                    else:
                        User.earnCoin(GameSystem.coins, 10 * survival1Results)

    def gameQuit(self):
        self.gameQuitted = True

GameSystem.gameStart("Test")
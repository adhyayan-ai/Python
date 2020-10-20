import sys
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
        self.questionAndAnswer = {}

class SurvivalQuiz(Quiz):
    def __init__(self):
        self.questionAndAnswer = {}


class GameWorld:
    worldName = ""
    worldType = ""
    time = 1
    user = ""
    essentials = []
    capitalCity: ""
    survivalQuiz = SurvivalQuiz()
    survivalQuiz2 = SurvivalQuiz()
    qualifyingQuiz: QualifyingQuiz()

    def initializeQuiz(self, questionAndAnswer):
        questionsRight = 0
        for question in questionAndAnswer:
            answer = input(question[0])
            if answer == question[1]:
                questionsRight += 1
        return questionsRight

    def survivalQuizMethod(self):
        self.survival = True

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

    def earnCoin(self):
        return 1

    def buyEssentials(self):
        return 1

    def takeQuiz(self):
        self.takenQuiz = True

    def navigateToCapitalcity(self):
        self.capitalcity = True

    def quit(self):
        exit()

    def buyTime(self):
        return 1

class GameSystem:
    name = ""
    worldType = ""
    timer = 0
    
    def qualifyingQuiz(self):
        self.qualify = True

    def gameStart(self):
        self.gameStarted = True

    def gameQuit(self):
        self.gameQuitted = True

def convertName(classStr):
    return getattr(sys.modules[__name__], classStr)

userName = input("Hello, and welcome to Gateway of Adventure! What is your name? ")
userLocation = input("Choose a world from the following: Nixoterra, Silvia, Aquamundi, or Monteocus. ")
userQualifying = [(i, convertName(userName).qualifyingQuiz.questionAndAnswer.get(i)) for i in convertName(userName).qualifyingQuiz.questionAndAnswer.keys()]
GameWorld.initializeQuiz(userQualifying)

import re

girlNames = re.split('(?=[A-Z])', 'EmmaIsabellaOliviaSophiaMiaAvaEmilyEvelynAmeliaCharlotteScarlettVictoriaSofiaPenelopeAbigailCamilaHarperMilaAriaLunaElizabethMadisonAveryXimenaLilyElenaAddisonZoeyEllaGraceNatalieAuroraGenesisRileyLaylaVioletAaliyahPaisleyBrooklynLillianMelanieSamanthaChloeQuinnEllieAriannaAubreyAllisonSavannahValentinaZoeKinsleyAudreyLeilaniHannahHazelMayaAlexaArianaStellaLucyNoraLeahGiannaKennedyNevaehBellaDelilahNataliaAliceClaireRubyBrielleElianaJadeHaileyEmiliaEverlyLilianaSerenityNaomiAthenaMadelynMariaSarahGabriellaJocelynWillowAnnaKayleeArielDaleyzaEleanorCoraAdelineIsabelleSadieRyleeAryaIvy')[1:]
boyNames = re.split('(?=[A-Z])', "LiamNoahSebastianAlexanderDanielOliverJulianBenjaminLoganElijahEthanMichaelAidenJamesMateoJacobSantiagoIsaacLukeMasonAdrianAngelJosephLucasMatthewWyattIsaiahJacksonGabrielWilliamJaydenDavidSamuelChristopherJoseEzekielJonathanHenryDylanLuisAnthonyLincolnJesusAndrewCarterChristianXavierAaronEliEzraJoshuaLeviDominicEliasGraysonAsherCalebNathanJosiahIanOwenHunterJackJaxonJohn RyanLeonardoDamianCarlosEastonJuanLeoJeremiahAdamLandonRobertHudsonCarsonDiegoNathanielCharlesTheodoreMiguelAdrielGiovanniMaverickEvanBraydenConnorJordanAustinThomasAydenFranciscoAxelEmilianoJamesonAbelAlejandroGael")[1:]
gender = input("Enter \"boy\" for male names and \"girl\" for female ones: ")
index = -1
finalList = []
letters = input("What letter(s) do you want your name to begin with? ")

def letterFilter(word):
    if word[0:len(letters)] == letters.capitalize():
        return True
    else:
        return False

while True:
    index += 1

    if gender.lower() == "boy":
        boyNames = list(filter(letterFilter, boyNames))
        if index + 1 <= len(boyNames):
            prompt = input(f"Name: {boyNames[index]}. \nSay next to move to the next name or say back to go back to the previous name. Say add to add {boyNames[index]} to your final list. Say done to end: ")
            if prompt.lower() == "next":
                continue
            elif prompt.lower() == "back":
                index -= 2
                continue
            elif prompt.lower() == "add":
                finalList.append(boyNames[index])
            elif prompt.lower() == "done":
                break
            else:
                print("Please enter only next, back, add, or done.")
                index -= 1
                continue
        else:
            break

    elif gender.lower() == "girl":
        girlNames = list(filter(letterFilter, girlNames))
        if index + 1 <= len(girlNames):
            prompt = input(f"Name: {girlNames[index]}. \nSay next to move to the next name or say back to go back to the previous name. Say add to add {girlNames[index]} to your final list. Say done to end: ")
            if prompt.lower() == "next":
                continue
            elif prompt.lower() == "back":
                index -= 2
                continue
            elif prompt.lower() == "add":
                finalList.append(girlNames[index])
            elif prompt.lower() == "done":
                break
            else:
                print("Please enter only next, back, add, or done.")
                index -= 1
                continue
        else:
            break

    else:
        print("Please type in either girl or boy. Try again. ")
        exit()

printList = "".join(["\n" + str(finalList.index(i) + 1) + ". " + i for i in finalList])
print(f"Thank you for using this script! Your final list is: {printList}" if len(finalList) > 0 else "I'm sorry that you couldn't find any name you wanted. We keep updating our list frequently, so do come back later and use this script! Thank you!")
print("I hope you can decide on a final name for your baby! Good Luck! :)")
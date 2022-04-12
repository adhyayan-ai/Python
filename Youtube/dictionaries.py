#text = input("Enter your message here: ")
AcronymDict = {"Laughing out loud": "LOL", "Oh my god": "OMG"}

#for i in AcronymDict.keys():
#    if i in text:
#        text = text.replace(i, AcronymDict[i])

#print(text)
``
for key, value in AcronymDict.items():
    print(key, "is the long version of", value)
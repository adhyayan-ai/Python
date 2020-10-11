inputs = []
count = 0
q = ["Noun: ", 'Present-tense verb: ', 'Present-tense verb: ', "Noun: ", "Adjective: ", "Gender: ", "Adverb: ", "Noun: ", "Past-tense verb: ", "Big number: ", "Present-tense verb: ", "Your favorite color: ", "A period of time: ", "Adverb: ", "Exclamation: "]
for i in q:
    j = input(i)
    j = j.lower()
    if j == "quit":
        print("Thanks for playing!")
        exit()
    else:
        inputs.append(j)
inputs[-1] = inputs[-1].upper()
print(f"Today, our class went to a field trip to see the grand {inputs[0]}. My classmate Peter {inputs[1]}ed his way out of the museum because he wanted to {inputs[2]} the {inputs[3]}. My teacher was a very {inputs[4]} {inputs[5]}. I {inputs[6]} ran over to see the {inputs[7]}. Our teacher told us that the {inputs[7]} {inputs[8]} {inputs[9]} years ago. I really wanted to {inputs[10]} on the {inputs[11]} {inputs[7]}. It felt like {inputs[12]}, but my teacher finally told us we can go home. When I woke up the next morning, I {inputs[13]} ran over to the bathroom and found the {inputs[7]} sitting on my toilet seat. {inputs[14]}, I said! This was the craziest day of my life!")
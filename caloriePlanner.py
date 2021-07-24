#greet
print("Welcome! To calculate your weigjt loss plan, I need your weight, height and age. Please be honest for the best results. ")

#wieght, height, and age
weight = float(input("Enter your weight in pounds: "))/2.205
height = float(input("Enter your height in inches: "))*2.5
age = int(input("Please enter your age: "))

bmr = 10*weight+6.25*height-age*5+5

activity = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9,
}

activityFactor = activity[int(input("""How active are you?

                                    1. Little or no exercise
                                    2. A little bit of exercise (light activity)
                                    3. Moderate exercise (some exercise almost every day of the week)
                                    4. Hard exercise (quite intense exercise every day)
                                    5. Extreme Exercise (very streenuous exercise at least twice a day) """))]

burnedPerDay = bmr*activityFactor

burnGoal = float(input("How many pounds do you wish to lose per week (please be realisitic.)? "))/7*3500
eatenPerDay = burnedPerDay-burnGoal

print(f"You should aim to eat {eatenPerDay:.2f} calories per day. Remember, it's not all about calories and you should maintain a good balance of carbs, protein, and fat. Additionally, always consult yoru doctor before burning a signifcant amount of weight. Thank you for using this tool.")
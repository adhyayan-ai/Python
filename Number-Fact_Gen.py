numbers = input("Enter yout list of number seperated by spaces: ")

n = numbers.split(" ")

#n = [1, 190, 29, -3, 299002]

print("Your list is:", n)

length = len(n)

l = int(n[0])

s = int(n[0])

for a in n:
   a = int(a)
   if l < a :
      l = a
      print(l)


   if s > a :
      s = a
      print(s)

def state_facts(x):

   if length < 5:
      print("Your list lenth was only", length,", try entering a longer list!")
   elif length >= 5 and length < 10:
      print("Your list length was a good", length, "numbers!")
   elif length >= 10 and length <= 20:
      print("Your list contained a whopping", length, "long! Wow")
   elif length > 20:
      print("YOUR LIST CONTAINED", length, "NUMBERS?!?! UNBELIEVABLE! Thanks for taking the time and effort to write all of that. :)")
   else:
      print("Lol this statement's never gonna get printed")

   print("The first number that you entered was:", n[0])

   print("The last number that you entered was:", n[-1])

   print("Your Maximum is:", l)

   print("Your Minimum is:", s)
   
   print("Note:", x)

state_facts("Well, I guess that was it.")





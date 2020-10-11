#Class 4: Functions

#Functions are a specific set of code stored inside a single functioned defined by you, the developer. 
#For example, you can define a function called myFunction(), inside where we will put the code associated with function.
#Have a look at the sample code below:

def myFunction(): #We use "def" to define a function.
    print("Hello")

#myFunction() #Let us now call this function my typing in its name.

#As you can see, the output is "Hello".

n = int(input("Enter number here: "))

def countdown(number):
    for i in range(number+1, 1, -1):
        print(i)
    print("Go!")

countdown
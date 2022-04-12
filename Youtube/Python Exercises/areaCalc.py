import math

def circle(radius):
    return round(radius**2*math.pi, 3)

def square(side):
    return side**2

def triangle(base, height):
    return base*height*0.5

def rectangle(length, width):
    return length*width

while True:

    shape = input("Enter a shape: ")

    if shape.lower() == "circle":
        try:
            radius = int(input("What is the radius? "))
        except:
            raise Exception("Please enter a number")

        print(circle(radius))

    elif shape.lower() == "square":
        try:
            side = int(input("What is the side length? "))
        except:
            raise Exception("Please enter a number")

        print(square(side))

    elif shape.lower() == "triangle":
        try:
            base = int(input("What is the base? ")) #3 #three
            height = int(input("What about the height? "))
        except:
            raise Exception("Please enter a number")

        print(triangle(base, height))

    elif shape.lower() == "rectangle":
        try:
            length = int(input("What is the length? "))
            width = int(input("What is the width? "))
        except:
            raise Exception("Please enter only a number")

        print(rectangle(length, width))

    elif shape.lower() == "done":
        break

    else:
        print("Please enter either Circle, Square, Triangle, or Rectangle") 

print("Thank you for using this calculator! ")
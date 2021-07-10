from tkinter import *
import tkinter.ttk 

root = Tk()
root.title("EasyHomework Prototype")
root.geometry("600x500")
root.configure(background='#81d4fa')
root.iconphoto(False, PhotoImage(file='TKinter/cong_app_icon.png'))

daysOfTheWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
calendarButton = Button(root, text="Calendar")
calendarButton.grid(column=2, row=0, columnspan=2, pady="10")

gradesButton = Button(root, text="Grades", bg="white")
gradesButton.grid(column=3, row=0, columnspan=2, pady="10")

def addAssignment():

    def done():
        assignmentMenu.destroy()

    packCounter = 3

    def packName():
        nonlocal packCounter
        Label(assignmentMenu, text=f"Assignment {assignmentName.get()} added!").grid(row=packCounter, column=0)
        packCounter += 1

    assignmentMenu = Toplevel(bg="white")

    doneButton = Button(assignmentMenu, text="DONE", bg="#81d4fa", fg="white", command=done)
    doneButton.grid(row=2, column=0)

    assignmentName = Entry(assignmentMenu)
    assignmentName.grid(row=0, column=0)

    namePacker = Button(assignmentMenu, text="Print Assignment Name", command=packName)
    namePacker.grid(row=1, column=0)

    assignmentMenu.mainloop

addButton = Button(root, text="+", command=addAssignment, bg="white")
addButton.grid(column=9, row=0)

for seperatorCount in range(1, 8):
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=seperatorCount, row=1, rowspan=10, ipady=200, sticky="nw", pady=35, ipadx="1")

for i, day in zip(range(7), daysOfTheWeek):
    Label(root, text=f"{day}", bg="#81d4fa", fg="white", font="Helvetica 12 bold").grid(column=i, row=1, padx="17", ipadx="2", ipady="20")

root.mainloop()

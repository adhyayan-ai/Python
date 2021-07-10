from tkinter import *
import tkinter.ttk 

root = Tk()
root.title("EasyHomework Prototype")
root.geometry("570x500")
root.configure(background='#81d4fa')
root.iconphoto(False, PhotoImage(file='TKinter/cong_app_icon.png'))

daysOfTheWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
calendarLabel = Button(root, text="Calendar")
calendarLabel.grid(column=2, row=0, columnspan=2, pady="10")

gradesLabel = Button(root, text="Grades", bg="white")
gradesLabel.grid(column=3, row=0, columnspan=2, pady="10")

for seperatorCount in range(1, 8):
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=seperatorCount, row=1, rowspan=10, ipady=200, sticky="nw", pady=35, ipadx="1")

for i, day in zip(range(7), daysOfTheWeek):
    Label(root, text=f"{day}", bg="#81d4fa", fg="white", font="Helvetica 12 bold").grid(column=i, row=1, padx="17", ipadx="2", ipady="20")

root.mainloop()
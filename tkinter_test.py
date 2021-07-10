from tkinter import *

root = Tk()
root.title("EasyHomework Prototype")
root.geometry("500x500")
root.configure(background='#81d4fa')
root.iconphoto(False, PhotoImage(file='TKinter/cong_app_icon.png'))

myLabel = Label(root, text="Hello World", bg="#81d4fa", fg="white", font="Helvetica 18 bold", pady="10")
myLabel.grid()

def on_enter(e):
   print("Entered")
   mainButton.config(highlightbackground="green")

def on_leave(e):
   mainButton.config(highlightbackground="yellow")

mainButton = Button(root, text="Home", bd="2", fg="#81d4fa", font="Helvetica 18 bold", bg="white")
mainButton.grid()

mainButton.bind("<Enter>", on_enter)
mainButton.bind("<Leave>", on_leave)

root.mainloop()
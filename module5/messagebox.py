from tkinter import *
from tkinter import messagebox
window = Tk()

def clickme():
    messagebox.showinfo("you just clicked me")

button = Button(window , text = "click here" , command= clickme)
button.place(x =75 , y = 100)
window.mainloop()
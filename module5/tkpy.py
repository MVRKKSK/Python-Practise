from tkinter import *
window = Tk()
def sell():
    selection=f"here are your fries{var.get()}"
    Label.config(text=selection)

var = StringVar()

r1 = Radiobutton(window,text="pizza slice" ,  variable= var, value="pizza" , command = sell)
r2 = Radiobutton(window,text="burger"  ,  variable= var, value="burger" , command = sell)
r3 = Radiobutton(window,text="fries"  ,  variable= var, value="fries" , command = sell)


r1.pack()
r2.pack()
r3.pack()
Label = Label(window)
Label.pack()
window.mainloop()
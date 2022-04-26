from tkinter import *
window = Tk()
window.geometry("500x100")
spin = Spinbox(window , from_=0 , to = 100000)
spin.pack()
window.mainloop()
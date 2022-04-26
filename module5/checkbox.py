from tkinter import *
window = Tk()

checkVar1 = IntVar()
checkVar2 = IntVar()

c1 = Checkbutton(window, text="male" , variable = checkVar1 , onvalue = 1 , offvalue =0 , height=25 , width = 25)
c2 = Checkbutton(window, text="female" , variable = checkVar2 , onvalue = 1 , offvalue =0 , height=25 , width = 25)

c1.pack()
c2.pack()
window.mainloop()
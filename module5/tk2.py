from tkinter import *
import tkinter as tk
window = tk.Tk()

def mhello():
    lable1 = tk.Label(window , text = txt_entry.get()).pack()

window.geometry("350x150")

window.title("python is a master language")
lbl_sample = tk.Label(window , text="please click on button").pack()

txt_entry = Entry(window)

txt_entry.pack()

btn_sample = tk.Button(window , text="click me now" , command=mhello , fg = "red").pack()

window.mainloop()


import tkinter as tk
window = tk.Tk()
window.geometry("300x150")
tk.Label(text="this is a simplest code" , background = "blue").pack()
lbl_sample = tk.Label(window , text="Label")
btn_sample = tk.Button(window, text = "Button")
txt_entry = tk.Entry(window)

lbl_sample.pack()
txt_entry.pack()
btn_sample.pack()




window.mainloop()
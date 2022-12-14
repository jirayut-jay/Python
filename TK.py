import tkinter as tk

window = tk.Tk()
window.title("TestPython")
window.minsize(width=400,height=400)

title_label = tk.Label(master=window,text="Username")
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window,text="Login")
ok_button.pack()

window.mainloop()
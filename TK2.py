import tkinter as tk

def set_start():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('Python')
window.minsize(width=300,height=300)

title_label = tk.Label(master=window, text = "Hello")
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window,text="Start",command=set_start)
ok_button.pack()


window.mainloop()
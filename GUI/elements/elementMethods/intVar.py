from tkinter import *

def click_button():
    clicks.set(clicks.get() + 1)


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

clicks = IntVar()
clicks.set(0)

btn = Button(textvariable=clicks,
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="Verdana 15",
             command=click_button)
btn.pack()

root.mainloop()
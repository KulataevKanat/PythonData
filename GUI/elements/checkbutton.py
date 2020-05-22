from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

python_lang = IntVar()
python_checkbutton = Checkbutton(
    text="Python",
    variable=python_lang,
    onvalue=1,
    offvalue=0,
    padx=15,
    pady=10
)
python_checkbutton.grid(
    row=0,
    column=0,
    sticky=W
)

java_lang = IntVar()
java_checkbutton = Checkbutton(
    text="Java",
    variable=java_lang,
    onvalue=1,
    offvalue=0,
    padx=15,
    pady=10
)
java_checkbutton.grid(
    row=1,
    column=0,
    sticky=W
)

root.mainloop()

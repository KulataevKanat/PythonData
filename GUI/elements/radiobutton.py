from tkinter import *

languages = [
    ("Python", 1),
    ("JavaScript", 2),
    ("TypeScript", 3),
    ("Java", 4)
]


def select():
    l = language.get()
    if l == 1:
        sel.config(text="Выбран Python")
    elif l == 2:
        sel.config(text="Выбран JavaScript")
    elif l == 3:
        sel.config(text="Выбран TypeScript")
    elif l == 4:
        sel.config(text="Выбран Java")


root = Tk()
root.title("GUI на Python")
root.geometry("500x500")

header = Label(text="Выберите язык",
               padx=15,
               pady=10
               )
header.grid(row=0,
            column=0,
            sticky=W
            )

language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt,
                value=val,
                variable=language,
                padx=15,
                pady=10,
                command=select) \
        .grid(row=row,
              sticky=W
              )
    row += 1

sel = Label(padx=15,
            pady=10
            )
sel.grid(row=row,
         sticky=W
         )

root.mainloop()

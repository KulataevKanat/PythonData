from tkinter import *

languages = [
    "Python",
    "JavaScript",
    "C#",
    "Java"
]

root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

languages_listbox = Listbox()

for language in languages:
    languages_listbox.insert(END,
                             language
                             )

languages_listbox.pack()

root.mainloop()

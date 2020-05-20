from tkinter import *

languages = [
    "Python",
    "JavaScript",
    "C#",
    "Java",
    "C/C++",
    "Swift",
    "PHP",
    "Ruby",
    "Go",
    "Typescript",
    "Kotlin",
    "Visual Basic"
]

root = Tk()
root.title("GUI на Python")

scrollbar = Scrollbar(root)
scrollbar.pack(
    side=RIGHT,
    fill=Y
)

languages_listbox = Listbox(
    yscrollcommand=scrollbar.set,
    width=40
)

for language in languages:
    languages_listbox.insert(
        END,
        language
    )

languages_listbox.pack(
    side=LEFT,
    fill=BOTH
)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()

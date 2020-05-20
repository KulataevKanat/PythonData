from tkinter import *
from tkinter import messagebox


def clear():
    name_entry.delete(0,
                      END
                      )
    surname_entry.delete(0,
                         END
                         )


def display():
    messagebox.showinfo("GUI Python",
                        name_entry.get() +
                        " " +
                        surname_entry.get()
                        )


root = Tk()
root.title("GUI на Python")
root.geometry("250x100+300+250")

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0,
                column=0,
                sticky="w"
                )
surname_label.grid(row=1,
                   column=0,
                   sticky="w"
                   )

name_entry = Entry()
surname_entry = Entry()

name_entry.grid(row=0,
                column=1,
                padx=5,
                pady=5
                )
surname_entry.grid(row=1,
                   column=1,
                   padx=5,
                   pady=5
                   )

# вставка начальных данных
name_entry.insert(0,
                  "Kanat"
                  )
surname_entry.insert(0,
                     "Kulataev"
                     )

display_button = Button(text="Display",
                        command=display
                        )
clear_button = Button(text="Clear",
                      command=clear
                      )

clear_button.grid(row=2,
                  column=0,
                  padx=5,
                  pady=5,
                  sticky=""
                  )
display_button.grid(row=2,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="e"
                    )

root.mainloop()

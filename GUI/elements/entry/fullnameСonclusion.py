from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("Fullname",
                        "\nИмя:" + name.get() +
                        "\nФамилия: " + surname.get() +
                        "\nОтчество: " + patronymic.get())


root = Tk()
root.title("Authorization")
root.geometry("325x200")

name = StringVar()
surname = StringVar()
patronymic = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
patronymic_label = Label(text="Введите отчество:")

name_label.grid(row=0,
                column=0,
                sticky="w",
                )

surname_label.grid(row=1,
                   column=0,
                   sticky="w"
                   )

patronymic_label.grid(row=2,
                      column=0,
                      sticky="w"
                      )

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
patronymic_entry = Entry(textvariable=patronymic)

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

patronymic_entry.grid(row=2,
                      column=1,
                      padx=5,
                      pady=5
                      )

message_button = Button(text="conclusion",
                        command=display_full_name
                        )
message_button.grid(row=3,
                    column=1,
                    padx=5,
                    pady=5,
                    sticky="e"
                    )

root.mainloop()

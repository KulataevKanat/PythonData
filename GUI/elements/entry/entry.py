from tkinter import *
from tkinter import messagebox

def show_message():
    messagebox.showinfo("GUI Python",
                        message.get()
                        )


root = Tk()
root.title("GUI на Python")
root.geometry("600x300")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5,
                    rely=.1,
                    anchor="c"
                    )

message_button = Button(text="Click Me",
                        command=show_message
                        )
message_button.place(relx=.5,
                     rely=.5,
                     anchor="c"
                     )

root.mainloop()
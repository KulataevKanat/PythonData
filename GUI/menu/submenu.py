from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250+500+200")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(
    label="File",
    menu=file_menu
)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250+500+200")

main_menu = Menu()
main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)
root.mainloop()
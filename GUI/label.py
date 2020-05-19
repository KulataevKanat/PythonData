from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("500x500")

label1 = Label(text="Hello World",
               fg="#eee",
               bg="#333"
               )
label1.pack()

label_element = "Элемент \"Label\" позволяет выводить \n статический текст без возможности редактирования."
label2 = Label(text=label_element,
               justify=CENTER
               )
label2.place(relx=.2,
             rely=.3
             )

root.mainloop()
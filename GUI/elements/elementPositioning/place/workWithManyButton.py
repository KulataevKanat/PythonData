from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn1 = Button(text="x=10, y=20",
              background="#555",
              foreground="#ccc",
              padx="14",
              pady="7",
              font="13"
              )
btn1.place(x=10,
           y=20
           )

btn2 = Button(text="x=50, y=100",
              background="#555",
              foreground="#ccc",
              padx="14",
              pady="7",
              font="13"
              )
btn2.place(x=50,
           y=100
           )

btn3 = Button(text="x=140, y=160",
              background="#555",
              foreground="#ccc",
              padx="14",
              pady="7",
              font="13"
              )
btn3.place(x=140,
           y=160
           )

root.mainloop()

from tkinter import *

root = Tk()
root.title("Fill Method")
root.geometry("500x500")

btn1 = Button(text="CLICK ME",
              background="#555",
              foreground="#ccc",
              padx="15",
              pady="6",
              font="15"
              )
btn1.pack(side=RIGHT, fill=Y)

btn2 = Button(text="!-?",
              bg="#555",
              fg="#ccc",
              padx="15",
              pady="6",
              font="15"
              )
btn2.pack(side=TOP, fill=X)

btn3 = Button(text="CLICK ME(2)",
              background="#555",
              foreground="#ccc",
              padx="15",
              pady="6",
              font="15"
              )
btn3.pack(side=RIGHT, fill=Y)

root.mainloop()

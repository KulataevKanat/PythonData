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
btn1.pack(fill=BOTH)

root.mainloop()

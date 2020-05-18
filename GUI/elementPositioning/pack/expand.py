from tkinter import *

root = Tk()
root.title("Expand Method")
root.geometry("300x250")

btn1 = Button(text="CLICK ME",
              background="#555",
              foreground="#ccc",
              padx="15",
              pady="6",
              font="15"
              )

btn1.pack(expand=True, fill=BOTH)

root.mainloop()

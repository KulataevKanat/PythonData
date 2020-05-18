from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))


root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300+300+250")

btn = Button(text="Hello GUI",  # текст кнопки
             background="#5DB11E",  # фоновый цвет кнопки
             foreground="#000000",  # цвет текста
             padx="20",  # отступ от границ до содержимого по горизонтали
             pady="8",  # отступ от границ до содержимого по вертикали
             font=("Verdana", 15, "bold"),  # высота шрифта
             command=click_button  # хранение кол-во кликов
             )
btn.pack()

root.mainloop()

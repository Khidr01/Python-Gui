from tkinter import *


food = ["pizza", "burger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered burger")
    else:
        print("You ordered hotdog")

window = Tk()

window.geometry("640x480")
x = IntVar()

food_img = PhotoImage(file="foodlogo1.png")

for i in range(len(food)):
    radio_btn = Radiobutton(
        window,
        text=food[i],
        variable=x,
        value=i,
        padx=25,
        pady=15,
        font=("Hack", 30),
        image=food_img,
        compound="left",
        indicatoron=0,   # eliminate the circle indicator
        width=200,
        command=order
        )
    radio_btn.pack(anchor=W)

window.mainloop()

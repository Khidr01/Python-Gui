from tkinter import *


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

x = IntVar()

python_logo = PhotoImage(file="python_logo.png")

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,  # Using this property we are associating a variable
                           # with this check button. By default, the checkboxes stores 1 or 0
                           # as True or False. However, we can manipulate it as we want by editing a
                           # called onvalue and offvalue. Those properties will determine what type or
                           # what we should return when the checkbox is activated or deactivated.
                           # But again, those properties have default values of 1 and 0.
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00FF00",
                           padx=25,
                           pady=10,
                           image=python_logo,
                           compound="right",
                           selectcolor="black",
                           )
check_button.pack()

window.mainloop()

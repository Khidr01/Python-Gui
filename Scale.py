from tkinter import *


def submit():
    print("The temperature is: {0} degree C".format(scale.get()))


window = Tk()

scale = Scale(
    window,
    from_=0,
    to=100,
    length=400,
    orient=VERTICAL,  # and can be Horizontal
    font=("Droid Sans Mono", 22),
    tickinterval=10,  # Numeric indicators, notice that if the length
    # of the scale isn't enough, it won't divide to real 10 slides
    showvalue=False,  # Hide the current value, and to retrieve it we should
    # press the submit button
    resolution=5,  # moves the slider 5 by 5
    troughcolor='#ffeeaa',
    fg='#eeee33',
    bg='#aa22bb'
)
scale.set(100)  # This statement is used to set the start position
# of the slider
# scale.set(['form'])  in this version we are indicating to start
# from the position we specified in the properties
scale.pack()

btn = Button(
    window,
    text="Submit",
    command=submit
)
btn.pack()

window.mainloop()

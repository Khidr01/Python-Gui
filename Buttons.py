from tkinter import *


def click():
    print("You clicked the button!")


window = Tk()

window.geometry("640x480")

photo = PhotoImage(file="internet.png", height=400, width=400)

button = Button(
    window,
    text="click me!",
    command=click,
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    state=ACTIVE,  # If this attribute was set
    # it means the button won't be clickable anymore, just static
    # Normally is it active, to deactivate set it to: DISABLED
    image=photo,
    # Again as we learned in label tutorial
    # When setting the image property, the text won't appear
    # Therefore, in order to let the text display, again we
    # need to specify the compound property.
    compound="top",  # this will set the photo to be on the top
    # and the text on bottom

)
button.pack()

window.mainloop()

from tkinter import *


def submit():
    username = entry.get()
    print("Hello {}".format(username))
    # This code is to play with the code
    # after a user enter his name the entry box will be disabled
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()
# window.geometry('640x480')

entry = Entry(
    window,
    font=("Arial", 50),
    fg="#00FF00",
    bg="black",
    show="*"  # This command is to replace the letters with asterisks
    # For example if we want to get a password from this entry
    # we can hide the entered value using this property.
)
entry.insert(0, 'Enter your name:')
# This is used for setting a default value
entry.pack(side=LEFT)

submit_button = Button(
    window,
    text="submit",
    command=submit
)
submit_button.pack(side=RIGHT)
delete_button = Button(
    window,
    text="delete",
    command=delete
)
delete_button.pack(side=RIGHT)
backspace_button = Button(
    window,
    text="backspace",
    command=backspace
)
backspace_button.pack(side=RIGHT)

window.mainloop()

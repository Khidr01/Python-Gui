from tkinter import *

window = Tk()
window.geometry("640x480")

photo = PhotoImage(file="internet.png")

label = Label(window,
              text="Hack The World",
              font=("Arial", 40, "bold"),
              fg="#FFFFAB",
              bg="black",
              relief=SUNKEN,  # setting a border
              # There is also another one called SUNKEN
              bd=10,  # setting border width
              padx=80,  # setting padding X
              pady=50,  # setting padding Y
              image=photo,  # Adding image for the label
              # but right now, just the image will appear not the text
              # However, by using the following attribute
              # we can let the both to appear together
              compound='right'
              )
label.pack()

window.mainloop()

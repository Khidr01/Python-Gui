from tkinter import *

window = Tk() # Instantiate an instance of a window
window.geometry("420x420")

window.title("My GUI")
icon = PhotoImage(file="internet.png")
window.iconphoto(True, icon)

window.config(background="#AA1111")

window.mainloop() # place window on computer screen
# and listen for events

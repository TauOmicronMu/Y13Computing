from Tkinter import *
from Constants import *

def CreatePopup(message):

    Popup = Toplevel()
    Popup.title(WINDOW_TITLE)

    msg = Message(Popup, text=message, width=350, justify=CENTER, padx=10, pady=10)
    msg.pack()

    button = Button(Popup, text="Dismiss", command=Popup.destroy)
    button.pack()

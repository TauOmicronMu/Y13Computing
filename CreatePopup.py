def CreatePopup(message):

    Popup = Toplevel()
    Popup.title(WINDOW_TITLE)

    msg = Message(top, text=message)
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

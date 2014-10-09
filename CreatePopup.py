from Tkinter import *
from Constants import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readlines()
    if Language == "GERMAN":
        from StringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *
        
def CreatePopup(message):

    from StringsGerman import *
    Popup = Toplevel()
    Popup.title(WINDOW_TITLE)

    msg = Message(Popup, text=message, width=350, justify=CENTER, padx=10, pady=10)
    msg.pack()

    button = Button(Popup, text=POPUP_DISMISS_TEXT, command=Popup.destroy)
    button.pack()

from Tkinter import *
from Constants import *
from TimeStamp import *
from easygui import *
from CreatePopup import *

import re

class InitSetupPopup(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Instance of InitSetupPopup Class initialised. Self : " + str(self) + " Parent: " + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        global AdminPassEntry
        global AdminPassEntryTwo

        AnchorLabel = Label()
        
        AdminPassLabel = Label(text=u'Enter an Administrator Password', anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        AdminPassLabelTwo = Label(text=u'Reenter Password', anchor=CENTER)
        AdminPassEntryTwo = Entry(show="*")

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        SubmitButton = Button(text=u"Submit")
        SubmitButton['command'] = lambda: self.PasswordSubmit()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded 2nd Button \n")

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        AdminPassLabel.grid(row=1, column=1)
        AdminPassEntry.grid(row=1, column=2)
        AdminPassLabelTwo.grid(row=2, column=1)
        AdminPassEntryTwo.grid(row=2, column=2)
        SubmitButton.grid(row=2, column=3)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")
    
    def PasswordSubmit(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Submit Button Pressed\n")
        if AdminPassEntry.get() == AdminPassEntryTwo.get():
            if re.search(r'\d', AdminPassEntry.get()):
                if re.search(r'[A-Z]', AdminPassEntry.get()):
                    if re.search(r'[a-z]', AdminPassEntry.get()):
                        if len(AdminPassEntry.get()) >= 8:
                            with open("AdminPass.txt" ,'w') as f:
                                f.write("%s" %hash(AdminPassEntry.get()))
                            with open("Log.txt", "a") as f:
                                f.write(TimeStamp() + " Admin Password created. \n")
                                self.parent.destroy()
                        else:
                            CreatePopup("Your password must contain at least 8 characters.")
                            return
                    else:
                        CreatePopup("Your password must contain at least 1 Lowercase letter.")
                        return
                else:
                    CreatePopup("Your password must contain at least 1 Uppercase letter.")
                    return
            else:
                CreatePopup("Your password must contain at least 1 Digit.")
                return
        else:
            CreatePopup("The Password Fields didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Admin Pass Creation - Password Mismatch. \n")
            return
            
from LoginForm import *


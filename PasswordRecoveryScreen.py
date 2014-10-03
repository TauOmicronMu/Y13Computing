from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

import pickle
import re

class PasswordRecoveryWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Instance of InitSetupPopup Class initialised. Self : " + str(self) + " Parent: " + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label="Back", underline=0, command=self.onBack)

        fileMenu.add_separator()
        
        fileMenu.add_command(label="Help", underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Menubar Initialised \n")

        global SecurityQuestionDropdown
        global UsernameEntry
        global SecurityQuestionAnswerEntry
        global NewPassEntry
        global NewPassEntryTwo

        AnchorLabel = Label()
        
        UsernameLabel = Label(text=u'Employee Username', anchor=CENTER)
        UsernameEntry = Entry()

        SecurityQuestionLabel = Label(text=u'Security Question')

        SecurityQuestionAnswerLabel = Label(text=u"Security Question Answer")
        SecurityQuestionAnswerEntry = Entry()

        NewPassLabel = Label(text=u'New Password')
        NewPassEntry = Entry()
        NewPassLabelTwo = Label(text=u'Reenter New Password')
        NewPassEntryTwo = Entry()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        SubmitButton = Button(text=u"Recover Password")
        SubmitButton['command'] = lambda: self.RecoverPassword()

        BackButton = Button(text=u"Back")
        BackButton['command'] = lambda: self.onBack()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Buttons \n")

        SecurityVar = StringVar(self.parent)
        SecurityVar.set("Mother's Maiden Name")

        SecurityQuestionDropdown = OptionMenu(self.parent, SecurityVar, "Mother's Maiden Name", "Memorable Place", "Name of First Pet", "Street you first lived in")

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        UsernameLabel.grid(row=1, column=1)
        UsernameEntry.grid(row=1, column=2)
        SecurityQuestionLabel.grid(row=2, column=1)
        SecurityQuestionDropdown.grid(row=2, column=2)
        SecurityQuestionAnswerLabel.grid(row=3, column=1)
        SecurityQuestionAnswerEntry.grid(row=3, column=2)
        NewPassLabel.grid(row=4, column=1)
        NewPassEntry.grid(row=4, column=2)
        NewPassLabelTwo.grid(row=5, column=1)
        NewPassEntryTwo.grid(row=5, column=2)
        SubmitButton.grid(row=6, column=2)
        BackButton.grid(row=7, column=2)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")
    
    def RecoverPassword(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Recover Account Button Pressed\n")
        
        pass

    def Help(self):
        
        CreatePopup("Here, you can recover your Account password..")

    def onBack(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Back Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Register Window Terminated\n")
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()

from LoginForm import *


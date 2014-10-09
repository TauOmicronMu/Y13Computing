from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from PasswordRecoveryScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from PasswordRecoveryScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import pickle
import re

class PasswordRecoveryWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + PASSWORD_RECOVERY_WINDOW_INSTANCE_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label=DROPDOWN_BACK_TEXT, underline=0, command=self.onBack)

        fileMenu.add_separator()
        
        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        global SecurityQuestionDropdown
        global UsernameEntry
        global SecurityQuestionAnswerEntry
        global NewPassEntry
        global NewPassEntryTwo

        AnchorLabel = Label()
        
        UsernameLabel = Label(text=EMPLOYEE_USERNAME_TEXT, anchor=CENTER)
        UsernameEntry = Entry()

        SecurityQuestionLabel = Label(text=SECURITY_QUESTION_TEXT)

        SecurityQuestionAnswerLabel = Label(text=SECURITY_ANSWER_TEXT)
        SecurityQuestionAnswerEntry = Entry()

        NewPassLabel = Label(text=NEW_PASSWORD_TEXT)
        NewPassEntry = Entry()
        NewPassLabelTwo = Label(text=REENTER_PASSWORD_TEXT)
        NewPassEntryTwo = Entry()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=RECOVER_PASSWORD_TEXT)
        SubmitButton['command'] = lambda: self.RecoverPassword()

        BackButton = Button(text=BACK_BUTTON_TEXT)
        BackButton['command'] = lambda: self.onBack()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        SecurityVar = StringVar(self.parent)
        SecurityVar.set(MOTHER_MAIDEN_NAME_TEXT)

        SecurityQuestionDropdown = OptionMenu(self.parent, SecurityVar,
                                              MOTHER_MAIDEN_NAME_TEXT,
                                              MEMORABLE_PLACE_TEXT,
                                              FIRST_PET_TEXT,
                                              FIRST_STREET_TEXT)

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

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)
    
    def RecoverPassword(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + RECOVER_ACCOUNT_BUTTON_PRESSED)
        
        pass

    def Help(self):
        
        CreatePopup(HELP_TEXT)

    def onBack(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + BACK_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()

from LoginForm import *


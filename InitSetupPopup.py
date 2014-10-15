from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from InitSetupPopupStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from InitSetupPopupStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import re

class InitSetupPopup(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_INITSETUPPOPUP_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.onExit)

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        global AdminPassEntry
        global AdminPassEntryTwo

        AnchorLabel = Label()
        
        AdminPassLabel = Label(text=ENTER_ADMIN_PASS_TEXT, anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        AdminPassLabelTwo = Label(text=REENTER_ADMIN_PASS_TEXT, anchor=CENTER)
        AdminPassEntryTwo = Entry(show="*")

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=SUBMIT_BUTTON_TEXT)
        SubmitButton['command'] = lambda: self.PasswordSubmit()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        AdminPassLabel.grid(row=1, column=1)
        AdminPassEntry.grid(row=1, column=2)
        AdminPassLabelTwo.grid(row=2, column=1)
        AdminPassEntryTwo.grid(row=2, column=2)
        SubmitButton.grid(row=2, column=3)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)
    
    def PasswordSubmit(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + SUBMIT_BUTTON_PRESSED_TEXT)
        if AdminPassEntry.get() == AdminPassEntryTwo.get():
            if re.search(r'\d', AdminPassEntry.get()):
                if re.search(r'[A-Z]', AdminPassEntry.get()):
                    if re.search(r'[a-z]', AdminPassEntry.get()):
                        if len(AdminPassEntry.get()) >= 8:
                            with open(ADMIN_PASS_FILENAME , WRITE_MODE) as f:
                                f.write("%s" %hash(AdminPassEntry.get()))
                            with open(LOG_FILENAME, APPEND_MODE) as f:
                                f.write(TimeStamp() + ADMIN_PASS_CREATED_TEXT)
                                self.parent.destroy()
                        else:
                            CreatePopup(PASS_TOO_SHORT_TEXT)
                            return
                    else:
                        CreatePopup(PASS_LOWERCASE_TEXT)
                        return
                else:
                    CreatePopup(PASS_UPPERCASE_TEXT)
                    return
            else:
                CreatePopup(PASS_DIGIT_TEXT)
                return
        else:
            CreatePopup(PASS_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + ADMIN_PASS_CREATION_MISMATCH)
            return

    def Help(self):
        
        CreatePopup(ADMIN_PASS_CREATION_HELP_TEXT)

    def onExit(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + QUIT_SELECTED_TEXT)
        CreatePopup(CREATE_ADMIN_PASS_TEXT)
            
from LoginForm import *


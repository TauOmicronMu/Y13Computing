#AddExpenditureScreen

from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from AddExpenditureScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from AddExpenditureScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import re

class AddExpenditureScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_INITSETUPPOPUP_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label=DROPDOWN_BACK_TEXT, underline=0, command=self.onBack)

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)

        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)
       
        global ExpenditureEntry
        global ExpenditureEntryTwo
        global AdminPassEntry

        AnchorLabel = Label()

        ExpenditureLabel = Label(text=EXPENDITURE_ONE_TEXT, anchor=CENTER)
        ExpenditureEntry = Entry()

        ExpenditureLabelTwo = Label(text=EXPENDITURE_TWO_TEXT, anchor=CENTER)
        ExpenditureEntryTwo = Entry()
        
        AdminPassLabel = Label(text=ENTER_ADMIN_PASS_TEXT, anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=SUBMIT_BUTTON_TEXT)
        SubmitButton['command'] = lambda: self.PasswordSubmit()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        ExpenditureLabel.grid(row=1, column=1)
        ExpenditureEntry.grid(row=1, column=2)
        ExpenditureLabelTwo.grid(row=2, column=1)
        ExpenditureEntryTwo.grid(row=2, column=2)
        AdminPassLabel.grid(row=3, column=1)
        AdminPassEntry.grid(row=3, column=2)
        SubmitButton.grid(row=4, column=3)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

    def Help(self):
        
        CreatePopup(ADD_EXPENDITURE_HELP_TEXT)

    def onBack(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + BACK_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)
        root =Tk()
        root.geometry(WINDOW_GEOMETRY)
        app = Splash(root)
        root.mainloop()
            
from MainScreen import *


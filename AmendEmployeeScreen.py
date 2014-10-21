#AmendEmployeeScreen

from Constants import *
from CreatePopup import *
from Tkinter import *
from TimeStamp import *
from BaseModule import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from AmendEmployeeScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from AmendEmployeeScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import pickle
import re

class AmendEmployeeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_AMENDLOGINSCREEN_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        global AmendTypeVar
        global ValueEntry

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu.add_command(label=DROPDOWN_BACK_TEXT, underline=0, command=self.onBack)
        
        fileMenu.add_command(label=DROPDOWN_QUIT_TEXT, underline=0, command=self.onExit)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        AnchorLabel = Label(padx=130, pady=70)

        BlankLabel = Label(pady=5)

        TitleLabel = Label(text=AMEND_FOR_EMPLOYEES_TEXT, font=("Purisa", 16))

        AmendTypeLabel = Label(text=AMEND_BY_TEXT, anchor=E)
        
        ValueLabel = Label(text=AMEND_FOR_TEXT, anchor=E)
        ValueEntry = Entry()

        EmployeeCodeLabel = Label(text=EMP_CODE_TEXT, anchor=E)
        EmployeeCodeEntry = Entry()

        AmendTypeVar = StringVar(self.parent)
        AmendTypeVar.set(DROPDOWN_NAME_TEXT)

        AmendTypeDropdown = OptionMenu(self.parent, AmendTypeVar,
                                        DROPDOWN_NAME_TEXT,
                                        DROPDOWN_DEPARTMENT_TEXT,
                                        DROPDOWN_DOB_TEXT,
                                        DROPDOWN_SALARY_TEXT,
                                        DROPDOWN_EMPCODE_TEXT)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + AMENDTYPEDROWPDOWN_MENU_INITIALISED_TEXT)

        BackButton = Button(text=BACK_BUTTON_TEXT)
        BackButton['command'] = lambda: self.onBack()

        AmendButton = Button(text=AMEND_BUTTON_TEXT)
        AmendButton['command'] = lambda: self.onAmend()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)
            
        AnchorLabel.grid(row=0, column=0)
        TitleLabel.grid(row=1, column=2)
        BlankLabel.grid(row=2, column=2)
        EmployeeCodeLabel.grid(row=3, column=1)
        EmployeeCodeEntry.grid(row=3, column=2)
        AmendTypeLabel.grid(row=4, column=1)
        AmendTypeDropdown.grid(row=4, column=2)
        ValueLabel.grid(row=5, column=1)
        ValueEntry.grid(row=5, column=2)
        AmendButton.grid(row=6, column=2)
        BackButton.grid(row=6, column=3)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

    def onAmend(self):
        pass

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

    def onExit(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + QUIT_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)

    def Help(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + HELP_SELECTED_TEXT)
        CreatePopup(HELP_OPTION_TEXT)

from LoginForm import *
from MainScreen import *


from Constants import *
from CreatePopup import *
from Tkinter import *
from MainScreen import *
from TimeStamp import *
from BaseModule import *
from SearchResultsScreen import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from SearchEmployeeScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from SearchEmployeeScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import pickle
import re

class SearchEmployeeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_CREATELOGINSCREEN_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        global SearchTypeVar
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

        TitleLabel = Label(text=SEARCH_FOR_EMPLOYEES_TEXT, font=("Purisa", 16))

        SearchTypeLabel = Label(text=SEARCH_BY_TEXT, anchor=E)
        
        ValueLabel = Label(text=SEARCH_FOR_TEXT, anchor=E)
        ValueEntry = Entry()

        SearchTypeVar = StringVar(self.parent)
        SearchTypeVar.set(DROPDOWN_NAME_TEXT)

        SearchTypeDropdown = OptionMenu(self.parent, SearchTypeVar,
                                        DROPDOWN_NAME_TEXT,
                                        DROPDOWN_DEPARTMENT_TEXT,
                                        DROPDOWN_DOB_TEXT,
                                        DROPDOWN_SALARY_TEXT,
                                        DROPDOWN_EMPCODE_TEXT)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + SEARCHTYPEDROWPDOWN_MENU_INITIALISED_TEXT)

        BackButton = Button(text=BACK_BUTTON_TEXT)
        BackButton['command'] = lambda: self.onBack()

        SearchButton = Button(text=SEARCH_BUTTON_TEXT)
        SearchButton['command'] = lambda: self.onSearch()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)
            
        AnchorLabel.grid(row=0, column=0)
        TitleLabel.grid(row=1, column=2)
        BlankLabel.grid(row=2, column=2)
        SearchTypeLabel.grid(row=3, column=1)
        SearchTypeDropdown.grid(row=3, column=2)
        ValueLabel.grid(row=4, column=1)
        ValueEntry.grid(row=4, column=2)
        SearchButton.grid(row=5, column=2)
        BackButton.grid(row=5, column=3)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

    def onSearch(self):

        try:
            if isNone(ValueEntry.get()) == True:
                CreatePopup(SEARCH_EMP_SCREEN_NONETYPE_ERROR_TEXT)
                return
            names = []
            departments = []
            DOBs = []
            genders = []
            salaries = []
            codes = []
            searchIn = SearchTypeVar.get()
            if searchIn == "Employee Code":
                searchIn = CODE_TEXT
            searchFor = ValueEntry.get()
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + SEARCH_SELECTED_TEXT)
            with open(EMP_DATABASE_FILENAME, READ_MODE) as f:
                EmpDatabase = eval(f.readline())
            #If you are searching for a name, and the search criteria
            #is one character in length 
            if searchIn == NAME_TEXT and len(searchFor) == 1:
                for i in EmpDatabase:
                    if i[searchIn][0] == searchFor:
                        names.append(i[NAME_TEXT])
                        departments.append(i[DEPARTMENT_TEXT])
                        DOBs.append(i[DOB_TEXT])
                        genders.append(i[GENDER_TEXT])
                        salaries.append(i[SALARY_TEXT])
                        codes.append(i[CODE_TEXT])
            #All other search cases
            else:
                for i in EmpDatabase:
                    if searchFor in i[searchIn]:
                        names.append(i[NAME_TEXT])
                        departments.append(i[DEPARTMENT_TEXT])
                        DOBs.append(i[DOB_TEXT])
                        genders.append(i[GENDER_TEXT])
                        salaries.append(i[SALARY_TEXT])
                        codes.append(i[CODE_TEXT])
            self.parent.destroy()
            root = Tk()
            root.geometry(WINDOW_GEOMETRY)
            app = SearchResultsScreen(root, names, departments, DOBs,
                                      genders, salaries, codes, searchIn, searchFor)
            root.mainloop()
        except:
            CreatePopup(NO_EMP_RECORDS_TEXT)

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


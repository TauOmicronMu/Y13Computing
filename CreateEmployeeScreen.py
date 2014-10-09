from Constants import *
from CreatePopup import *
from Tkinter import *
from MainScreen import *
from TimeStamp import *
from BaseModule import *
from GenerateCode import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from CreateEmployeeScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from CreateEmployeeScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import pickle
import re

class CreateEmployeeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_CREATEEMPSCREEN_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

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

        global EmployeeNameEntry
        global EmployeeNameEntryTwo
        global EmployeeDepartmentEntry
        global EmployeeDepartmentEntryTwo
        global EmployeeDOBEntry
        global EmployeeDOBEntryTwo
        global EmployeeGenderEntry
        global EmployeeGenderEntryTwo
        global EmployeeSalaryEntry
        global EmployeeSalaryEntryTwo

        AnchorLabel = Label()
       
        EmployeeNameLabel = Label(text=EMP_NAME_LABEL_TEXT, anchor=E)
        EmployeeNameEntry = Entry()
        EmployeeNameLabelTwo = Label(text=EMP_NAME_LABEL_TWO_TEXT, anchor=E)
        EmployeeNameEntryTwo = Entry()

        EmployeeDepartmentLabel = Label(text=EMP_DEPARTMENT_LABEL_TEXT, anchor=E)
        EmployeeDepartmentEntry = Entry()
        EmployeeDepartmentLabelTwo = Label(text=EMP_DEPARTMENT_LABEL_TWO_TEXT, anchor=E)
        EmployeeDepartmentEntryTwo = Entry()

        EmployeeDOBLabel = Label(text=EMP_DOB_LABEL_TEXT, anchor=E)
        EmployeeDOBEntry = Entry()
        EmployeeDOBLabelTwo = Label(text=EMP_DOB_LABEL_TWO_TEXT, anchor=E)
        EmployeeDOBEntryTwo = Entry()

        EmployeeGenderLabel = Label(text=EMP_GENDER_LABEL_TEXT, anchor=E)
        EmployeeGenderEntry = Entry()
        EmployeeGenderLabelTwo = Label(text=EMP_GENDER_LABEL_TWO_TEXT, anchor=E)
        EmployeeGenderEntryTwo = Entry()

        EmployeeSalaryLabel = Label(text=EMP_SALARY_LABEL_TEXT, anchor=E)
        EmployeeSalaryEntry = Entry()
        EmployeeSalaryLabelTwo = Label(text=EMP_SALARY_LABEL_TWO_TEXT, anchor=E)
        EmployeeSalaryEntryTwo = Entry()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=CES_SUBMIT_BUTTON_TEXT)
        SubmitButton['command'] = lambda: self.SubmitAndCreate()

        EmployeeNameHelpButton = Button(text=HELP_SYMBOL)
        EmployeeNameHelpButton['command'] = lambda: self.EmpNameHelp()

        EmployeeDepartmentHelpButton = Button(text=HELP_SYMBOL)
        EmployeeDepartmentHelpButton['command'] = lambda: self.EmpDepartmentHelp()

        EmployeeDOBHelpButton = Button(text=HELP_SYMBOL)
        EmployeeDOBHelpButton['command'] = lambda: self.EmpDOBHelp()

        EmployeeGenderHelpButton = Button(text=HELP_SYMBOL)
        EmployeeGenderHelpButton['command'] = lambda: self.EmpGenderHelp()

        EmployeeSalaryHelpButton = Button(text=HELP_SYMBOL)
        EmployeeSalaryHelpButton['command'] = lambda: self.EmpSalaryHelp()

        BackButton = Button(text=CES_BACK_BUTTON_TEXT)
        BackButton['command'] = lambda: self.onBack()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        EmployeeNameLabel.grid(row=1, column=1)
        EmployeeNameEntry.grid(row=1, column=2)
        EmployeeNameHelpButton.grid(row=1, column=3)
        EmployeeNameLabelTwo.grid(row=2, column=1)
        EmployeeNameEntryTwo.grid(row=2, column=2)
        EmployeeDepartmentLabel.grid(row=3, column=1)
        EmployeeDepartmentEntry.grid(row=3, column=2)
        EmployeeDepartmentHelpButton.grid(row=3, column=3)
        EmployeeDepartmentLabelTwo.grid(row=4, column=1)
        EmployeeDepartmentEntryTwo.grid(row=4, column=2)
        EmployeeDOBLabel.grid(row=5, column=1)
        EmployeeDOBEntry.grid(row=5, column=2)
        EmployeeDOBHelpButton.grid(row=5, column=3)
        EmployeeDOBLabelTwo.grid(row=6, column=1)
        EmployeeDOBEntryTwo.grid(row=6, column=2)
        EmployeeGenderLabel.grid(row=7, column=1)
        EmployeeGenderEntry.grid(row=7, column=2)
        EmployeeGenderHelpButton.grid(row=7, column=3)
        EmployeeGenderLabelTwo.grid(row=8, column=1)
        EmployeeGenderEntryTwo.grid(row=8, column=2)
        EmployeeSalaryLabel.grid(row=9, column=1)
        EmployeeSalaryEntry.grid(row=9, column=2)
        EmployeeSalaryHelpButton.grid(row=9, column=3)
        EmployeeSalaryLabelTwo.grid(row=10, column=1)
        EmployeeSalaryEntryTwo.grid(row=10, column=2)
        SubmitButton.grid(row=11, column=2)
        BackButton.grid(row=11, column=3)
        

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)
    
    def SubmitAndCreate(self):

        if isNone(EmployeeNameEntry.get()) == True or isNone(EmployeeNameEntryTwo.get()) == True:
            CreatePopup(NO_EMP_NAME_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_NO_EMP_NAME_TEXT)
            return
        elif EmployeeNameEntry.get() != EmployeeNameEntryTwo.get():
            CreatePopup(EMP_NAME_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_EMP_NAME_MISMATCH_TEXT)
            return
        elif isNone(EmployeeDepartmentEntry.get()) == True or isNone(EmployeeDepartmentEntryTwo.get()) == True:
            CreatePopup(NO_EMP_DEPARTMENT_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_NO_EMP_DEPARTMENT_TEXT)
            return
        elif EmployeeDepartmentEntry.get() != EmployeeDepartmentEntryTwo.get():
            CreatePopup(EMP_DEPARTMENT_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_EMP_DEPARTMENT_MISMATCH_TEXT)
            return
        elif isNone(EmployeeDOBEntry.get()) or isNone(EmployeeDOBEntryTwo.get()) == True:
            CreatePopup(NO_EMP_DOB_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_NO_DOB_TEXT)
            return
        elif not DOBCheck(EmployeeDOBEntry.get()) == True:
            CreatePopup(EMP_DOB_INVALID_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_INVALID_DOB_TEXT)
            return
        elif EmployeeDOBEntry.get() != EmployeeDOBEntry.get():
            CreatePopup(EMP_DOB_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_EMP_DOB_MISMATCH_TEXT)
            return
        elif isNone(EmployeeGenderEntry.get()) == True or isNone(EmployeeGenderEntryTwo.get()) == True:
            CreatePopup(NO_EMP_GENDER_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_NO_EMP_GENDER_TEXT)
            return
        elif not GenderCheck(EmployeeGenderEntry.get()) == True:
            CreatePopup(EMP_GENDER_INVALID_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_INVALID_GENDER_TEXT)
            return
        elif EmployeeGenderEntry.get() != EmployeeGenderEntryTwo.get():
            CreatePopup(EMP_GENDER_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_EMP_GENDER_MISMATCH_TEXT)
            return
        elif isNone(EmployeeSalaryEntry.get()) == True or isNone(EmployeeSalaryEntryTwo.get()) == True:
            CreatePopup(NO_EMP_SALARY_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_NO_EMP_SALARY_TEXT)
            return
        elif not SalaryCheck(EmployeeSalaryEntry.get()) == True:
            CreatePopup(EMP_SALARY_INVALID_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_INVALID_SALARY_TEXT)
            return
        elif EmployeeSalaryEntry.get() != EmployeeSalaryEntryTwo.get():
            CreatePopup(EMP_SALARY_MISMATCH_TEXT)
            with open(LOG_FILENAME, APPEND_MODE) as f:
                f.write(TimeStamp() + LOG_EMP_SALARY_MISMATCH_TEXT)
            return
        CurrentDatabase = pickle.load(open(EMP_DATABASE_FILENAME, READ_BINARY_MODE))
        EmpCode = GenerateCode()
        EmpCodes = pickle.load(open( EMPCODE_FILENAME, READ_BINARY_MODE))
        EmpCodes.append(EmpCode)
        pickle.dump(EmpCodes, open(EMPCODE_FILENAME, APPEND_BINARY_MODE))
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_EMP_DATABASE_TEXT)
        CurrentDatabase.update({CES_NAME_TEXT:EmployeeNameEntry.get(),
                                CES_DEPARTMENT_TEXT:EmployeeDepartmentEntry.get(),
                                CES_DOB_TEXT:EmployeeDOBEntry.get(),
                                CES_GENDER_TEXT:EmployeeGenderEntry.get(),
                                CES_SALARY_TEXT:EmployeeSalaryEntry.get(),
                                CES_CODE_TEXT:EmpCode})
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + ADDED_TEXT %CurrentDatabase + " \n")
        pickle.dump(CurrentDatabase, open(EMP_DATABASE_FILENAME, APPEND_BINARY_MODE))
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + SAVED_NEW_DATABASE_TEXT)
        self.onBack()

    def Help(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + HELP_SELECTED_TEXT)
        CreatePopup(CES_HELP_TEXT)

    def EmpNameHelp(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + EMP_NAME_HELP_SELECTED_TEXT)
        CreatePopup(CES_NAME_HELP_TEXT)

    def EmpDepartmentHelp(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + EMP_DEPARTMENT_HELP_SELECTED_TEXT)
        CreatePopup(CES_DEPARTMENT_HELP_TEXT)

    def EmpDOBHelp(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + EMP_DOB_HELP_SELECTED_TEXT)
        CreatePopup(CES_DOB_HELP_TEXT)

    def EmpGenderHelp(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + EMP_GENDER_HELP_SELECTED_TEXT)
        CreatePopup(CES_GENDER_HELP_TEXT)

    def EmpSalaryHelp(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + EMP_SALARY_HELP_SELECTED_TEXT)
        CreatePopup(CES_SALARY_HELP_TEXT)

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
            
from LoginForm import *
from MainScreen import *


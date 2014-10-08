from Constants import *
from CreatePopup import *
from Tkinter import *
from MainScreen import *
from TimeStamp import *
from BaseModule import *
from GenerateCode import *
from Strings import *

import pickle
import re

class CreateEmployeeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
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

        with open("Log.txt", "a") as f:
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

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=u"Submit")
        SubmitButton['command'] = lambda: self.SubmitAndCreate()

        EmployeeNameHelpButton = Button(text=u"?")
        EmployeeNameHelpButton['command'] = lambda: self.EmpNameHelp()

        EmployeeDepartmentHelpButton = Button(text=u"?")
        EmployeeDepartmentHelpButton['command'] = lambda: self.EmpDepartmentHelp()

        EmployeeDOBHelpButton = Button(text=u"?")
        EmployeeDOBHelpButton['command'] = lambda: self.EmpDOBHelp()

        EmployeeGenderHelpButton = Button(text=u"?")
        EmployeeGenderHelpButton['command'] = lambda: self.EmpGenderHelp()

        EmployeeSalaryHelpButton = Button(text=u"?")
        EmployeeSalaryHelpButton['command'] = lambda: self.EmpSalaryHelp()

        BackButton = Button(text=u"Back")
        BackButton['command'] = lambda: self.onBack()

        with open("Log.txt", "a") as f:
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
        

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)
    
    def SubmitAndCreate(self):

        if isNone(EmployeeNameEntry.get()) == True or isNone(EmployeeNameEntryTwo.get()) == True:
            CreatePopup("Please Enter/Confirm the Employee's Name.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Employee Issue: No Name \n")
            return
        elif EmployeeNameEntry.get() != EmployeeNameEntryTwo.get():
            CreatePopup("The Employee Names didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Name Mismatch \n")
            return
        elif isNone(EmployeeDepartmentEntry.get()) == True or isNone(EmployeeDepartmentEntryTwo.get()) == True:
            CreatePopup("Please Enter/Confirm the Employee's Department.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: No Department \n")
            return
        elif EmployeeDepartmentEntry.get() != EmployeeDepartmentEntryTwo.get():
            CreatePopup("The Employee Departments didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Department Mismatch \n")
            return
        elif isNone(EmployeeDOBEntry.get()) or isNone(EmployeeDOBEntryTwo.get()) == True:
            CreatePopup("Please Enter/Confirm the Employee's DOB")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: No DOB \n")
            return
        elif not DOBCheck(EmployeeDOBEntry.get()) == True:
            CreatePopup("Please enter a valid DOB.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Invalid DOB \n")
            return
        elif EmployeeDOBEntry.get() != EmployeeDOBEntry.get():
            CreatePopup("The Employee DOB's didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: DOB Mismatch \n")
            return
        elif isNone(EmployeeGenderEntry.get()) == True or isNone(EmployeeGenderEntryTwo.get()) == True:
            CreatePopup("Please Enter/Confirm the Employee's Gender.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: No Gender \n")
            return
        elif not GenderCheck(EmployeeGenderEntry.get()) == True:
            CreatePopup("Please enter a valid gender.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Invalid Gender \n")
            return
        elif EmployeeGenderEntry.get() != EmployeeGenderEntryTwo.get():
            CreatePopup("The Employee Genders didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Gender Mismatch \n")
            return
        elif isNone(EmployeeSalaryEntry.get()) == True or isNone(EmployeeSalaryEntryTwo.get()) == True:
            CreatePopup("Please Enter/Confirm the Employee's Salary.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: No Salary \n")
            return
        elif not SalaryCheck(EmployeeSalaryEntry.get()) == True:
            CreatePopup("Please enter a valid Salary.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Invalid Salary \n")
            return
        elif EmployeeSalaryEntry.get() != EmployeeSalaryEntryTwo.get():
            CreatePopup("The Employee Salaries didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Create Emp Issue: Salary Mismatch \n")
            return
        CurrentDatabase = pickle.load(open( "EmpDatabase.p", "rb"))
        EmpCode = GenerateCode()
        EmpCodes = pickle.load(open( "EmpCodes.p", "rb"))
        EmpCodes.append(EmpCode)
        pickle.dump(EmpCodes, open("EmpCodes.p", "ab"))
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded EmpDatabase.p \n")
        CurrentDatabase.update({"Name":EmployeeNameEntry.get(),"Department":EmployeeDepartmentEntry.get(),"DOB":EmployeeDOBEntry.get(),"Gender":EmployeeGenderEntry.get(),"Salary":EmployeeSalaryEntry.get(),"Code":EmpCode})
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Added %s " %CurrentDatabase + " \n")
        pickle.dump(CurrentDatabase, open( "EmpDatabase.p", "ab"))
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Saved new Database \n")
        self.onBack()

    def Help(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Help Selected \n")
        CreatePopup("Here you can create a new Employee Record. Fill in the fields, and click 'Submit' to do so.")

    def EmpNameHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " EmpName Help Selected \n")
        CreatePopup("This is the Employee's Name - Forename & Surname")

    def EmpDepartmentHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " EmpName Help Selected \n")
        CreatePopup("This is the Employee's current Department")

    def EmpDOBHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " EmpName Help Selected \n")
        CreatePopup("This is the Employee's Date of Birth")

    def EmpGenderHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " EmpName Help Selected \n")
        CreatePopup("This is the Employee's Gender (M/F)")

    def EmpSalaryHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " EmpName Help Selected \n")
        CreatePopup("This is the Employee's Salary per annum (Just a number : i.e. 23000)")

    def onBack(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Back Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")
        root =Tk()
        root.geometry(WINDOW_GEOMETRY)
        app = Splash(root)
        root.mainloop()

    def onExit(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Quit Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")
            
from LoginForm import *
from MainScreen import *


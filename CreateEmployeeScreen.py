from Constants import *
from CreatePopup import *
from Tkinter import *
from MainScreen import *
from TimeStamp import *
from BaseModule import *

import re

class CreateEmployeeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Instance of CreateEmployeeScreen Class initialised. Self : " + str(self) + " Parent: " + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title(WINDOW_TITLE)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label="Quit", underline=0, command=self.onExit)

        fileMenu.add_separator()

        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Menubar Initialised \n")

        AnchorLabel = Label()

        EmployeeNameLabel = Label(text=u'Employee Name', anchor=E)
        EmployeeNameEntry = Entry()
        EmployeeNameLabelTwo = Label(text=u'Reenter Name', anchor=E)
        EmployeeNameEntryTwo = Entry()

        EmployeeDepartmentLabel = Label(text=u'Employee Department', anchor=E)
        EmployeeDepartmentEntry = Entry()
        EmployeeDepartmentLabelTwo = Label(text=u'Reenter Department', anchor=E)
        EmployeeDepartmentEntryTwo = Entry()

        EmployeeDOBLabel = Label(text=u'Employee DOB (DD/MM/YYYY)', anchor=E)
        EmployeeDOBEntry = Entry()
        EmployeeDOBLabelTwo = Label(text=u'Reenter DOB', anchor=E)
        EmployeeDOBEntryTwo = Entry()

        EmployeeGenderLabel = Label(text=u'Employee Gender', anchor=E)
        EmployeeGenderEntry = Entry()
        EmployeeGenderLabelTwo = Label(text=u'Reenter Gender', anchor=E)
        EmployeeGenderEntryTwo = Entry()

        EmployeeSalaryLabel = Label(text=u'Employee Salary', anchor=E)
        EmployeeSalaryEntry = Entry()
        EmployeeSalaryLabelTwo = Label(text=u'Reenter Salary', anchor=E)
        EmployeeSalaryEntryTwo = Entry()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        SubmitButton = Button(text=u"Submit")
        SubmitButton['command'] = lambda: self.Submit()

        EmployeeNameHelpButton = Button(text=u"?")

        EmployeeGenderHelpButton = Button(text=u"?")

        EmployeeSalaryHelpButton = Button(text=u"?")

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Submit Button \n")

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        EmployeeNameLabel.grid(row=1, column=1)
        EmployeeNameEntry.grid(row=1, column=2)
        EmployeeNameHelpButton.grid(row=1, column=3)
        EmployeeNameLabelTwo.grid(row=2, column=1)
        EmployeeNameEntryTwo.grid(row=2, column=2)
        EmployeeDepartmentLabel.grid(row=3, column=1)
        EmployeeDepartmentEntry.grid(row=3, column=2)
        EmployeeDepartmentLabelTwo.grid(row=4, column=1)
        EmployeeDepartmentEntryTwo.grid(row=4, column=2)
        EmployeeDOBLabel.grid(row=5, column=1)
        EmployeeDOBEntry.grid(row=5, column=2)
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
        

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")
    
    def Submit(self):

        pass

    def onExit(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Quit Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")
            
from LoginForm import *


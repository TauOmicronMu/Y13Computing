#DeleteEmployeeScreen

from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

from LoggingStringsEnglish import *

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from DeductExpenditureScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from DeductExpenditureScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

import re

class DeductExpenditureScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INSTANCE_OF_DEDUCTEXPENDITURESCREEN_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

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
        global ReasonEntry

        AnchorLabel = Label()

        ExpenditureLabel = Label(text=DEDUCT_EXPENDITURE_ONE_TEXT, anchor=CENTER)
        ExpenditureEntry = Entry()

        ExpenditureLabelTwo = Label(text=DEDUCT_EXPENDITURE_TWO_TEXT, anchor=CENTER)
        print DEDUCT_EXPENDITURE_TWO_TEXT
        ExpenditureEntryTwo = Entry()

        ReasonLabel = Label(text="Reason for Expenditure: ")
        ReasonEntry = Entry()

        AdminPassLabel = Label(text=ENTER_ADMIN_PASS_TEXT, anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        SubmitButton = Button(text=SUBMIT_BUTTON_TEXT)
        SubmitButton['command'] = lambda: self.Submit()

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        ExpenditureLabel.grid(row=1, column=1)
        ExpenditureEntry.grid(row=1, column=2)
        ExpenditureLabelTwo.grid(row=2, column=1)
        ExpenditureEntryTwo.grid(row=2, column=2)
        ReasonLabel.grid(row=3, column=1)
        ReasonEntry.grid(row=3, column=2)
        AdminPassLabel.grid(row=4, column=1)
        AdminPassEntry.grid(row=4, column=2)
        SubmitButton.grid(row=5, column=3)

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)

    def Submit(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + "Deduct Expenditure Button Pressed. \n")
        with open(ADMIN_PASS_FILENAME, READ_MODE) as f:
            AdminPass = f.readline()
        if str(AdminPass) == str(hash(AdminPassEntry.get())):
            if ExpenditureEntry.get() == ExpenditureEntryTwo.get():
                with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
                    TotalExpenditure = int(f.readline())
                    TotalExpenditure -= int(ExpenditureEntry.get())
                with open(TOTAL_EXPENDITURE_FILENAME, WRITE_MODE) as f:
                    f.write("%s" %TotalExpenditure)
                    with open(LOG_FILENAME, APPEND_MODE) as f:
                        f.write(TimeStamp() + " Expenditure of %s deducted" %TotalExpenditure + " Reason: %s\n" %ReasonEntry.get())
                    self.parent.destroy()
                    with open(LOG_FILENAME, APPEND_MODE) as f:
                        f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)
                    root =Tk()
                    root.geometry(WINDOW_GEOMETRY)
                    app = Splash(root)
                    root.mainloop()
            else:
                CreatePopup("The Expenditures didn't match.")
        else:
            CreatePopup("The Administrator password was incorrect.")
            return

    def Help(self):
        
        CreatePopup(DEDUCT_EXPENDITURE_HELP_TEXT)

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

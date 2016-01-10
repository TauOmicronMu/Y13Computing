from Tkinter import *
from TimeStamp import *
from logging import *
from Constants import *
from CreatePopup import *

from LoggingStringsEnglish import *

import os

with open(LANGUAGE_FILENAME, READ_MODE) as f:
    Language = f.readline()
    if Language == "GERMAN":
        from MainScreenStringsGerman import *
        from PopupsStringsGerman import *
        from DropdownMenuStringsGerman import *
    else:
        from MainScreenStringsEnglish import *
        from PopupsStringsEnglish import *
        from DropdownMenuStringsEnglish import *

class Splash(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.initialiseUI()
        
    def initialiseUI(self):

        global pressedAlready
        pressedAlready = False

        Image = PhotoImage(file=LOGO_GIF_FILENAME)
        global label
        label = Label(self.parent, image=Image, relief=RAISED)
        label.image = Image
        label.pack()

        Image2 = PhotoImage(file=COPYRIGHT_IMAGE_FILENAME)
        global label2
        label2 = Label(self.parent, image=Image2)
        label2.image = Image2
        label2.pack()
      
        self.parent.title(WINDOW_TITLE)
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label=DROPDOWN_LOGOUT_TEXT, underline=0, command=self.Logout)
        fileMenu.add_command(label=DROPDOWN_QUIT_TEXT, underline=0, command=self.Quit)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)
    
        fileMenu.add_separator()
        
        empMenu = Menu(menubar)
        empSubMenu = Menu(empMenu)
        
        empMenu.add_command(label=EMP_MENU_CREATE_TEXT, command=self.CreateEmployee)
        empMenu.add_command(label=EMP_MENU_SEARCH_TEXT, command=self.SearchEmployees)
        empMenu.add_command(label=EMP_MENU_AMEND_TEXT, underline=0, command=self.AmendRecord)
        empMenu.add_command(label=EMP_MENU_DELETE_TEXT, underline=0, command=self.DeleteRecord)
        
        empMenu.add_separator()

        expMenu = Menu(menubar)

        expSubMenu = Menu(expMenu)

        expSubMenu.add_command(label=EXP_SUBMENU_YEARLY_TEXT, command=self.YearlyExpenditure)
        expSubMenu.add_command(label=EXP_SUBMENU_BIANNUAL_TEXT, command=self.BiannualExpenditure)
        expSubMenu.add_command(label=EXP_SUBMENU_QUARTERLY_TEXT, command=self.QuarterlyExpenditure)
        expSubMenu.add_command(label=EXP_SUBMENU_MONTHLY_TEXT, command=self.MonthlyExpenditure)
        expSubMenu.add_command(label=EXP_SUBMENU_WEEKLY_TEXT, command=self.WeeklyExpenditure)
        expSubMenu.add_command(label=EXP_SUBMENU_DAILY_TEXT, command=self.DailyExpenditure)

        expSubMenu.add_separator()

        totalsMenu = Menu(menubar)

        totalsMenu.add_command(label=EMP_COUNT_TEXT,command=self.EmpCount)
        totalsMenu.add_command(label=TOTAL_SALARY_TEXT,command=self.TotalSalary)
        totalsMenu.add_command(label=TOTAL_EXP_TEXT,command=self.TotalExpenditure)

        totalsMenu.add_separator()
        
        menubar.add_cascade(label=MENUBAR_FILE_TEXT, underline=0, menu=fileMenu)
        menubar.add_cascade(label=MENUBAR_EMPLOYEES_TEXT, underline=0, menu=empMenu)
        menubar.add_cascade(label=MENUBAR_EXPENDITURE_TEXT, underline=0, menu=expMenu)
        menubar.add_cascade(label=TOTALS_MENU_TEXT, underline=0, menu=totalsMenu)
        menubar.add_cascade(label=" ", command=self.ChocolateyEgg)
        expMenu.add_cascade(label=EXP_MENU_TOTAL_TEXT, underline=0, menu=expSubMenu)

        expMenu.add_command(label=EXP_MENU_ADD_EXP_TEXT, command=self.addExpenditure)
        expMenu.add_command(label=EXP_MENU_DEDUCT_EXP_TEXT, command=self.deductExpenditure)
  
        expMenu.add_separator()
        
        global TotalSalary
        self.LoadSalary()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + TOTAL_SALARY_LOADED_TEXT)

    def Logout(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOGOUT_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        with open(CURRENT_EMP_FILENAME, WRITE_MODE) as f:
            f.write("")
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CURRENT_EMP_FILENAME + CURRENT_EMPLOYEE_WIPED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()
                
    def Quit(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + QUIT_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)

    def Help(self):
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_SCREEN_HELP_SELECTED_TEXT)
            CreatePopup(MAIN_SCREEN_HELP_TEXT)

    def LoadSalary(self):
        global TotalSalary
        TotalSalary = 0
        with open(EMP_DATABASE_FILENAME, READ_MODE) as f:
            Employees = eval(f.readline())
        for Employee in Employees:
            TotalSalary += int(Employee["Salary"])

    def CreateEmployee(self):

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATE_EMPLOYEE_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = CreateEmployeeScreen(root)
        root.mainloop()

    def SearchEmployees(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + SEARCH_EMPLOYEE_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n")
        app = SearchEmployeeScreen(root)
        root.mainloop()

    def EmpCount(self):
        with open(EMP_DATABASE_FILENAME, READ_MODE) as f:
            Employees = eval(f.readline())
            EmpCount = len(Employees)
        CreatePopup(EMP_COUNT_POPUP_TEXT %EmpCount)

    def TotalSalary(self):
        global TotalSalary
        CreatePopup(TOTAL_SALARY_POPUP_TEXT %TotalSalary)

    def TotalExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            TotalExpenditure = int(f.readline()) + TotalSalary
        CreatePopup(TOTAL_EXPENDITURE_POPUP_TEXT %TotalExpenditure)

    def YearlyExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
        CreatePopup(YEARLY_EXPENDITURE_POPUP_TEXT %YearlyExpenditure)

    def BiannualExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
            BiannualExpenditure = YearlyExpenditure/BIANNUAL_MONTHS
        CreatePopup(BIANNUAL_EXPENDITURE_POPUP_TEXT %BiannualExpenditure)

    def QuarterlyExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
            QuarterlyExpenditure = YearlyExpenditure/QUARTERLY_MONTHS
        CreatePopup(QUARTERLY_EXPENDITURE_POPUP_TEXT %QuarterlyExpenditure)

    def MonthlyExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
            MonthlyExpenditure = YearlyExpenditure/MONTHS_IN_A_YEAR
        CreatePopup(MONTHLY_EXPENDITURE_POPUP_TEXT %MonthlyExpenditure)

    def WeeklyExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
            WeeklyExpenditure = YearlyExpenditure/WEEKS_IN_A_YEAR
        CreatePopup(WEEKLY_EXPENDITURE_POPUP_TEXT %WeeklyExpenditure)

    def DailyExpenditure(self):
        global TotalSalary
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            YearlyExpenditure = int(f.readline()) + TotalSalary
            DailyExpenditure = int(round(YearlyExpenditure/DAYS_IN_A_YEAR,-1))
        CreatePopup(DAILY_EXPENDITURE_POPUP_TEXT %DailyExpenditure)

    def ChocolateyEgg(self):
        global pressedAlready
        import PortalDAGger
        if pressedAlready != True:
            pressedAlready = True
        else:
            reload(PortalDAGger)

    def AmendRecord(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + AMEND_EMPLOYEE_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = AmendEmployeeScreen(root)
        root.mainloop()

    def addExpenditure(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + ADD_EXPENDITURE_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = AddExpenditureScreen(root)
        root.mainloop()

    def deductExpenditure(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + DEDUCT_EXPENDITURE_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = DeductExpenditureScreen(root)
        root.mainloop()

    def DeleteRecord(self):
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + DELETE_RECORD_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + MAIN_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = DeleteEmployeeScreen(root)
        root.mainloop()
        

        
from LoginForm import *
from CreateEmployeeScreen import *
from SearchEmployeeScreen import *
from AmendEmployeeScreen import *
from Constants import *
from AddExpenditureScreen import *
from DeductExpenditureScreen import *
from DeleteEmployeeScreen import *



from Tkinter import *
from TimeStamp import *
from logging import *
from Constants import *
from CreatePopup import *

from MainScreenStringsEnglish import *
from LoggingStringsEnglish import *
from PopupsStringsEnglish import *
from DropdownMenuStringsEnglish import *

class Splash(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.initialiseUI()
        
    def initialiseUI(self):

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
        empMenu.add_cascade(label=EMP_MENU_AMEND_TEXT, underline=0, menu=empSubMenu)
        empMenu.add_command(label=EMP_MENU_DELETE_TEXT)
        
        empMenu.add_separator()

        empSubMenu.add_command(label=EMP_SUBMENU_NAME_TEXT)
        empSubMenu.add_command(label=EMP_SUBMENU_DEPARTMENT_TEXT)
        empSubMenu.add_command(label=EMP_SUBMENU_DOB_TEXT)
        empSubMenu.add_command(label=EMP_SUBMENU_GENDER_TEXT)
        empSubMenu.add_command(label=EMP_SUBMENU_SALARY_TEXT)

        empSubMenu.add_separator()

        expMenu = Menu(menubar)

        expSubMenu = Menu(expMenu)

        expSubMenu.add_command(label=EXP_SUBMENU_YEARLY_TEXT)
        expSubMenu.add_command(label=EXP_SUBMENU_MONTHLY_TEXT)
        expSubMenu.add_command(label=EXP_SUBMENU_WEEKLY_TEXT)
        expSubMenu.add_command(label=EXP_SUBMENU_DAILY_TEXT)
        
        menubar.add_cascade(label=MENUBAR_FILE_TEXT, underline=0, menu=fileMenu)
        menubar.add_cascade(label=MENUBAR_EMPLOYEES_TEXT, underline=0, menu=empMenu)
        menubar.add_cascade(label=MENUBAR_EXPENDITURE_TEXT, underline=0, menu=expMenu)
        expMenu.add_cascade(label=EXP_MENU_TOTAL_TEXT, underline=0, menu=expSubMenu)

        expMenu.add_command(label=EXP_MENU_ADD_EXP_TEXT)
        expMenu.add_command(label=EXP_MENU_DEDUCT_EXP_TEXT)
  
        expMenu.add_separator()

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
        
from LoginForm import *
from CreateEmployeeScreen import *
from SearchEmployeeScreen import *



from Tkinter import *
from TimeStamp import *
from logging import *
from Constants import *
from CreatePopup import *

class Splash(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent

        self.initialiseUI()
        
    def initialiseUI(self):

        Image = PhotoImage(file="EmpTrackerImage.gif")
        global label
        label = Label(self.parent, image=Image, relief=RAISED)
        label.image = Image
        label.pack()

        Image2 = PhotoImage(file="CopyrightNotice.gif")
        global label2
        label2 = Label(self.parent, image=Image2)
        label2.image = Image2
        label2.pack()
      
        self.parent.title("Employee Tracker 1.0.0 (c)")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label="Logout", underline=0)
        fileMenu.add_command(label="Quit", underline=0, command=self.Quit)

        fileMenu.add_separator()

        fileMenu.add_command(label="Help", underline=0, command=self.Help)
        
        empMenu = Menu(menubar)       
        
        empMenu.add_command(label="Create new Employee")
        empMenu.add_command(label="Display all Employee Records")
        empMenu.add_command(label="Search for an Employee Record")
        
        empMenu.add_separator()

        expMenu = Menu(menubar)

        expSubMenu = Menu(expMenu)

        expSubMenu.add_command(label="Yearly")
        expSubMenu.add_command(label="Monthly")
        expSubMenu.add_command(label="Weekly")
        expSubMenu.add_command(label="Daily")
        
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        menubar.add_cascade(label="Employees", underline=0, menu=empMenu)
        menubar.add_cascade(label="Expenditure", underline=0, menu=expMenu)
        expMenu.add_cascade(label="Total", underline=0, menu=expSubMenu)

        expMenu.add_command(label="Add Expenditure")
        expMenu.add_command(label="Deduct Expenditure")
  
        expMenu.add_separator()
                
    def Quit(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Quit Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")

    def Help(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Help Option Pressed\n")
            CreatePopup("This is the main screen. From here, you can perform numerous operations. Use the menu bar to find them.")




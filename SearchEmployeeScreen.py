from Constants import *
from CreatePopup import *
from Tkinter import *
from MainScreen import *
from TimeStamp import *
from BaseModule import *

import pickle
import re

class SearchEmployeeScreen(Frame):

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

        fileMenu.add_command(label="Back", underline=0, command=self.onBack)
        
        fileMenu.add_command(label="Quit", underline=0, command=self.onExit)

        fileMenu.add_separator()

        fileMenu.add_command(label="Help", underline=0, command=self.Help)
        
        fileMenu.add_separator()

        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Menubar Initialised \n")

        BackButton = Button(text=u"Back")
        BackButton['command'] = lambda: self.onBack()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Buttons \n")
            
        BackButton.grid(row=11, column=3)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")

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

    def Help(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Help Selected \n")
        CreatePopup("Here you can create a new Employee Record. Fill in the fields, and click 'Submit' to do so.")


            
from LoginForm import *
from MainScreen import *


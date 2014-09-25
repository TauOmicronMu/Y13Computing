from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *

import pickle

class LoginScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Instance of LoginScreen Class initialised. Self : " + str(self) + " Parent: " + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising LoginScreen UI \n")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label="Quit", underline=0, command=self.onExit)

        fileMenu.add_separator()

        fileMenu.add_command(label="Help", underline=0, command = self.loginHelp)

        fileMenu.add_separator()

        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Menubar Initialised \n")

        self.parent.title(WINDOW_TITLE)

        global UsernameEntry
        global PasswordEntry

        ImageLeft = PhotoImage(file="EmpTrackerImageLeft.gif")
        global LogoLeft
        LogoLeft = Label(self.parent, image=ImageLeft)
        LogoLeft.image = ImageLeft

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded EmpTrackerImageLeft.gif \n")

        ImageRight = PhotoImage(file="EmpTrackerImageRight.gif")
        global LogoRight
        LogoRight = Label(self.parent, image=ImageRight)
        LogoRight.image = ImageRight

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded EmpTrackerImageRight.gif \n")

        AnchorLabel = Label()
        UsernameLabel = Label(text=u'Username',anchor=W)
        UsernameEntry = Entry()
        PasswordLabel = Label(text=u'Password',anchor=W)
        PasswordEntry = Entry(show="*")

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        LoginButton = Button(text=u'Login')
        LoginButton['command'] = lambda: self.tryLogin()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Login Button \n")

        RegisterButton = Button(text=u"Register New Employee Account")
        RegisterButton['command'] = lambda: self.registerAccount()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Register Button \n")

       # HelpButton = Button(text=u"?")
       # HelpButton['command'] = lambda: self.loginHelp()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Register Button \n")
        
        AnchorLabel.grid(pady=35,padx=90,row=0,column=0)
        LogoLeft.grid(pady=20, padx=0,row=1,column=6)
        LogoRight.grid(pady=20, padx=0, row=1, column=7)
        UsernameLabel.grid(row=2, column=6)
        UsernameEntry.grid(row=2, column=7)
        PasswordLabel.grid(row=3, column=6)
        PasswordEntry.grid(row=3, column=7)
        LoginButton.grid(row=4, column=8)
        RegisterButton.grid(row=6, column=7)
        #HelpButton.grid(row=7, column=9)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")

    def onExit(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Quit Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")

    def loginHelp(self):
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Help Option Pressed\n")
            CreatePopup("From here, you can log into your employee account. Both usernames, and passwords are case sensitive. To use the software, you will need to create an account.")   
        
        
    def tryLogin(self):

        from TimeStamp import *
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Button Pressed\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Attempted Login: Username = " + str(UsernameEntry.get()) + "\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Attempted Login: Password = " + str(hash(PasswordEntry.get())) + "\n")
        LoginDict = pickle.load(open( "LoginData.p", "rb"))
        if UsernameEntry.get() in LoginDict:
            if str(LoginDict[UsernameEntry.get()]) == str(hash(PasswordEntry.get())):
                with open("Log.txt", "a") as f:
                    f.write(TimeStamp() + " Successful Login. \n")
                with open("Log.txt", "a") as f:
                    f.write(TimeStamp() + " Updated Current Employee.txt \n")
                with open("CurrentEmployee.txt", "w") as f:
                    f.write(UsernameEntry.get())
                self.parent.destroy()
                root =Tk()
                root.geometry(WINDOW_GEOMETRY)
                with open("Log.txt", "a") as f:
                    f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n")
                app = Splash(root)
                root.mainloop()
            
    def registerAccount(self):
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Register Button Pressed\n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Window Terminated\n")
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
        app = RegisterScreen(root)
        root.mainloop()

from RegisterScreen import *
from MainScreen import *

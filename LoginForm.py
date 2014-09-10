from Tkinter import *
from Constants import *
from TimeStamp import *

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
        UsernameLabel = Label(text=u'Username',anchor=CENTER)
        UsernameEntry = Entry()
        PasswordLabel = Label(text=u'Password',anchor=CENTER)
        PasswordEntry = Entry(show="*")

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        LoginButton = Button(text=u'Login')
        LoginButton['command'] = lambda: self.tryLogin()

        RegisterButton = Button(text=u"Register New Employee Account")
        RegisterButton['command'] = lambda: self.registerAccount()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Login Button \n")
        
        AnchorLabel.grid(pady=35,padx=90,row=0,column=0)
        LogoLeft.grid(pady=20, padx=0,row=1,column=6)
        LogoRight.grid(pady=20, padx=0, row=1, column=7)
        UsernameLabel.grid(row=2, column=6)
        UsernameEntry.grid(row=2, column=7)
        PasswordLabel.grid(row=3, column=6)
        PasswordEntry.grid(row=3, column=7)
        LoginButton.grid(row=4, column=8)
        RegisterButton.grid(row=6, column=7)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")

    def tryLogin(self):
        from TimeStamp import *
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Button Pressed\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Attempted Login: Username = " + str(UsernameEntry.get()) + "\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Attempted Login: Password = " + str(hash(PasswordEntry.get())) + "\n")

    def registerAccount(self):
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Register Button Pressed\n")
        self.root.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Login Window Terminated\n")
        pass
            
            
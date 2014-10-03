from Tkinter import *
from Constants import *
from TimeStamp import *
from CreatePopup import *
from Strings import *

import pickle

class LoginScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOGINSCREEN_INITIALISED_TEXT_ONE + str(self) + LOGINSCREEN_INITIALISED_TEXT_TWO + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):
        
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISING_LOGINSCREEN_TEXT)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label=DROPDOWN_QUIT_TEXT, underline=0, command=self.onExit)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command = self.loginHelp)

        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)

        self.parent.title(WINDOW_TITLE)

        global UsernameEntry
        global PasswordEntry

        AnchorLabel = Label()
        
        TitleLabelLeft = Label(text=TITLE_LABEL_LEFT_TEXT, font=("Purisa", 26))
        TitleLabelRight = Label(text=VERSION_NUMBER + TITLE_LABEL_RIGHT_TEXT, font=("Purisa", 26))

        UsernameLabel = Label(text=USERNAME_LABEL_TEXT)
        UsernameEntry = Entry()
        
        PasswordLabel = Label(text=PASSWORD_LABEL_TEXT)
        PasswordEntry = Entry(show="*")

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        LoginButton = Button(text=u'Login')
        LoginButton['command'] = lambda: self.tryLogin()

        RegisterButton = Button(text=REGISTER_BUTTON_TEXT)
        RegisterButton['command'] = lambda: self.registerAccount()

        ForgottenPassButton = Button(text=FORGOTTEN_PASS_BUTTON_TEXT)
        ForgottenPassButton['command'] = lambda: self.ForgottenPass()

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)
        
        AnchorLabel.grid(pady=35,padx=110,row=0,column=0)
        TitleLabelLeft.grid(pady=20, row=1, column=6)
        TitleLabelRight.grid(pady=20, row=1, column=7)
        UsernameLabel.grid(row=2, column=6)
        UsernameEntry.grid(row=2, column=7)
        PasswordLabel.grid(row=3, column=6)
        PasswordEntry.grid(row=3, column=7)
        LoginButton.grid(row=4, column=8)
        RegisterButton.grid(row=6, column=7)
        ForgottenPassButton.grid(row=7, column=7)
        #HelpButton.grid(row=7, column=9)

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISED_UI_TEXT)

    def onExit(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + QUIT_SELECTED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + WINDOW_TERMINATED_TEXT)

    def loginHelp(self):
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + LOGIN_HELP_PRESSED_TEXT)
            CreatePopup(LOGIN_HELP_TEXT)   
        
        
    def tryLogin(self):

        from TimeStamp import *
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + " Login Button Pressed\n")
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + " Attempted Login: Username = " + str(UsernameEntry.get()) + "\n")
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + " Attempted Login: Password = " + str(hash(PasswordEntry.get())) + "\n")
        LoginDict = pickle.load(open( "LoginData.p", "rb"))
        if hash(UsernameEntry.get()) in LoginDict:
            if str(LoginDict[hash(UsernameEntry.get())]) == str(hash(PasswordEntry.get())):
                with open(LOG_FILENAME, "a") as f:
                    f.write(TimeStamp() + " Successful Login. \n")
                with open(LOG_FILENAME, "a") as f:
                    f.write(TimeStamp() + " Updated Current Employee.txt \n")
                with open("CurrentEmployee.txt", "w") as f:
                    f.write(UsernameEntry.get())
                self.parent.destroy()
                root =Tk()
                root.geometry(WINDOW_GEOMETRY)
                with open(LOG_FILENAME, "a") as f:
                    f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n")
                app = Splash(root)
                root.mainloop()
            else:
                CreatePopup("Invalid Username/Password")
        else:
            CreatePopup("Invalid Username/Password")
            
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

    def ForgottenPass(self):
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Forgotten Password Pressed\n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Register Window Terminated\n")
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
        app = PasswordRecoveryWindow(root)
        root.mainloop()

from RegisterScreen import *
from MainScreen import *
from PasswordRecoveryScreen import *

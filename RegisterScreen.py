from Tkinter import *
from Constants import *
from TimeStamp import *
from easygui import *
from CreatePopup import *
from BaseModule import *

import re

class RegisterScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Instance of RegisterScreen Class initialised. Self : " + str(self) + " Parent: " + str(parent) + "\n")

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

        menubar.add_cascade(label="File", underline=0, menu=fileMenu)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Menubar Initialised \n")


        self.parent.title(WINDOW_TITLE)

        global EmpLoginEntry
        global EmpLoginEntryTwo
        global EmpPassEntry
        global EmpPassEntryTwo
        global AdminPassEntry
        global SecurityDropdown
        global SecurityAnswerEntry
        global SecurityVar

        AnchorLabel = Label()

        InstructionLabel = Label(text=u'<Insert instructions here>')
        
        EmpLoginLabel = Label(text=u'Employee Login', anchor=CENTER)
        EmpLoginEntry = Entry()

        EmpLoginLabelTwo = Label(text=u'Reenter Employee Login', anchor=CENTER)
        EmpLoginEntryTwo = Entry()
        
        EmpPassLabel = Label(text=u'Employee Password', anchor=CENTER)
        EmpPassEntry = Entry(show="*")

        EmpPassLabelTwo = Label(text=u'Reenter Employee Password', anchor=CENTER)
        EmpPassEntryTwo = Entry(show="*")

        SecurityLabel = Label(text=u"Security Question : ")

        SecurityAnswerLabel = Label(text=u"Security Answer : ")
        SecurityAnswerEntry = Entry()
        
        AdminUserLabel = Label(text=u'Administrator Username', anchor=CENTER)
        AdminUserEntry = Entry()
        
        AdminPassLabel = Label(text=u'Administrator Password', anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Labels \n")

        RegisterButton = Button(text=u"Create Account")
        RegisterButton['command'] = lambda: self.createAccount()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Create Button \n")

        BackButton = Button(text=u"Back")
        BackButton['command'] = lambda: self.goBack()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Return/Back Button \n")

        EmpLoginHelpButton = Button(text=u"?")
        EmpLoginHelpButton['command'] = lambda: self.displayEmpLoginHelp()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded 1st Button \n")

        EmpPassHelpButton = Button(text=u"?")
        EmpPassHelpButton['command'] = lambda: self.displayEmpPassHelp()

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded 2nd Button \n")

        SecurityVarHelpButton = Button(text=u"?")
        SecurityVarHelpButton['command'] = lambda: self.displaySecurityHelp()

        SecurityVar = StringVar(self.parent)
        SecurityVar.set("Mother's Maiden Name")

        SecurityDropdown = OptionMenu(self.parent, SecurityVar, "Mother's Maiden Name", "Memorable Place", "Name of First Pet", "Street you first lived in")

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        EmpLoginLabel.grid(row=2, column=6)
        EmpLoginEntry.grid(row=2, column=7)
        EmpLoginLabelTwo.grid(row=3, column=6)
        EmpLoginEntryTwo.grid(row=3, column=7)
        EmpPassLabel.grid(row=4, column=6)
        EmpPassEntry.grid(row=4, column=7)
        EmpPassLabelTwo.grid(row=5, column=6)
        EmpPassEntryTwo.grid(row=5, column=7)
        SecurityLabel.grid(row=6, column=6)
        SecurityDropdown.grid(row=6, column=7)
        SecurityAnswerLabel.grid(row=7, column=6)
        SecurityAnswerEntry.grid(row=7, column=7)
        SecurityVarHelpButton.grid(row=7, column=8)
        AdminPassLabel.grid(row=8, column=6)
        AdminPassEntry.grid(row=8, column=7)
        EmpLoginHelpButton.grid(row=3, column=8)
        EmpPassHelpButton.grid(row=5, column=8)
        RegisterButton.grid(row=10, column=7)
        BackButton.grid(row=11, column=7)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")

    def onExit(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Quit Selected \n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Window Terminated \n")
    
    def goBack(self):
        
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Back Button Pressed\n")
        self.parent.destroy()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Register Window Terminated\n")
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()

    def displayEmpPassHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Emp Pass Help Button Pressed\n")
        CreatePopup("Employee Passwords must be 8 Characters Long, and contain at least 1 uppercase character, 1 lowercase character and 1 digit.")   
        return

    def displayEmpLoginHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Emp Pass Help Button Pressed\n")
            CreatePopup("This is the Employee's unique login.") 
            return

    def displaySecurityHelp(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + "Security Help Button Pressed\n")
        CreatePopup("This is used to recover your password.")
        return

    def createAccount(self):
        
        LoginDict = pickle.load(open( "LoginData.p", "rb"))
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded LoginData.p \n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Account Creation initiated \n")
        if not isNone(EmpLoginEntry.get()) == True:
            if EmpLoginEntry.get() == EmpLoginEntryTwo.get():
                if EmpLoginEntry.get() in LoginDict:
                    CreatePopup("That Employee Login is already in use.") 
                    return
                elif EmpLoginEntry.get() in RESERVED_NAMES:
                    CreatePopup("That Employee Login is reserved.") 
                    return
            else:
                CreatePopup("The Login fields didn't match.")
                return
        else:
            CreatePopup("Please Enter an Employee Login")
            return
        if EmpPassEntry.get() == EmpPassEntryTwo.get():
            if re.search(r'\d', EmpPassEntry.get()):
                if re.search(r'[A-Z]', EmpPassEntry.get()):
                    if re.search(r'[a-z]', EmpPassEntry.get()):
                        if len(EmpPassEntry.get()) >= 8:
                            with open("AdminPass.txt", 'r') as f:
                                AdminPassHash = f.readline()
                                with open("Log.txt", "a") as f:
                                    f.write(TimeStamp() + " Admin Pass Hash loaded. \n")
                            if str(hash(AdminPassEntry.get())) == str(AdminPassHash):
                                LoginDict.update({hash(EmpLoginEntry.get()):hash(EmpPassEntry.get()),"Security Question":hash(SecurityVar.get()),"Security Answer":hash(SecurityAnswerEntry.get())})
                                pickle.dump( LoginDict, open( "LoginData.p", "wb" ) )
                                CreatePopup("Employee Account Created.")
                                with open("Log.txt", "a") as f:
                                    f.write(TimeStamp() + " New Employee Account : " + str(EmpLoginEntry.get()) + " created. \n")
                                return
                            else:
                                CreatePopup("Incorrect Admin Password.")
                                with open("Log.txt", "a") as f:
                                    f.write(TimeStamp() + " Account Creation - Incorrect Admin pass. \n")
                                return
                        else:
                             CreatePopup("Your password must contain at least 8 characters.")
                             return
                    else:
                         CreatePopup("Your password must contain at least 1 Lowercase letter.")
                         return
                else:
                     CreatePopup("Your password must contain at least 1 Uppercase letter.")
                     return
            else:
                 CreatePopup("Your password must contain at least 1 Digit.")
                 return
        else:
            CreatePopup("The Password Fields didn't match.")
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Account Creation - Password Mismatch. \n")
            return
                
                
                  

from LoginForm import *


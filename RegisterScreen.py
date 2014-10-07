from Tkinter import *
from TimeStamp import *
from easygui import *
from CreatePopup import *
from BaseModule import *
from Constants import *

import re

class RegisterScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + REGISTERSCREEN_INSTANCE_CREATED_TEXT + str(self) + PARENT_TEXT + str(parent) + "\n")

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISING_LOGINSCREEN_TEXT)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        
        fileMenu.add_command(label=DROPDOWN_BACK_TEXT, underline=0, command=self.onBack)

        fileMenu.add_separator()

        fileMenu.add_command(label=DROPDOWN_HELP_TEXT, underline=0, command=self.Help)

        fileMenu.add_separator()

        menubar.add_cascade(label=DROPDOWN_FILE_TEXT, underline=0, menu=fileMenu)

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + MENUBAR_INITIALISED_TEXT)


        self.parent.title(WINDOW_TITLE)

        global EmpLoginEntry
        global EmpLoginEntryTwo
        global EmpPassEntry
        global EmpPassEntryTwo
        global AdminPassEntry
        global SecurityDropdown
        global SecurityAnswerEntry

        AnchorLabel = Label()
        
        EmpLoginLabel = Label(text=EMP_LOGIN_LABEL_TEXT, anchor=CENTER)
        EmpLoginEntry = Entry()

        EmpLoginLabelTwo = Label(text=EMP_LOGIN_LABEL_TWO_TEXT, anchor=CENTER)
        EmpLoginEntryTwo = Entry()
        
        EmpPassLabel = Label(text=EMP_PASS_LABEL_TEXT, anchor=CENTER)
        EmpPassEntry = Entry(show="*")

        EmpPassLabelTwo = Label(text=EMP_PASS_LABEL_TWO_TEXT, anchor=CENTER)
        EmpPassEntryTwo = Entry(show="*")

        SecurityLabel = Label(text=SECURITY_LABEL_TEXT)

        SecurityAnswerLabel = Label(text=SECURITY_ANSWER_LABEL_TEXT)
        SecurityAnswerEntry = Entry()
        
        AdminPassLabel = Label(text=ADMIN_PASS_LABEL_TEXT, anchor=CENTER)
        AdminPassEntry = Entry(show="*")

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_LABELS_TEXT)

        RegisterButton = Button(text=REGISTER_BUTTON_TEXT)
        RegisterButton['command'] = lambda: self.createAccount()

        BackButton = Button(text=BACK_BUTTON_TEXT)
        BackButton['command'] = lambda: self.onBack()

        EmpLoginHelpButton = Button(text=u"?")
        EmpLoginHelpButton['command'] = lambda: self.displayEmpLoginHelp()

        EmpPassHelpButton = Button(text=u"?")
        EmpPassHelpButton['command'] = lambda: self.displayEmpPassHelp()

        SecurityVarHelpButton = Button(text=u"?")
        SecurityVarHelpButton['command'] = lambda: self.displaySecurityHelp()

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_BUTTONS_TEXT)

        SecurityVar = StringVar(self.parent)
        SecurityVar.set(SECURITY_VAR_MAIDEN_NAME_TEXT)

        SecurityDropdown = OptionMenu(self.parent, SecurityVar, SECURITY_VAR_MAIDEN_NAME_TEXT, SECURITY_VAR_MEMORABLE_TEXT, SECURITY_VAR_FIRST_PET_TEXT, SECURITY_VAR_FIRST_STREET_TEXT)

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

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISED_GRID_UI_TEXT)
    
    def onBack(self):
        
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + BACK_BUTTON_PRESSED_TEXT)
        self.parent.destroy()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + REGISTER_WINDOW_TERMINATED_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()

    def Help(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + HELP_SELECTED_TEXT)
        CreatePopup(REGISTER_SCREEN_HELP_POPUP_TEXT)

    def displayEmpPassHelp(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + EMP_PASS_HELP_PRESSED_TEXT)
        CreatePopup(EMP_PASS_HELP_TEXT)   
        return

    def displayEmpLoginHelp(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + EMP_PASS_HELP_PRESSED_TEXT)
            CreatePopup(EMP_LOGIN_HELP_TEXT) 
            return

    def displaySecurityHelp(self):

        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + SECURITY_HELP_BUTTON_PRESSED_TEXT)
        CreatePopup(SECURITY_HELP_TEXT)
        return

    def createAccount(self):
        
        LoginDict = pickle.load(open( "LoginData.p", "rb"))
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_LOGIN_DICT_TEXT)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + ACCOUNT_CREATION_INITIATED_TEXT)
        if not isNone(EmpLoginEntry.get()) == True:
            if EmpLoginEntry.get() == EmpLoginEntryTwo.get():
                if EmpLoginEntry.get() in LoginDict:
                    CreatePopup(USERNAME_IN_USE_TEXT) 
                    return
                elif EmpLoginEntry.get() in RESERVED_NAMES:
                    CreatePopup(USERNAME_RESERVED_TEXT) 
                    return
            else:
                CreatePopup(LOGIN_FIELD_MISMATCH_TEXT)
                return
        else:
            CreatePopup(LOGIN_FIELD_MISSING_TEXT)
            return
        if EmpPassEntry.get() == EmpPassEntryTwo.get():
            if re.search(r'\d', EmpPassEntry.get()):
                if re.search(r'[A-Z]', EmpPassEntry.get()):
                    if re.search(r'[a-z]', EmpPassEntry.get()):
                        if len(EmpPassEntry.get()) >= 8:
                            with open("AdminPass.txt", 'r') as f:
                                AdminPassHash = f.readline()
                                with open(LOG_FILENAME, "a") as f:
                                    f.write(TimeStamp() + ADMIN_PASS_HASH_LOADED_TEXT)
                            if str(hash(AdminPassEntry.get())) == str(AdminPassHash):
                                LoginDict.update({hash(EmpLoginEntry.get()):hash(EmpPassEntry.get()),hash(SECURITY_QUESTION_TEXT):hash(SecurityVar.get()),hash(SECURITY_QUESTION_ANSWER_TEXT):hash(SecurityAnswerEntry.get())})
                                pickle.dump( LoginDict, open( "LoginData.p", "wb" ) )
                                CreatePopup(EMP_ACCOUNT_CREATED_TEXT)
                                with open(LOG_FILENAME, "a") as f:
                                    f.write(TimeStamp() + NEW_EMPLOYEE_ACCOUNT_TEXT + str(EmpLoginEntry.get()) + CREATED_TEXT)
                                self.goBack()
                            else:
                                CreatePopup(INCORRECT_ADMIN_PASS_TEXT)
                                with open(LOG_FILENAME, "a") as f:
                                    f.write(TimeStamp() + INCORRECT_ADMIN_PASS_LOG_TEXT)
                                return
                        else:
                             CreatePopup(PASS_LENGTH_TEXT)
                             return
                    else:
                         CreatePopup(PASS_LOWERCASE_TEXT)
                         return
                else:
                     CreatePopup(PASS_UPPERCASE_TEXT)
                     return
            else:
                 CreatePopup(PASS_DIGIT_TEXT)
                 return
        else:
            CreatePopup(PASS_MISMATCH_TEXT)
            with open(LOG_FILENAME, "a") as f:
                f.write(TimeStamp() + ACCOUNT_CREATION_PASSWORD_MISMATCH_TEXT)
            return
                
                
                  
from Constants import *
from LoginForm import *


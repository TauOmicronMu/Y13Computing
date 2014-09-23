from Tkinter import *
from Constants import *
from TimeStamp import *
from easygui import *

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

        AnchorLabel = Label()

        InstructionLabel = Label(text=u'<Insert instructions here>')
        
        EmpLoginLabel = Label(text=u'Employee Login', anchor=CENTER)
        EmpLoginEntry = Entry()

        EmpLoginLabelTwo = Label(text=u'Reenter Employee Login', anchor=CENTER)
        EmpLoginEntryTwo = Entry()
        
        EmpPassLabel = Label(text=u'Employee Password', anchor=CENTER)
        EmpPassEntry = Entry()

        EmpPassLabelTwo = Label(text=u'Reenter Employee Password', anchor=CENTER)
        EmpPassEntryTwo = Entry(show="*")
        
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

        global EmpLoginEntry
        global EmpLoginEntryTwo

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        EmpLoginLabel.grid(row=2, column=6)
        EmpLoginEntry.grid(row=2, column=7)
        EmpLoginLabelTwo.grid(row=3, column=6)
        EmpLoginEntryTwo.grid(row=3, column=7)
        EmpPassLabel.grid(row=4, column=6)
        EmpPassEntry.grid(row=4, column=7)
        EmpPassLabelTwo.grid(row=5, column=6)
        EmpPassEntryTwo.grid(row=5, column=7)
        AdminPassLabel.grid(row=6, column=6)
        AdminPassEntry.grid(row=6, column=7)
        RegisterButton.grid(row=9, column=7)
        BackButton.grid(row=10, column=7)

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

    def createAccount(self):

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Account Creation initiated \n")
        if EmpLoginEntry.get() == EmpLoginEntryTwo.get():
            with open('LoginNames.txt', 'r') as f:
                LoginNames = f.readlines()
                for name in LoginNames:
                    if EmpLoginEntry.get() == name:
                        msgbox(msg="(That Employee Login is already in use.)", title=WINDOW_TITLE, ok_button="OK")   
                        return
                    else:
                        pass
                
                  

from LoginForm import *


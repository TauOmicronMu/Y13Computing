from Tkinter import *
from Constants import *
from TimeStamp import *

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

        self.parent.title(WINDOW_TITLE)

        AnchorLabel = Label()

        InstructionLabel = Label(text=u'<Insert instructions here>')
        
        EmpCodeLabel = Label(text=u'Employee Code', anchor=CENTER)
        EmpCodeEntry = Entry()
        
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

        AnchorLabel.grid(pady=35,padx=130,row=0,column=0)
        EmpCodeLabel.grid(row=2, column=6)
        EmpCodeEntry.grid(row=2, column=7)
        EmpPassLabel.grid(row=3, column=6)
        EmpPassEntry.grid(row=3, column=7)
        EmpPassLabelTwo.grid(row=4, column=6)
        EmpPassEntryTwo.grid(row=4, column=7)
        AdminPassLabel.grid(row=5, column=6)
        AdminPassEntry.grid(row=5, column=7)
        RegisterButton.grid(row=8, column=7)

        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialised Grid. UI Initialisation Complete. \n")

        


def main():

    root = Tk()
    root.geometry(WINDOW_GEOMETRY)
    with open("Log.txt", "a") as f:
        f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
    app = RegisterScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()  
    

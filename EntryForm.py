from Tkinter import *

class LoginScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initialiseUI()

    def initialiseUI(self):

        self.parent.title("Employee Tracker 1.0.0 (c)")

        global UsernameEntry
        global PasswordEntry

        ImageLeft = PhotoImage(file="EmpTrackerImageLeft.gif")
        global LogoLeft
        LogoLeft = Label(self.parent, image=ImageLeft)
        LogoLeft.image = ImageLeft

        ImageRight = PhotoImage(file="EmpTrackerImageRight.gif")
        global LogoRight
        LogoRight = Label(self.parent, image=ImageRight)
        LogoRight.image = ImageRight

        AnchorLabel = Label()
        UsernameLabel = Label(text=u'Username',anchor=CENTER)
        UsernameEntry = Entry()
        PasswordLabel = Label(text=u'Password',anchor=CENTER)
        PasswordEntry = Entry(show="*")
        LoginButton = Button(text=u'Login')
        LoginButton['command'] = lambda: self.printInput()
        
        AnchorLabel.grid(pady=35,padx=90,row=0,column=0)
        LogoLeft.grid(pady=20, padx=0,row=1,column=6)
        LogoRight.grid(pady=20, padx=0, row=1, column=7)
        UsernameLabel.grid(row=2, column=6)
        UsernameEntry.grid(row=2, column=7)
        PasswordLabel.grid(row=3, column=6)
        PasswordEntry.grid(row=3, column=7)
        LoginButton.grid(row=4, column=8)

    def printInput(self):
        print UsernameEntry.get()
        print hash(PasswordEntry.get())

def main():
    
    root = Tk()
    root.geometry("900x600+200+50")
    app = LoginScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()  

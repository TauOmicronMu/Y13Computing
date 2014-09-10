#============================================================
#=========================  Main  ===========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

from Tkinter import *
from BaseModule import *
from LoginForm import *
from InitialSetup import *
from Constants import *
    
def main():
    
    Setup()
    root = Tk()
    root.geometry(WINDOW_GEOMETRY)
    with open("Log.txt", "a") as f:
        f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
    app = LoginScreen(root)
    root.mainloop()

if __name__ == '__main__':
    main()  

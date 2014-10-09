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
from logging import *
from TimeStamp import *
from InitSetupPopup import *

basicConfig(filename=LOG_FILENAME,level=DEBUG,)
    
def main():

    try:
        Setup()
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + " Initialising window of with geometry: " + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()
    except:
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp(),)
        exception('Got exception on main handler')
        raise

if __name__ == '__main__':
    main()  

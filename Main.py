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
from CreatePopup import *

import pickle

from LoggingStringsEnglish import *

basicConfig(filename=LOG_FILENAME,level=DEBUG,)
    
def main():

    try:
        Setup()
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_WINDOW_TEXT + WINDOW_GEOMETRY + "\n") 
        app = LoginScreen(root)
        root.mainloop()
    except:
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp(),)
        exception(GOT_MAIN_EXCEPTION)
        raise

if __name__ == '__main__':
    main()  

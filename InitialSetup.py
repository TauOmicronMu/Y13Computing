#============================================================
#=====================  Initial Setup  ======================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

from Constants import *
from TimeStamp import *
from Tkinter import *
from InitSetupPopup import *

import pickle

def Setup(): #Procedure defining the Initial Setup for EmpTracker.

    global empCount
    global totalSalary
    global totalExpenditure
    global array

    Setup = False
    array = [] #Creates a blank array, which is used to store employee's data-dictionaries.

    with open(CURRENT_EMP_FILENAME, WRITE_MODE) as f:
        f.write("")
        
    with open(LOG_FILENAME, APPEND_MODE) as f:
        f.write(TimeStamp() + RESTART_TEXT)
        
    with open(LOG_FILENAME, APPEND_MODE) as f:
        f.write(TimeStamp() + CREATED_OR_WIPED_CURRENT_EMP_TEXT)
        
    f = open(INITIAL_SETUP_FILENAME, APPEND_MODE) #Ensures that the file "InitialSetup.txt" exists.

    f = open(INITIAL_SETUP_FILENAME, READ_MODE)
    
    searchlines = f.readlines() #Creates a second definition of the function f.readlines()
    for i, line in enumerate(searchlines): #Searches the file
       if "True" in line:
           Setup = True
           
    if Setup == True:
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADING_VARIABLES_TEXT)
            
        f = open(EMP_COUNT_FILENAME, READ_MODE)
        with open(EMP_COUNT_FILENAME, READ_MODE) as f:
            empCountList = f.readlines()
            empCount = int(empCountList[0])
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_EMP_COUNT_TEXT)
            
        f = open(TOTAL_SALARY_FILENAME, READ_MODE)
        with open(TOTAL_SALARY_FILENAME, READ_MODE):
            totalSalaryList = f.readlines()
            totalSalary = int(totalSalaryList[0])
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_TOTAL_SALARY_TEXT)
            
        f = open(TOTAL_EXPENDITURE_FILENAME, READ_MODE)
        with open(TOTAL_EXPENDITURE_FILENAME, READ_MODE) as f:
            totalExpenditureList = f.readlines()
            totalExpenditure = int(totalExpenditureList[0])
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + LOADED_TOTAL_EXPENDITURE_TEXT)
            
        with open(CURRENT_EMP_FILENAME, WRITE_MODE) as f:
            f.write("")
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_OR_WIPED_CURRENT_EMP_TEXT)
    else:
        LoginData = {}
        pickle.dump( LoginData, open(LOGIN_DATA_FILENAME, WRITE_BINARY_MODE ) )

        EmpDatabase = []
        with open(EMP_DATABASE_FILENAME, WRITE_MODE) as f:
            f.write("%s" %EmpDatabase)

        pickle.dump(0, open(LOGIN_SECURITY_FILENAME, WRITE_BINARY_MODE))

        EmpCodes = []
        pickle.dump( EmpCodes, open(EMPCODE_FILENAME, WRITE_BINARY_MODE) )

        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIATING_FIRST_TIME_SETUP_TEXT)
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_LOGINNAMES_TEXT)

        with open(LANGUAGE_FILENAME, WRITE_MODE) as f:
            f.write("ENGLISH")
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_LANGUAGE_FILE_TEXT)
            
        totalSalary = 0
        empCount = 0
        totalExpenditure = 0
        
        f = open(EMP_COUNT_FILENAME, WRITE_MODE)
        with open(EMP_COUNT_FILENAME, WRITE_MODE) as f:
            f.write("%s\n" %empCount)
            f.close()
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_EMPCOUNT_TEXT)
        f = open(TOTAL_SALARY_FILENAME, WRITE_MODE)
        
        with open(TOTAL_SALARY_FILENAME, WRITE_MODE) as f:
             f.write("%s\n" %totalSalary)
             f.close()
             
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_TOTALSALARY_TEXT)
            
        f = open(TOTAL_EXPENDITURE_FILENAME, WRITE_MODE)
        with open(TOTAL_EXPENDITURE_FILENAME, WRITE_MODE) as f:
            f.write("%s\n" %totalExpenditure)
            f.close()
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_TOTALEXPENDITURE_TEXT)
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + FIRST_TIME_ADMIN_PASS_SETUP_TEXT)
            
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + INITIALISING_INITSETUPPOPUP_TEXT)
            
        app = InitSetupPopup(root)
        root.mainloop()
        
        f = open(INITIAL_SETUP_FILENAME, WRITE_MODE) #Creates the file "InitialSetup.txt"

        with open(INITIAL_SETUP_FILENAME, WRITE_MODE) as f:
            f.write("True") #Writes "True" to the file "InitialSetup.txt", which will be used to check whether setup is complete.
            f.close()
            
        with open(LOG_FILENAME, APPEND_MODE) as f:
            f.write(TimeStamp() + CREATED_INITIALSETUP_TEXT)
        

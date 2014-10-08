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
from Strings import *

import pickle

def Setup(): #Procedure defining the Initial Setup for EmpTracker.

    from easygui import *

    global empCount
    global totalSalary
    global totalExpenditure
    global array

    Setup = False
    array = [] #Creates a blank array, which is used to store employee's data-dictionaries.

    with open("CurrentEmployee.txt", "w") as f:
        f.write("")
    with open(LOG_FILENAME, "a") as f:
        f.write(TimeStamp() + RESTART_TEXT)
    with open(LOG_FILENAME, "a") as f:
        f.write(TimeStamp() + CREATED_OR_WIPED_CURRENT_EMP_TEXT)
    f = open('EmpCodeList.txt','w')
    with open('EmpCodeList.txt','w') as f:
        f.close()
    f = open('InitialSetup.txt','a') #Ensures that the file "InitialSetup.txt" exists.
    f = open('InitialSetup.txt','r')
    searchlines = f.readlines() #Creates a second definition of the function f.readlines()
    for i, line in enumerate(searchlines): #Searches the file
       if "True" in line:
           Setup = True
    if Setup == True:
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADING_VARIABLES_TEXT)
        f = open('EmpCount.txt','r')
        with open('EmpCount.txt','r') as f:
            empCountList = f.readlines()
            empCount = int(empCountList[0])
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_EMP_COUNT_TEXT)
        f = open('TotalSalary.txt','r')
        with open('TotalSalary.txt','r'):
            totalSalaryList = f.readlines()
            totalSalary = int(totalSalaryList[0])
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_TOTAL_SALARY_TEXT)
            f = open('TotalExpenditure.txt','r')
        with open('TotalExpenditure.txt','r') as f:
            totalExpenditureList = f.readlines()
            totalExpenditure = int(totalExpenditureList[0])
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + LOADED_TOTAL_EXPENDITURE_TEXT)
        with open('CurrentEmployee.txt','w') as f:
            f.write("")
        with open(v, "a") as f:
            f.write(TimeStamp() + CREATED_OR_WIPED_CURRENT_EMP_TEXT)
    else:
        LoginData = {}
        pickle.dump( LoginData, open( "LoginData.p", "wb" ) )
        EmpDatabase = {}
        pickle.dump( EmpDatabase, open("EmpDatabase.p", "wb") )
        EmpCodes = []
        pickle.dump( EmpCodes, open("EmpCodes.p", "wb") )
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIATING_FIRST_TIME_SETUP_TEXT)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + CREATED_LOGINNAMES_TEXT)
        f = open('EmpDatabase.txt','a') #Ensures that the file "EmpDatabase.txt" exists.
        with open('EmpDatabase.txt','a'):
            f.close()
        totalSalary = 0
        empCount = 0
        totalExpenditure = 0
        f = open('EmpCount.txt','w')
        with open('EmpCount.txt','w') as f:
            f.write("%s\n" %empCount)
            f.close()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + CREATED_EMPCOUNT_TEXT)
        f = open('TotalSalary.txt','w')
        with open('TotalSalary.txt','w') as f:
             f.write("%s\n" %totalSalary)
             f.close()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + CREATED_TOTALSALARY_TEXT)
        f = open('TotalExpenditure.txt','w')
        with open('TotalExpenditure.txt','w') as f:
            f.write("%s\n" %totalExpenditure)
            f.close()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + CREATED_TOTALEXPENDITURE_TEXT)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + FIRST_TIME_ADMIN_PASS_SETUP_TEXT)
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + INITIALISING_INITSETUPPOPUP_TEXT) 
        app = InitSetupPopup(root)
        root.mainloop()
        f = open('InitialSetup.txt','w') #Creates the file "InitialSetup.txt"
        with open('InitialSetup.txt','w') as f:
            f.write("True") #Writes "True" to the file "InitialSetup.txt", which will be used to check whether setup is complete.
            f.close()
        with open(LOG_FILENAME, "a") as f:
            f.write(TimeStamp() + CREATED_INITIALSETUP_TEXT)
        

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

    from easygui import *

    global empCount
    global totalSalary
    global totalExpenditure
    global array

    Setup = False
    array = [] #Creates a blank array, which is used to store employee's data-dictionaries.

    with open("CurrentEmployee.txt", "w") as f:
        f.write("")
    with open("Log.txt", "a") as f:
        f.write(TimeStamp() + "=====RESTART=====\n")
    with open("Log.txt", "a") as f:
        f.write(TimeStamp() + "Created/Wiped CurrentEmployee.txt\n")
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
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loading variables\n")
        f = open('EmpCount.txt','r')
        with open('EmpCount.txt','r') as f:
            empCountList = f.readlines()
            empCount = int(empCountList[0])
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Employee Count\n")
        f = open('TotalSalary.txt','r')
        with open('TotalSalary.txt','r'):
            totalSalaryList = f.readlines()
            totalSalary = int(totalSalaryList[0])
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Total Salary\n")
            f = open('TotalExpenditure.txt','r')
        with open('TotalExpenditure.txt','r') as f:
            totalExpenditureList = f.readlines()
            totalExpenditure = int(totalExpenditureList[0])
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Loaded Total Expenditure\n")
        with open('CurrentEmployee.txt','w') as f:
            f.write("")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Wiped CurrentEmployee.txt\n")
    else:
        LoginData = {}
        pickle.dump( LoginData, open( "LoginData.p", "wb" ) )
        EmpDatabase = {}
        pickle.dump( EmpDatabase, open("EmpDatabase.p", "wb") )
        EmpCodes = {}
        pickle.dump( EmpCodes, open("EmpCodes.p", "wb") )
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initiating first-time setup\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created LoginNames.txt \n")
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
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created EmpCount.txt\n")
        f = open('TotalSalary.txt','w')
        with open('TotalSalary.txt','w') as f:
             f.write("%s\n" %totalSalary)
             f.close()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created TotalSalary.txt\n")
        f = open('TotalExpenditure.txt','w')
        with open('TotalExpenditure.txt','w') as f:
            f.write("%s\n" %totalExpenditure)
            f.close()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created TotalExpenditure.txt\n")
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " First time Admin password Setup\n")
        root = Tk()
        root.geometry(WINDOW_GEOMETRY)
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initialising Popup window.\n") 
        app = InitSetupPopup(root)
        root.mainloop()
        f = open('InitialSetup.txt','w') #Creates the file "InitialSetup.txt"
        with open('InitialSetup.txt','w') as f:
            f.write("True") #Writes "True" to the file "InitialSetup.txt", which will be used to check whether setup is complete.
            f.close()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created InitialSetup.txt\n")
        

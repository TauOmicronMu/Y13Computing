#============================================================
#=====================  Initial Setup  ======================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

from Constants import *
from TimeStamp import *

def Setup(): #Procedure defining the Initial Setup for EmpTracker.

    from easygui import *

    global empCount
    global totalSalary
    global totalExpenditure
    global array

    Setup = False
    array = [] #Creates a blank array, which is used to store employee's data-dictionaries.

    with open("Log.txt", "a") as f:
        f.write(TimeStamp() + "=====RESTART=====\n")
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
        with open("LoginNames.txt", "a") as f:
            ReservedNames = RESERVED_NAMES
            for name in RESERVED_NAMES:
                f.write(name + "\n")
    else:
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Initiating first-time setup\n")
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
        f = open('InitialSetup.txt','w') #Creates the file "InitialSetup.txt"
        with open('InitialSetup.txt','w') as f:
            f.write("True") #Writes "True" to the file "InitialSetup.txt", which will be used to check whether setup is complete.
            f.close()
        with open("Log.txt", "a") as f:
            f.write(TimeStamp() + " Created InitialSetup.txt\n")
        while True:
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " First time Admin password Setup\n")
            AdminPass = passwordbox(msg='Input a Password for the Administrator: ', title=WINDOW_TITLE, default='', image=None, root=None)
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Allowing Password input (1)\n")
            AdminPassCheck = passwordbox(msg='Please confirm the Password: ', title=WINDOW_TITLE, default='', image=None, root=None)
            with open("Log.txt", "a") as f:
                f.write(TimeStamp() + " Allowing Password input (2)\n")
            if AdminPass == AdminPassCheck:
                with open('AdminPass.txt','w') as f:
                    f.write("%s" %hash(AdminPass))
                    with open("Log.txt", "a") as f:
                        f.write(TimeStamp() + " Saved hashed Admin Pass to Adminpass.txt\n")
                break
            else:
                msgbox(msg='The passwords didnt match.', title=WINDOW_TITLE, ok_button='OK',image=None, root = None)
                with open("Log.txt", "a") as f:
                    f.write(TimeStamp() + " Password Creation failed : Mismatch\n")

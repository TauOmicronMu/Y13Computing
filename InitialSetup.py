#============================================================
#=====================  Initial Setup  ======================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

def Setup(): #Procedure defining the Initial Setup for EmpTracker.

    from easygui import *

    global empCount
    global totalSalary
    global totalExpenditure
    global array

    Setup = False
    array = [] #Creates a blank array, which is used to store employee's data-dictionaries.

    
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
        f = open('EmpCount.txt','r')
        with open('EmpCount.txt','r') as f:
            empCountList = f.readlines()
            empCount = int(empCountList[0])
        f = open('TotalSalary.txt','r')
        with open('TotalSalary.txt','r'):
            totalSalaryList = f.readlines()
            totalSalary = int(totalSalaryList[0])
            f = open('TotalExpenditure.txt','r')
        with open('TotalExpenditure.txt','r') as f:
            totalExpenditureList = f.readlines()
            totalExpenditure = int(totalExpenditureList[0])                            
    else:
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
        f = open('TotalSalary.txt','w')
        with open('TotalSalary.txt','w') as f:
             f.write("%s\n" %totalSalary)
             f.close()
        f = open('InitialSetup.txt','w') #Creates the file "InitialSetup.txt"
        with open('InitialSetup.txt','w') as f:
            f.write("True") #Writes "True" to the file "InitialSetup.txt", which will be used to check whether setup is complete.
            f.close()
        f = open('TotalExpenditure.txt','w')
        with open('TotalExpenditure.txt','w') as f:
            f.write("%s\n" %totalExpenditure)
            f.close()
        while True:
            AdminPass = passwordbox(msg='Input a Password for the Administrator: ', title='Employee Tracker', default='', image=None, root=None)
            AdminPassCheck = passwordbox(msg='Please confirm the Password: ', title='Employee Tracker', default='', image=None, root=None)
            if AdminPass == AdminPassCheck:
                with open('AdminPass.txt','w') as f:
                    f.write("%s" %hash(AdminPass))
                break
            else:
                msgbox(msg='The passwords didnt match.', title='Employee Tracker', ok_button='OK',image=None, root = None)

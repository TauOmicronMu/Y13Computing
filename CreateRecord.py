#============================================================
#======================  New Record  ========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

from BaseModule import *
from easygui import *

global name
global nameCheck
global Unique_Code

EmployeeCreated = False
NameComplete = False
DepartmentComplete = False

def CreateRecord():
    while EmployeeCreated == False:
        while NameComplete == False:
            name = enterbox(msg='Input Employee Name: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
            if isNone(name) == True:
                msgbox(msg='Please enter a name.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            elif isInt(name) == True:
                msgbox(msg='Please enter a valid name.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            else:
                nameCheck = enterbox(msg='Reenter Employee Name: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
                if isNone(name) == True:
                    msgbox(msg='Please enter a name.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif isInt(name) == True:
                    msgbox(msg='Please enter a valid name.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif name != nameCheck:
                    msgbox(msg='The Names didnt match. Please try again.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                else:
                    NameComplete == True
                    break

#TODO : Department, DOB, Gender, Salary
#TODO : Unique Code
#TODO : Update base files.

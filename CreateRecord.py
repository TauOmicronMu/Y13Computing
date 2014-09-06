#============================================================
#======================  New Record  ========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

from BaseModule import *
from easygui import *
from GenerateCode import *

global UniqueCode

EmployeeCreated = False
NameComplete = False
DepartmentComplete = False
DOBComplete = False
GenderComplete = False
SalaryComplete = False


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
        while DepartmentComplete == False:
            department = enterbox(msg='Input Employee Department: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
            if isNone(department) == True:
                msgbox(msg='Please enter a department.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            elif isInt(department) == True:
                msgbox(msg='Please enter a valid department.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            else:
                departmentCheck = enterbox(msg='Reenter Employee Department: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
                if isNone(departmentCheck) == True:
                    msgbox(msg='Please enter a department.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif isInt(departmentCheck) == True:
                    msgbox(msg='Please enter a valid department.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif department != departmentCheck:
                    msgbox(msg='The departments didnt match. Please try again.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                else:
                    DepartmentComplete == True
                    break
        while DOBComplete == False:
            DOB = enterbox(msg='Input Employee DOB (DD/MM/YY): ', title='Employee Tracker', default='', strip=True, image=None, root=None)
            if isNone(DOB) == True:
                msgbox(msg='Please enter a DOB.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            elif DOBCheck(DOB) == True:
                msgbox(msg='Please enter a valid DOB.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            else:
                DOBCheck = enterbox(msg='Reenter Employee DOB: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
                if isNone(DOBCheck) == True:
                    msgbox(msg='Please enter a DOB.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif DOBCheck(DOBCheck) != True:
                    msgbox(msg='Please enter a valid DOB.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif DOB != DOBCheck:
                    msgbox(msg='The DOBs didnt match. Please try again.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                else:
                    DOBComplete == True
                    break
        while GenderComplete == False:
            gender = choicebox(msg='Choose Employee Gender', title='Employee Tracker', choices=('M','F'))
            if isNone(gender) == True:
                msgbox(msg='Please enter a Gender.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            else:
                genderCheck = choicebox(msg='Choose Employee Gender', title='Employee Tracker', choices=('M','F'))
                if isNone(genderCheck) == True:
                    msgbox(msg='Please enter a Gender.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif gender != genderCheck:
                    msgbox(msg='The Genders didnt match. Please try again.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                else:
                    GenderComplete == True
                    break
        while SalaryComplete == False:
            salary = enterbox(msg='Input Employee Salary: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
            if isNone(salary) == True:
                msgbox(msg='Please enter a salary.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            elif isInt(salary) != True:
                msgbox(msg='Please enter a valid salary.', title='Employee Tracker', ok_button='OK', image=None, root=None)
            else:
                salaryCheck = enterbox(msg='Reenter Employee Salary: ', title='Employee Tracker', default='', strip=True, image=None, root=None)
                if isNone(salaryCheck) == True:
                    msgbox(msg='Please enter a salary.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif isInt(salaryCheck) != True:
                    msgbox(msg='Please enter a valid salary.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                elif salary != salaryCheck:
                    msgbox(msg='The salaries didnt match. Please try again.', title='Employee Tracker', ok_button='OK', image=None, root=None)
                else:
                    SalaryComplete == True
                    break
        UniqueCode = GenerateCode()

#TODO : Create employee record.
#TODO : Update base files.

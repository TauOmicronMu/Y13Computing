#============================================================
#======================  Base Module  =======================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

import datetime


#============================================================
#====================     Type Checks    ====================
#============================================================
        
def isFloat(n): #Checks to see if a given input is a Float.
    try:
        float(n)
        return True
    except ValueError:
        return False

def isInt(n): #Checks to see if a given input is an Integer.
    try:
        int(n)
        return True
    except ValueError:
        return False

def isNone(n): #Checks to see if a given input is nonetype
    if (n is None) or (len(n) == 0):
        return True
    else:
        return False

#============================================================
#====================   Format Checks   =====================
#============================================================

def DOBCheck(n):
    #CurrentDate = str(datetime.date.today.day()) + "/" + str(datetime.date.today.month()) + "/" + str(datetime.date.today.year()
    MonthsWith30Days = ["09","04","06","11"]
    if isInt(n[0:2]) == True and isInt(n[3:5]) == True and isInt(n[6:]) == True:
        if n[2] == "/" and n[5] == "/":
            #if not(n > CurrentDate):
            if int(n[3:5]) <= 12:
                if int(n[3:5]) == 02: #If the month is February
                    if int(n[6:]) % 4 == 0: #If it is a Leap Year
                        if int(n[0:2]) <= 29: #29 Days in Feb in a Leap Year
                            return True
                        else:
                            return False
                    else: #If it isn't a Leap Year
                        if int(n[0:2]) <= 28: #28 Days in Feb in a 'Regular' Year
                            return True
                        else:
                            return False
                else: #If it isn't February
                    if n[3:5] in MonthsWith30Days:
                        if int(n[3:5]) <= 30:
                            return True
                        else:
                            return False
                    else:
                        if int(n[3:5]) <= 31:
                            return True
                        else:
                            return False
            else:
                return False
            #else:
                return False
        else:
            return False
    else:
        return False

def GenderCheck(x):
    if x.lower() == "m" or x.lower() == "f":
        return True
    else:
        return False

def SalaryCheck(n):
    if isInt(n) == True:
        return True
    else:
        return False

#============================================================
#====================    Clear Screen    ====================
#============================================================
        
def ClearScreen():
    for i in range(50):
        print("")


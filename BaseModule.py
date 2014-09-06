#============================================================
#======================  Base Module  =======================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

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
    if isInt(n[0:2]) == True and isInt(n[3:5]) == True and isInt(n[6:]) == True:
        if n[2] == "/" and n[5] == "/":
            return True
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


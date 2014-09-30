#============================================================
#======================  Code Gen. ==========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

import random
import pickle

def GenerateCode():
    CodeCreated = False
    EmpDatabase = pickle.load(open("EmpDatabase.p", "rb") )
    while not CodeCreated:
        EmpCode = "EMP" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "E"
        if EmpCode in EmpDatabase:
            pass
        else:
            CodeCreated = True
    return EmpCode

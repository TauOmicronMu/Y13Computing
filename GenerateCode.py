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
    EmpDatabase = pickle.load(open(EMP_DATABASE_FILENAME, READ_BINARY_MODE) )
    while not CodeCreated:
        EmpCode = "EMP" + str(random.randint(1,9)) + \
                  str(random.randint(1,9)) + str(random.randint(1,9)) + \
                  str(random.randint(1,9)) + str(random.randint(1,9)) + \
                  str(random.randint(1,9)) + str(random.randint(1,9)) + "E"
        if EmpCode in EmpDatabase:
            pass
        else:
            CodeCreated = True
    return EmpCode

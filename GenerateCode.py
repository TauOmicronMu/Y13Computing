#============================================================
#======================  Code Gen. ==========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================
from Constants import *

import random
import pickle

def GenerateCode():
    CodeCreated = False
    with open(EMP_DATABASE_FILENAME, READ_MODE) as f:
        EmpDatabase = eval(f.readline())
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

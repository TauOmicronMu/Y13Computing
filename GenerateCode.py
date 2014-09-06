#============================================================
#======================  Code Gen. ==========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

import random

def GenerateCode():
    EmpCode = "EMP" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9)) + "E"
    return EmpCode

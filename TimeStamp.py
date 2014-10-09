from Constants import *

import datetime
import time

def TimeStamp():
    with open(CURRENT_EMP_FILENAME, READ_MODE) as f:
        Username = f.readline()
    ts = time.time()
    return "[" + str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "]" + " [" + Username + "]"
    

import datetime
import time

def TimeStamp():
    with open("CurrentEmployee.txt", "r") as f:
        Username = f.readline()
    ts = time.time()
    return "[" + str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "]" + " [" + Username + "]"
    

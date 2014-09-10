import datetime
import time

def TimeStamp():
    ts = time.time()
    return "[" + str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')) + "]"
    

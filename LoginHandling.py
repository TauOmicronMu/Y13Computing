#============================================================
#========================  Login   ==========================
#============================================================
#================= Author: T.A.Goodman 2014 =================
#=============== Copyright: T.A.Goodman 2014 ================
#============================================================

#============================================================
#====================   Login Handling   ====================
#============================================================
    
def Login():
    from easygui import *
    global LoginAttempt
    LoginAttempt = 0
    global LoginSuccessful
    LoginSuccessful = False
    while True:
        import getpass
        Password = passwordbox(msg='Password: ', title='Employee Tracker', default='', image=None, root=None)
        with open('AdminPass.txt','r') as f:
            AdminPass = f.readline()
        if str(hash(Password)) == AdminPass:
           LoginSuccessful = True
           break
        else:
           LoginAttempt += 1
           if LoginAttempt >= 3:
               msgbox(msg='Access Denied.', title='Employee Tracker', ok_button='OK', image=None, root=None)
               break
           else:
               msgbox(msg='Password Incorrect.', title='Employee Tracker', ok_button='OK', image=None, root=None)
    return LoginSuccessful

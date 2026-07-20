"""
-- The symbol “_():” is used to indicate the function in question
"""

import os                             # My OS is Windows 7, you know :D
import msvcrt
import sys
import subprocess
import random as r
from time import sleep as timeout 

# ==========================================================================
from library import shortcut       # it is very important :D

# Wait....... ( deprecated )

# from library.shortcut import clear_screen as cls          
# from library.shortcut import clstime as clstime    
# from library.shortcut import enter    
# ==========================================================================

from library import AES
from library import JsonEx as jse
from library import file as f
from library import captcha as chkbot
from library import usercontrol as uc

from datetime import datetime as w_timenow  # it is "write time now", you know :v
from getpass import getpass

from tkinter import Tk, filedialog         
root = Tk()
root.withdraw()

from colorama import Fore, Style, init
init(autoreset=True)

BOLD = "\033[1m"
HIJAU = Fore.LIGHTGREEN_EX
MERAH = Fore.LIGHTRED_EX
BIRU = Fore.LIGHTBLUE_EX
BIRU_TUA = Fore.BLUE
KUNING = Fore.LIGHTYELLOW_EX
JINGGA = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.LIGHTMAGENTA_EX
ABU = "\033[90;40m" 
RESET = Style.RESET_ALL

# i not use global, i use dictionary :D

# ``` No 
# username = ""
# password = ""

# ``` Yes
datacache = {
    "username": "",
    "password": ""
}
    
def areyousure(text=""):
    if text:
        huh = input(text)
        if huh == "y":
            return True
        elif huh == "n":
            return False
        else:
            return False  
    else:
        clstime("give your prompt :v")
        return
        
def chkrobot():
    while True:
        choice = r.randint(1, 3)
        
        if choice == 1:
            result = chkbot.ver1()
        elif choice == 2:
            result = chkbot.ver2()
        else:
            result = chkbot.ver3()
    
        if result == "Human":
            print(HIJAU + "Human detected..")          # i have no enemies .....
            timeout(1)
            cls()
            return True # last return : "HUMAN"
        else:                                                                     
            tryagain = input("Try Again?? :D [ y/n ] : ")
            if tryagain == "y": 
                cls()
                continue
            else:
                # I really don't have any enemies.... :) 
                return False # last return : "It's_a_robot,_but_that's_okay" 
            
        # i not hate robot, okey?

# === area registration ======================================================
def reg():
    username = user()
    if not username:
        print(MERAH + "Cancelled..")   # yoo, are you kidding me? :v
        datacache['username'] = ""
        clstime()
        return
    
    datacache['username'] = username
    datacache["password"] = mpass()
    now = w_timenow.now().strftime("%Y-%m-%d %H:%M:%S") # get time, ahh time :v
    
    data_user = {
    "password": datacache["password"],
    "created": now,
    "last_login": now
    }
    
    jse.write(username + ".json", data_user) 
    _respon_infile = infile()
    
    if not _respon_infile:
        f.write("readme.wmes", "WELCOME TO MY PROJECT..")

        result = subprocess.run([
            "7z.exe",
            "a",
            datacache['username'] + ".7z",
            "readme.wmes",
            "-mx=5",
            "-p" + datacache["password"],
            "-y"
        ],    
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
        
        if result.returncode != 0:
            print("Error!!!")
            print(result.stderr)
            clstime("goto main_menu...")
            main_menu()
        else:
            print(HIJAU + "done")
            clstime()
            return
    else:
        print(HIJAU + "done")
        clstime()
        return        

def user():
    print('"C" to "Cancel"')
    _var = input("Username: ")
    if _var in ["c", "C"]:
        return False
    else:
        return _var
              
def mpass():
    while True:
        # make pass
        pw = getpass("Password: ")
        pw_pw = getpass("Confirm password: ")
        
        if pw == pw_pw:
            clstime()
            return pw
        else:
            print("The password doesn't match!, try again...")
            clstime()
        
# area process file =========================================
def infile():
    file_welcome = filedialog.askopenfilename(title="Welcome message...", filetypes=[("Text Only", "*.txt")])
    
    if not file_welcome:
        print(MERAH + "Cancelled...")
        clstime()
        return False # last return = "idk bruh :v"
    
    _get = f.read(file_welcome)
    f.write("readme.wmes", _get)

    result = subprocess.run([
        "7z.exe",
        "a",
        datacache['username'] + ".7z",
        "readme.wmes",
        "-mx=5",
        "-p" + datacache["password"],
        "-y"
    ],    
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
    
    if result.returncode != 0:
        print("Error!!!")
        clstime("goto main_menu...")
        main_menu()
    else:
        print("done!!")
        
# area if password correct :v ====================================  
def ifpasscorrect():
    now = w_timenow.now().strftime("%Y-%m-%d %H:%M:%S") # Hey, look at my twin in line .. :D
    data = jse.read(datacache['username'] + ".json")
    datacache["last_login"] = now

    jse.write(datacache['username'] + ".json", data)
    
    cls()
    result = subprocess.run([
        "7z.exe",
        "x",
        datacache['username'] + ".7z",
        "-p" + datacache["password"],
        "-y"
    ],    
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
    
    if result.returncode != 0:
        reporterr(ifpasscorrect)
        print(result.stderr)
        timeout(1)
        print("goto main_menu...")
        timeout(1)
        cls()
        main_menu()   

    if not (wmes := f.read("readme.wmes")):
        print(MERAH + "Welcome message not found.")
        clstime()
        print("WELCOME TO MY PROJECT..!")
    else:
        print(wmes)
        
    # area information, By the way, enough with the jokes...... just kidding, haha :D
    
    # getinfo, like the "systeminfo" command... right?
    getinfo = jse.read(datacache['username'] + ".json")
    _get_created = getinfo["created"]
    _get_last_login = getinfo["last_login"]
    
    # view this info
    print("\n\n===============================")
    print("INFORMATION!: ")
    print(f"Created : {_get_created}")
    print(f"Last Login : {_get_last_login}\n")
    timeout(1)
    print("END INFORMATION")
    timeout(1)
    print(MERAH + "Login to 3 sec...")
    timeout(3)
    cls()
    userislogin()
    
# area if user change password :v ===============================================
def changepasszip(newpass):
    print(ABU + "change password archive...")

    result = subprocess.run([
        "7z.exe",
        "a",
        datacache['username'] + ".7z",
        "readme.wmes",
        "-mx=5",
        "-p" + newpass,
        "-y"
    ],    
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
    
    if result.returncode != 0:
        print("Error!!!")
        clstime()
        return
    else:
        print(HIJAU + "Done!..")
        clstime()
        return
    
# area if user login , yey ========================================================
def userislogin():
    while True:   
        print("user : " + datacache['username'])
        print(KUNING + '"-h" to help :v')
        enter()
        cmd = input("> ") 
        
        if cmd == "-h":
            print("""\
            Usage: 
            -h                Display this help
            -cp               Change Paasword
            -del              Delete Account
            -my1              Hey look!, want to see my abilities :D?, type \"-my1\" now :D
            -logout           Logout account
            
            Press Enter to continue...
            """)
            input()
            cls()
        elif cmd == "-cp":
            username = datacache["username"]
            password = datacache["password"]
            while True:
                # clpw = Check Last PassWord
                clpw = input("Confirm last password ( Leave blank to cancel. ) : ")
                if clpw == "":
                    print("Cancelled..")
                    clstime()
                    break
                elif cpw == password:
                    print("Correct!")
                    clstime()
                    # npw = New PassWord
                    npw = input("New Password : ")
                    # cnpw = Confirm New PassWord
                    cnpw = input("Confirm Password : ")
                    
                    if npw == cnpw:
                        changepasszip(npw)
                        result = uc.changepassword(username, npw)
                        if result:
                            print(f"{HIJAU}Success to change password!")
                            clstime()
                            break
                        else:
                            print("Error!! :FILENOTFOUND")
                            clstime()
                            break
                    else:
                        print("The password doesn't match!, try again...")
                        clstime()
                        continue        
                else:
                    print("Incorrect password. Try again...")
                    clstime()
                    continue    

        elif cmd == "-del":
            if areyousure("Are you sure you want to delete account? [y/n] : "):
                if areyousure("ARE YOU SURE!! [y/n] : "):
                    if uc.delaccount(datacache['username']):
                        print(KUNING + "Updating data cache..")
                        datacache['username'] = ""
                        datacache['password'] = ""
                        clstime("Plaase wait...")
                        main_menu()
                    else:
                        clstime("Cancelled..")
                        continue  
                else:
                    clstime("Cancelled..")
                    continue   
            else:
                clstime("Cancelled..")
                continue    

        elif cmd == "-my1":
            cls()
            
            
            enter()
            clstime("Tekan Enter untuk kembali ke menu...")
            
        elif cmd == "-logout":
            result = areyousure("Are you sure you want to log out? [y/n] : ")
            if result:
                print(ABU + "Logging out...")
                timeout(2)         
                clstime()
                main_menu()
            else:
                continue
               
def passw(): 

    while True:         
        # input password
        inpass = input("( type \"e\" to Exit ) pass#: ")
        # hmmmmm -_-              
        if inpass == "e":  # so manyyy :v, eh :v
            datacache['username'] = ""
            clstime()
            return

        cfileaccount = f.exist(datacache['username'] + ".json")
        if not cfileaccount:
            print(f"{MERAH}File User : {datacache['username']} not found!, please registry or switch user...")
            clstime()
            return # hahaha, not found :v
        else: 
            # rpass = Read Password
            rpass = jse.read(datacache['username'] + ".json")
            # set username and password :v ======
            # username = rpass["username"] >> im not find username dawg :V
            password = rpass["password"]
            # you remember "_getpass = rpass["password"]" ?, yes me to :v
            
        if inpass == password:
            cls()
            print(HIJAU + "Correct!!")
            datacache["password"] = inpass
            print("check you robot or human?...")
            clstime()
            
            if chkrobot():
                print("ok..")
                clstime()
            else:
                print("you robot?, okey, not problem..")
                clstime()
                
            clstime("Plaase wait!..")
            ifpasscorrect()
        else: 
            cls()
            print("wrong!!, try again")
            clstime()
            continue
            
def main_menu():  # ===================================================== 
    print("Welcome!\n") 
    while True: 
        print('Type "r" to registry\n  and ' + MERAH + '"exit" to exit\n\n"debug" to debug:v')
        login = input("login#: ").lower()
        
        if login == "r":
           cls()
           reg()
        elif login == "exit":
           exit()
        elif login == "debug":
           breakpoint()
        else: 
           datacache['username'] = login
           passw()            

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        exit()
from . import JsonEx as jse
from . import file as f

from colorama import Fore, Style, init
init(autoreset=True)
MERAH = Fore.LIGHTRED_EX

def changepassword(usrname, newpassword):


    data = jse.read(usrname + ".json")
    data["password"] = newpassword

    try:
        jse.write(username + ".json", data)
        return True  # last return : "OK"
    except FileNotFoundError:
        return False # last return : "FILENOTFOUND!"
        
def delaccount(username):
    confirmation = input(f'Type name account "{username}" to delete... : ')
    if confirmation == username:
        print(MERAH + "Deleting account...")
        f.remove(username + ".json")
        f.remove(username + ".7z")
        return True
    else:
        return False
#
# SHORTCUT BABEH!!!!!!!!!!
#
#
# =======================================================
from time import sleep as timeout 
import os
from colorama import Fore, Style, init

init(autoreset=True)
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def clstime(text=""):
    if text:
        print(text)

    timeout(1)
    cls()
    
def enter():
    print("\n")    

def reporterr(text=""):
    if text:
        print(f"{red}Error!!! in function {yellow}_(): {Style.RESET_ALL}{text}")
    
    clstime()
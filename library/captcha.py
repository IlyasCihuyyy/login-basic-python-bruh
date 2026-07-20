import random as r
from time import sleep as t
from colorama import Fore, Style, init

BIRU = Fore.LIGHTBLUE_EX
HIJAU = Fore.LIGHTGREEN_EX
MERAH = Fore.LIGHTRED_EX

def ver1():
    num = 1
    
    while True:
        a = r.randint(1, 20)
        b = r.randint(1, 20)
    
        print(f"{HIJAU}Human Verification")
        print(f"{MERAH}------------------")
        print("\n")

        print(f"{a} + {b} = ?\n")
    
        try:
            jawab = int(input("> "))
    
            if jawab == a + b:
                return "Human"
            else:
                if num <= 2:
                    num = num + 1
                    print("Wrong!, try again")
                    t(0.5)
                else:
                    return "Robot"
        except ValueError:
            print("Why is it empty?")
            t(1)
            
    
def ver2():
    num = 1
    
    while True:
        captcha = [
            "hututu46",
            "karapu84",
            "qetequ86",
            "nubeja38",
            "tuqeye88",
            "pamuru73",
            "rawena37",
            "yefuru87",
            "pupeme67"
        ]
        
        human_verification = r.choice(captcha)
        
        print(f"{HIJAU}Human Verification")
        print(f"{MERAH}------------------")
        print("\n")
    
        
        print("Type this:")
        print(f"[  {human_verification}  ]\r")
        
        user = input("> ")
        
        if user == human_verification:
            return "Human"
        else:
            if num <= 2:
                num = num + 1
                print("Wrong!, try again")
                t(0.5)
            else:
                return "Robot"
            
def ver3():
    print(f"{HIJAU}Human Verification")
    print(f"{MERAH}------------------")
    print("\n")
    
    print("type enter to next...")
    input()
    return "Human"
    
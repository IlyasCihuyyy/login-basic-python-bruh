import subprocess
from . import file as f

def adduser(username, password):
    if f.exist("readme.wmes"):
        subprocess.run([
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
    else:
        
    
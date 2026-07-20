import os
import shutil

def read(name_file): # def baca(name_file):
    with open(name_file, "r") as f:
        return f.read()
        
def write(name_file, content): # def tulis(name_file, content):
    with open(name_file, "w") as f:
        f.write(content)
        
def add(name_file, content):
    with open(name_file, "a") as f:
        f.write(content)
        
def remove(name_file):
    os.remove(name_file)
    
def copy(sumber, tujuan):
    shutil.copy(sumber, tujuan)
    
def move(sumber, tujuan):
    shutil.move(sumber, tujuan)

def rename(lama, baru):
    os.rename(lama, baru)
    
def exist(name_file):
    return os.path.exists(name_file)

def seesize(name_file):
    return os.path.getsize(name_file)
    
def create(name_file):
    open(name_file, "w").close()
    
def createfolder(folder):
    os.makedirs(folder, exist_ok=True)

def daftar(folder="."):
    return os.listdir(folder)
    
def writeline(name_file):
    with open(name_file, "r") as f:
        return f.readlines()
        
def linecount(name_file):
    with open(name_file, "r") as f:
        return len(f.readlines())
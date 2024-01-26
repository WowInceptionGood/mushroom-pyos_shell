import os
import shutil
import sys

working_directory = ""
try:
    with open("mushroom_dir.conf", 'r') as f:
        working_directory = f.read()
except IOError:
    pass

if (working_directory != ""):
    pass
elif (working_directory == "" or working_directory == " "):
    pass


def cf():
    global working_directory
    fp = working_directory + "/" + input("Path: ")
    with open(fp, 'w') as f:
        f.write("")

def vf():
    global working_directory
    fp = working_directory + "/" + input("Path: ")
    file = open(fp, mode='r', encoding='utf-8')
    print(file.read())

def wf():
    global working_directory
    fp = working_directory + "/" + input("Path: ")
    data = input("Data: ")
    with open(fp, 'w') as f:
        f.write(data)

def loadmod():
    global working_directory
    modpath = input("Please, enter mod path: ")
    with open(modpath) as f2:
        exec(f2.read())

def mkdir():
    global working_directory
    path = working_directory + "/" + input("Path: ")
    if not os.path.exists(path):
        os.mkdir(path)

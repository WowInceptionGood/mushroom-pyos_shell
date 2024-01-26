import os
import shutil
import sys
import mushroomlib

working_directory = ""
try:
    with open("mushroom_dir.conf", 'r') as f:
        working_directory = f.read()
except IOError:
    pass

if (working_directory != ""):
    pass

elif (working_directory == "" or working_directory == " "):
    working_directory = ""

def ls():
    global working_directory
    listdir = os.listdir(working_directory)
    for i in listdir:
        print(i)

def cd():
    global working_directory
    pathdir = input("Path: ")
    fullpath = working_directory + "/" + pathdir
    isdir = os.path.isdir(fullpath)
    if (isdir == True):
        working_directory = fullpath
    else:
        print("Directory not found.")

def cddotdot():
    global working_directory
    working_directory = os.path.abspath(os.path.join(working_directory, os.pardir))

def pwd():
    global working_directory
    print(working_directory)

commands = {
"ls":ls,
"cd":cd,
"cd ..":cddotdot,
"pwd":pwd,
}

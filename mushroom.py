import os
import shutil
import sys
import mushroomlib

working_directory = os.getcwd()

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
        try:
            with open("mushroom_dir.conf", 'w') as f:
                f.write(working_directory)
        except IOError:
            pass
    else:
        print("Directory not found.")

def cddotdot():
    global working_directory
    working_directory = os.path.abspath(os.path.join(working_directory, os.pardir))
    try:
        with open("mushroom_dir.conf", 'w') as f:
            f.write(working_directory)
    except IOError:
        pass

def pwd():
    global working_directory
    print(working_directory)

commands = {
"ls":ls,
"cd":cd,
"cd ..":cddotdot,
"pwd":pwd,
"m":mushroomlib.loadmod,
"loadmod":mushroomlib.loadmod,
}

def console():
    global working_directory
    while True:
        command = input("Mushroom: ")
        if command in commands:
            commands[command]()
        else:
            print("Command not found. Type 'help' for a list of commands.")

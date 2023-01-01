#!/usr/bin/env python3
import os
import shutil
from PIL import Image

def conversion(full_path,ext):

    for filename in os.listdir(full_path):
        f = os.path.join(full_path, filename)
        if os.path.isfile(f):
            try:
                im = Image.open(f).convert('RGB')
                im.save(f + ext)
            except OSError:
                print("cannot convert", f)

def resizing(full_path):
    for filename in os.listdir(full_path):
        f = os.path.join(full_path,filename)
        if os.path.isfile(f) and f.endswith('.jpeg'):
            try:
                im = Image.open(f)
                im.resize((128,128)).save(f)
            except OSError:
                print("cannot resize", f)

def rotation(full_path):
    files = list()
    for filename in os.listdir(full_path):
        f = os.path.join(full_path,filename)
        if os.path.isfile(f) and f.endswith('.jpeg'):
            files.append(f) 
            #this is not necessary. Did it for debugging. 

    ###### Creation of the destination dir. 
    new_dir = "new_dir"
    path = os.path.join(".",new_dir)
    os.mkdir(path) 
    destination = "/home/herrboh/1.CurrentStudies/3.Programs/Python/GooglePy/6course/1week/qwiklab/new_dir/"
    ######

    for i in files:
        path_name, file_name = os.path.split(i)
        #separating the file name from the full path
        try:
           im = Image.open(i)
           im.rotate(-90).save(i)
        except OSError:
            print("cannot rotate", i)

        shutil.move(i, destination + file_name)
        #if I dont move it to a different directory
        #there are going to be inconsistencies in the rotation
        #because of the for loop. 
        # I do not yet understand why. 
        # It works, but I need to further study this. 

def main():
    ext = ".jpeg"
    directory = "/home/herrboh/1.CurrentStudies/3.Programs/"+\
            "Python/GooglePy/6course/1week/qwiklab/images"

    conversion(directory,ext)
    resizing(directory) 
    rotation(directory)

main()

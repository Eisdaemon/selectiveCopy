#! python3
# selectiveCopy.py - makes copies of specific fileytypes

import os, shutil, pyinputplus
from pathlib import Path

def selectiveCopier(filepath, fileType):
    p = Path(filepath)
    c = Path(p / 'Copy')
    #Create a new Dictonary
    while True:
        try:
            #If succesfull create one and break the Loop
            os.makedirs(c)
            break
        #Folder exists alredy
        except:
            #Should be a new one created?
            prompt = 'Copy Folder exists already\nShould a new Copy be created (yes/no)\n'
            response = pyinputplus.inputYesNo(prompt)
            response = response.lower()
            #Create a new folder Path with New name, os.makedits above creates new one or another erros leads back here
            if response == 'yes':
                prompt2 = 'Name?\n'
                newName = str(pyinputplus.inputStr(prompt2))
                c = Path(p / newName)
            #Close Program
            else:
                os._exit(1)
    #Walks through entire Path
    for filename in p.rglob('*.jpg'):
        try:
            #Copies of possible
            shutil.copy(filename,c)
        except:
            #Files can't exist twice
            print(f'"{filename}" is already Backed up')
selectiveCopier('E:/Private Cloud', '*.jpg')

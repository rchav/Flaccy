# Let's get Flaccy

import shutil
import os

src = "/Projects/InPho/"
dest = "/Projects/InPho/Rikers Calls Dev/"

DANYsrc = '\\DANY.NYCNET\DANYXDrive\Rikers Calls\\'
DANYdest = '\\DANY.NYCNET\DANYXDrive\Rikers Calls\Rikers Calls Dev\\'

def GetFlaccy(mySrc, myDest):

    # create some lists of flac files and their paths
    fullPaths = []
    justFileNames = []

    # what type of file are you looking for?
    fileType = '.flac'

    # loop time
    for root, dirs, files in os.walk(mySrc, topdown=False):
        for name in files:

            # create a list of the full paths
            fullFilePath = os.path.join(root, name)
            if fullFilePath.endswith(fileType):
                fullPaths.append(fullFilePath)

            # create a list of the flac file names
            justFlacFileName = os.path.join(name)
            if justFlacFileName.endswith(fileType):
                justFileNames.append(justFlacFileName)


    # create a set of unique BACs
    BACs = set()
    for fileName in justFileNames:
        BACs.add(fileName[:10])

    # turn the set into a list
    BACs = list(BACs)


    # create the BAC folders
    for BAC in BACs: 
        folder = myDest + BAC + '/'
        if not os.path.exists(folder):
            os.makedirs(folder)
        

    # copy files to their places
    for file in fullPaths:
        lastSlash = file.rfind('/') + 1
        tempDest = file[lastSlash:]
        tempList = tempDest.split('_')
        subDest = tempList[0]
        finalDest = myDest + subDest
        shutil.copy(file, finalDest)

lets = GetFlaccy(src, dest)

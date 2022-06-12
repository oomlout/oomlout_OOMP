import oomBase as ob
import os

def harvestFootprintImages():
    footprints = getFootprintNames()
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")

    
def harvest(name):
    c=0


def getFootprintNames():
    directory = "C:/Program Files/KiCad/6.0/share/kicad/footprints/"
    footprints = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if("kicad_mod" in file):
                #print(file)
                fileName = file.split(".")
                footprints.append(fileName[0])
    return footprints
    

import OOMP
import OOMPtags #### hex for footprint
import OOMP_footprints_BASE
from oomBase import *

import os

from kiutils.footprint import Footprint

def createFootprints():
    owners = ["kicad-footprints"]
    for owner in owners:
        footprints = getKicadFootprintNames(owner)        
        for footprint in footprints: 
            d = {}
            d["oompType"] =  "FOOTPRINT"
            d["oompSize"] =  "kicad"
            d["oompColor"] =  owner
            d["oompDesc"] =  footprint[0]
            d["FOOTPRINT"] = footprint[1]
            loadFootprintDict(d)
            makeFootprint(d)


def makeFootprint(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]   
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    print("Making Footprint: " + oompID)

    oompSlashes = type + "/" + size + "/" + color + "/" + desc + "/" + index + "/"

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_eda/" + oompSlashes
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    repoName = ""

    skipTags = ["oompType","oompSize","oompColor","oompDesc","oompIndex","FOOTPRINT","hexID"]

    extraTags = []
    for tag in d:
        if tag not in skipTags:
            extraTags.append(OOMP.oompTag(tag,d[tag]))        
    tagString = ""
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)
    pass

def loadFootprintDict(d):
    footprint = d["FOOTPRINT"]
    #print(symbol)
    """
Property(key='Reference', value='U', id=0, position=Position(X=-7.62, Y=19.05, angle=0, unlocked=False), effects=Effects(font=Font(face=None, height=1.27, width=1.27, thickness=None, bold=False, italic=False, lineSpacing=None), justify=Justify(horizontally=None, vertically=None, mirror=False), hide=False))
1:
Property(key='Value', value='14529', id=1, position=Position(X=-7.62, Y=-21.59, angle=0, unlocked=False), effects=Effects(font=Font(face=None, height=1.27, width=1.27, thickness=None, bold=False, italic=False, lineSpacing=None), justify=Justify(horizontally=None, vertically=None, mirror=False), hide=False))
    """

    d["name"] = footprint.libraryLink.replace("'","")
    try:
        d["description"] = footprint.description.replace("'","")
    except:
        pass
    d["tags"] = footprint.tags



    attributes = footprint.attributes
    d["kicadFootprintAtribute" + "Type"] = attributes.type
    
    for model in footprint.models:
        d["kicadFootprint3DModel"] = model.path

    try:
        for pad in footprint.pads:
            num = pad.number
            d["kicadFootprintPad" + num + "Type"] = pad.type
            d["kicadFootprintPad" + num + "Shape"] = pad.shape
            d["kicadFootprintPad" + num + "Position"] = pad.position
            d["kicadFootprintPad" + num + "Size"] = pad.size
    except:
        print("        Unable to capture pads")
    


    d["oompIndex"] = d["name"]

    oompID = d["oompType"] + "-" + d["oompSize"] + "-" + d["oompColor"] + "-" + d["oompDesc"] + "-" + d["oompIndex"]
    d["hexID"] = OOMPtags.getFootprintHex(oompID)

    return d

def getKicadFootprintNames(owner):
    directory = "oomlout_OOMP_eda/sourceFiles/" + owner + "/"    
    footprints = []
    count = 0
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filename = subdir + "/" + file
            if("kicad_mod" in file and "Obsolete" not in filename):                                
                print("Working on File: "  + filename)
                try:
                    foot = Footprint().from_file(filename)
                    footprints.append([subdir.replace(".pretty","").replace("oomlout_OOMP_eda/sourceFiles/kicad-footprints/",""),foot])
                except:
                    print("    ERROR Unable to parse file into kiutils")
                    
                count = count + 1
                if count > 1:
                    pass
                    #break  ## For only one file
        if count > 1:
            pass
            #break  ## For only one file
    return footprints    
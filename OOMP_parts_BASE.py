import OOMP
from oomBase import *

import OOMP_parts_OOML
import OOMP_parts_JLCC

def createAllParts():
    OOMP_parts_OOML.createParts()
    OOMP_parts_JLCC.createParts()

def makePart(type="",size="",color="",desc="",index="",hexID="",extraTags=[],dict=""):
    if dict != "":
        type = dict["type"]
        size = dict["size"]
        color = dict["color"]
        desc = dict["desc"]
        index = dict["index"]
        hexID = dict["hexID"]
        try:
            extraTags = dict["extraTags"]
        except:
            pass


    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index
    print("Making part: " + oompID)



    inputFile = "templates/partsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/" + oompID + "/"
    outputFile = outputDir + "details.py"

    datasheet = ""
    if dict != "":
        try:
            datasheet = dict["datasheet"]
        except:
            pass
    if datasheet != "":
        oomCopyFile(datasheet,outputDir + "datasheet.pdf" )


    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)
    
    
    
    tagString = ""
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)


    oomWriteToFile(outputFile,contents)


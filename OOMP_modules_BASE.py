import OOMP
import OOMPproject
import OOMPprojectParts
from oomBase import *

######  Company Files
import OOMP_projects_ADAF
import OOMP_projects_ELLA
import OOMP_projects_IBBC
import OOMP_projects_SEED
import OOMP_projects_SOPA

def createAllModules():
    d = {}
    d["oompType"] = "BLOCK"
    d["oompSize"] = "POWE"
    d["oompColor"] = "V12R"
    d["oompDesc"] = "V33D"
    d["oompIndex"] = "01"
    d["hexID"] = "BP123"
    d["name"] = "Power Block About 12 v In, 3.3 v Out"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    makeModule(d)
    d = {}
    d["oompType"] = "BLOCK"
    d["oompSize"] = "SENS"
    d["oompColor"] = "ACCEL"
    d["oompDesc"] = "I2C"
    d["oompIndex"] = "01"
    d["hexID"] = "BSAI"
    d["name"] = "Sensor Block (Accelerometer) I2C"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    makeModule(d)    
    d = {}
    d["oompType"] = "BLOCK"
    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    d["hexID"] = "BCI"
    d["name"] = "Connector Block (I2C)"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    makeModule(d)
    d = {}
    d["oompType"] = "BLOCK"
    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C"
    d["oompDesc"] = "EXTRA"
    d["oompIndex"] = "01"
    d["hexID"] = "BCIE"
    d["name"] = "Connector Block (I2C) Plus Extra Pins"    
    d["extraTags"] = []
    #d["extraTags"].append([])
    makeModule(d)
    
    d = {}
    d["oompType"] = "MODULE"
    d["oompSize"] = "SENS"
    d["oompColor"] = "K345"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    d["hexID"] = "MS345"
    d["name"] = "Sensor Module ADXL345"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-SENS-ACCEL-I2C-01"])
    d["extraTags"].append(["oompParts","U1,SENS-LG14-X-K345-01"])    
    makeModule(d)
    
    d = {}
    d["oompType"] = "MODULE"
    d["oompSize"] = "CONN"
    d["oompColor"] = "BRBO"
    d["oompDesc"] = "IBBC"
    d["oompIndex"] = "SZ01"
    d["hexID"] = "MCBI1"
    d["name"] = "Connector Module Breakout Board IBBZ Size 01"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-EXTRA-01"])
    d["extraTags"].append(["oompParts","J1,HEAD-I01-X-PI06-01"])    
    d["extraTags"].append(["oompParts","J2,HEAD-I01-X-PI06-01"])    
    makeModule(d)
    
    d = {}
    d["oompType"] = "MODULE"
    d["oompSize"] = "CONN"
    d["oompColor"] = "I2C"
    d["oompDesc"] = "QWIIC"
    d["oompIndex"] = "01"
    d["hexID"] = "MCQ"
    d["name"] = "Connector Module I2C QWIIC"    
    d["extraTags"] = []
    d["extraTags"].append(["matchingBlock","BLOCK-CONN-I2C-STAN-01"])
    d["extraTags"].append(["oompParts","J1,HEAD-JSTSH-X-PI04-RS"])    
    makeModule(d)

def makeModule(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_modules/" + oompID + "/"
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    extraTags = []
    try:
        for tag in d["extraTags"]:
            extraTags.append(OOMP.oompTag(tag[0],tag[1]))        
    except:
        print("no extra tags")

    tagString = ""
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    



    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)


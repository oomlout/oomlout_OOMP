import OOMP
from oomBase import *

def makePart(type,size,color,desc,index,hexID):
    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/AAAA-AAA-A-AAAA-AA/XXXdetailsXXX.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/" + oompID + "/"
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)

    oomWriteToFile(outputFile,contents)




def makeOne():
    type = "TERS"
    size = "35D"
    color = "L"
    desc = "PI01"
    index = "01"
    hexID = "T35L1"

    #makePart(type,size,color,desc,index,hexID)

    for x in range(2,10):
        desc = "PI2X" + str(x).zfill(2)
        makePart(type,size,color,desc,index,hexID)



def makeAll():


    ##############################
    ######  HEAD
    type = "HEAD";size = "I01";color = "X";desc = "PI2X10";index = "SHRO";hexID = "H2X10SH"

    for x in range(2,10+1):
        desc = "PI2X" + str(x).zfill(2)
        hexID = "H2X" + str(x) + "SH"
        makePart(type,size,color,desc,index, hexID)

    type = "HEAD";size = "JSTXH";color = "X";desc = "PI01";index = "01";hexID = "JX"

    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HXH" + str(x)
        makePart(type,size,color,desc,index,hexID)

    type = "HEAD";size = "JSTSH";color = "X";desc = "PI01";index = "SM";hexID = "T35L1"

    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HSH" + str(x)
        makePart(type,size,color,desc,index,hexID)

    type = "HEAD";size = "JSTSH";color = "X";desc = "PI01";index = "RS";hexID = "T35L1"
    for x in range(1,20+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "HSHR" + str(x)    
        makePart(type,size,color,desc,index,hexID)

    ##############################
    ######  RESA
    resistorSmall = ["O102","O103","O220","O222","O472"]

    resaPackages = ["06038","12068"]

    type = "RESA";size = "";color = "X";desc = "";index = "01";hexID = ""
    for size in resaPackages:
        for desc in resistorSmall:
            hexID = "RA" + size.replace("06038","6").replace("12068","12") + desc.replace("O","")
            desc = desc + "X4"            
            makePart(type,size,color,desc,index,hexID)
    

    ##############################
    ######  SENS
    ###### ADXL345
    type = "SENS";size = "LG14";color = "X";desc = "K345";index = "01";hexID = "SEN345"
    makePart(type,size,color,desc,index,hexID)

    ##############################
    ######  TERS
    type = "TERS";size = "35D";color = "L";desc = "PI01";index = "01";hexID = "T35L1"

    for x in range(1,15+1):
        desc = "PI" + str(x).zfill(2)
        hexID = "T35L" + str(x)
        makePart(type,size,color,desc,index,hexID)



makeAll()
#makeOne()
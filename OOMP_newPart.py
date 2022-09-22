import OOMP
from oomBase import *



type = "VREG"
size = "SO235"
color = "X"
desc = "KMIC5205"
index = "V5"
hexID = "V235MIC52055"

oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

inputFile = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/AAAA-AAA-A-AAAA-AA/XXXdetailsXXX.py"
outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_parts/" + oompID + "/"
outputFile = outputDir + "details.py"

contents = oomReadFileToString(inputFile)
contents = contents.replace("TYPEZZ",type)
contents = contents.replace("SIZEZZ",size)
contents = contents.replace("COLORZZ",color)
contents = contents.replace("DESCZZ",desc)
contents = contents.replace("INDEXZZ",index)
contents = contents.replace("HEXZZ",hexID)

oomWriteToFile(outputFile,contents)



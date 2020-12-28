#### oomp migrate
import OOMP
import os
import time
from shutil import copyfile

baseDir = "C:\\GH\\OLD01-oomlout-OOMP\\parts\\"
dirList = os.listdir(baseDir)
        
def addPartFromDir(string):
    oldOompDir = "C:\\GH\\OLD01-oomlout-OOMP\\parts\\"
    oompBase = "C:\\GH\\oomlout-OOMP\\"
    
    fileName = "OOMPpart_" + string.replace("-","_")
    parts = string.split("-")
    if len(parts) == 5:
        oompType = parts[0]
        oompSize = parts[1]
        oompColor = parts[2]
        oompDesc = parts[3]
        oompIndex = parts[4]
        print("Adding: " + string)
        #create file
        f = open(oompBase + fileName + ".py","w+")
        f.write("import OOMP\n")
        f.write("\n")
        global index
        f.write("newPart = OOMP.oompItem(" + str(index) + ")\n")
        index = index + 1
        f.write("newPart.addTag(\"oompType\", \"" + oompType + "\")\n")
        f.write("newPart.addTag(\"oompSize\", \""   + oompSize + "\")\n")
        f.write("newPart.addTag(\"oompColor\", \"" + oompColor + "\")\n")           
        f.write("newPart.addTag(\"oompDesc\", \"" + oompDesc + "\")\n")
        f.write("newPart.addTag(\"oompIndex\", \"" + oompIndex + "\")\n") 
        f.write("\n")
        f.write("OOMP.parts.append(newPart)\n")
        f.close()            
        #copy files
        migrateFiles(string)
        #add to parts load
        addToPartsLoadFile(string)

def addToPartsLoadFile(string):
    oompBase = "C:\\GH\\oomlout-OOMP\\"
    partsLoadFile = oompBase + "OOMPparts.py"
    f = open(partsLoadFile,"a")
    f.write("import OOMPpart_" + string.replace("-","_") + "\n")
    f.close()

def migrateFiles(string):
    oompBase = "C:\\GH\\oomlout-OOMP\\"
    newDirectory = oompBase + "parts\\" + string + "\\"
    oldOOMPDir = "C:\\GH\\OLD01-oomlout-OOMP\\parts\\"
    oldDirectory = oldOOMPDir + string + "\\"
    oldBase = oldOOMPDir + string + "\\" + string
    
    if not os.path.isdir(newDirectory):
        os.mkdir(newDirectory)
    
    #image file
    src = oldBase + ".jpg"
    dest = newDirectory + "image.jpg"
    if os.path.isfile(src):
        print("        Copying Image File")
        copyfile(src,dest)
    #bottom file
    src = oldBase + "_BOTTOM.jpg"
    dest = newDirectory + "image_BOTTOM.jpg"
    if os.path.isfile(src):
        print("        Copying Image File")
        copyfile(src,dest)    
    #re file
    src = oldBase + "_RE.jpg"
    dest = newDirectory + "image_RE.jpg"
    if os.path.isfile(src):
        print("        Copying Image File")
        copyfile(src,dest)        
    #re file
    src = oldBase + "-datasheet.pdf"
    dest = newDirectory + "datasheet.pdf"
    if os.path.isfile(src):
        print("        Copying Image File")
        copyfile(src,dest)        

    

index = 8762

for x in dirList:
    if os.path.isdir(baseDir + x):
        print(x)
        addPartFromDir(str(x))

##addPartFromDir("HEAD-I01-X-PI03-01")

#### oomp add

#### oomp migrate
#import OOMP
import os
import time
from shutil import copyfile
import re






def translateDiag(inFile, outFile, part):
    inf = open(inFile, "r")
    outf = open(outFile, "w")

    input = inf.read()

    lines = input.split("\n")


    newLine = "######  OOMP Template File"
    outf.write(newLine+"\n")
    newLine = "import OOMP"
    outf.write(newLine+"\n")    
    newLine = ""
    outf.write(newLine+"\n")


    newLine = 'indexA = len(OOMP.parts) + 1'
    outf.write(newLine+"\n")
    newLine = 'newPart = OOMP.oompItem(indexA)'
    outf.write(newLine+"\n")
    newLine = 'newPart.addTag("hexID", "' + part + '")'
    outf.write(newLine+"\n")
    


    newLine = 'newPart.addTag("oompType", "TEMPLATE")'
    outf.write(newLine+"\n")
    newLine = 'newPart.addTag("oompSize", "A")'
    outf.write(newLine+"\n")
    newLine = 'newPart.addTag("oompColor", "A")'
    outf.write(newLine+"\n")
    newLine = 'newPart.addTag("oompDesc", "A")'
    outf.write(newLine+"\n")
    newLine = 'newPart.addTag("oompIndex", str(indexA))'
    outf.write(newLine+"\n")
    newLine = ''
    outf.write(newLine+"\n")
 
    for line in lines:
        
        attribute = stringBetween("</",">",line)
        element = stringBetween(">","</",line)
        newLine = ""

        if element != None:
            newLine = 'newPart.addTag("drawItem","' + element.group(1) + '")'

               

        outf.write(newLine+"\n")
    
    newLine = 'OOMP.parts.append(newPart)'
    outf.write(newLine+"\n")
    

    inf.close()
    outf.close()

def stringBetween(start,end,str):
    print(str)
    return re.search(start + "(.*)" + end, str)

def translateDiags(inFolder):
    
    for subdir, dirs, files in os.walk(inFolder):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + file

            if filepath.endswith(".oomp"):
                inFile = filepath
                part = file.replace(".oomp","")                
                outFile = "C:/GH/oomlout-OOMP/templates/diag/" + part + ".py"
                print (filepath + "   " + part + "   " + outFile)
                translateDiag(inFile, outFile, part)

part = "BUTA-06-X-STAN-01"
inFile = "C:/GH/oomlout-OOMP/templates/diag/old/" + part + ".oomp"
outFile = "C:/GH/oomlout-OOMP/templates/diag/" + part + ".py"
#translateDiag(inFile, outFile, part)



inFolder = "C:/GH/oomlout-OOMP/templates/diag/old/"
translateDiags(inFolder)




##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
######  OLD

"""


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

def addPartFromXML(string):
    print("Adding part from xml")
    oldOompDir = "C:\\GH\\OLD01-oomlout-OOMP\\parts\\"
    oompBase = "C:\\GH\\oomlout-OOMP\\"

    xmlFile=oldOompDir + string + "\\" + string + ".oomp"
    newFile = "C:\\GH\\oomlout-OOMP\\" + "test\\" + string +".py"

    print("    XML file: " + xmlFile)
    
    fileName = "OOMPpart_" + string.replace("-","_")
    parts = string.split("-")

    f = open(xmlFile)
    contents = f.read()
    f.close()


    outputContents = "import OOMP\n\nnewPart = OOMP.oompItem(" + str(index) + ")\n\n"

    contents = contents.replace("<xml>","")
    contents = contents.replace("</xml>","")
    contents = contents.replace("<oompPart>","")
    contents = contents.replace("</oompPart>","")

    lines = contents.split("\n")

    global x
    x = 0
    while x < len(lines):
        print("Running line # " + str(x))
        line = lines[x]
##        print("    " + str(line))
        tagName = getXMLTagName(line)
        newLine = ""
        if tagName != "":
            if not omitTag(tagName):
                if singleProcessing(tagName):
                    print("#SINGLE PROCESSING: " + tagName)
                    testLine = ""
                    if "oompBbls" == tagName:
                        testLine = "/oompBbls"
                        newLine = handleSimpleList(x,lines,"oompBbls")
                    if "oompDiag" == tagName:
                        testLine = "/oompDiag"
                        newLine = handleSimpleList(x,lines,"oompDiag")
                    if "oompIden" == tagName:
                        testLine = "/oompIden"
                        newLine = handleSimpleList(x,lines,"oompIden")
                    if "oompSchem" == tagName:
                        testLine = "/oompSchem"
                        newLine = handleSimpleList(x,lines,"oompSchem")
                    if "oompSimp" == tagName:
                        testLine = "/oompSimp"
                        newLine = handleSimpleList(x,lines,"oompSimp")
                    runThrough = True
                    while runThrough:
                        line = lines[x]
                        print("     line   " + line)
                        if testLine in line:
                            runThrough = False
                        else:
                            print(" x inside: " + str(x))
                            x=x+1
                    
                elif extraProcessing(tagName):
                    print("#EXTRA PROCESSING: " + tagName)
                    testLine = ""
                    if "sourceList" == tagName:
                        testLine = "/sourceList"
                        newLine = handleList(x,lines,"sourceList","manufacturer")
                    elif "oplList" == tagName:
                        testLine = "/oplList"
                        newLine = handleList(x,lines,"oplList","oplSystem")



                    runThrough = True
                    while runThrough:
                        line = lines[x]
                        if testLine in line:
                            runThrough = False
                        else:
                            x=x+1
                else:
                    print("        not ex" + str(line))
                    newLine = getPythonStringFromXML(tagName, line)
                        
            else:
                newLine = ""

        outputContents = outputContents + str(newLine) + "\n"
        x=x+1
            
                
        
    outputContents = outputContents  + ("OOMP.parts.append(newPart)\n")
    f = open(newFile, "w+")
    f.write(outputContents)
    f.close()


def handleList(x,lines,listName,typeName):    
    rv = "\n" + listName + " = []\n"
    #will be a manufacturer tag
    line = lines[x+1]
    #start filling first manufacurer
    rv = rv + typeName + "Details = []\n"
    y = x + 2
    while y < 20000:
        line = lines[y]
        tagName = getXMLTagName(line)
        print("       tag name  " + str(tagName) + "     typeName " + typeName)
        if typeName in tagName :
            y = 30000
        else:
            rv  = rv + getPythonStringFromXMLList(typeName +"Details", tagName, line) + "\n"
            y += 1


    rv = rv + "sourceList.append(OOMP.oompTag(\"" + typeName + "\"," + typeName + "Details))\n"
    rv = rv + "newPart.addTag(\"" + listName + "\", " + listName + ")\n"
    return rv                                                

def handleSimpleList(x,lines,listName):    
    rv = "\n" + listName + " = []\n"
    #will be a manufacturer tag
    line = lines[x+1]
    #start filling first manufacurer
    y = x + 1
    while y < 20000:
        line = lines[y]
        tagName = getXMLTagName(line)
        print(listName + "   " + tagName)
        if listName in tagName :
            y = 30000
        else:
            rv  = rv + getPythonStringFromXMLList(listName, tagName, line) + "\n"
            y += 1

    rv = rv + "newPart.addTag(\"" + listName + "\", " + listName + ")\n"
    print(rv)

    return rv                                                


##    sourceListTag = 
    rv = "newPart.addTag(\"sourceList\", sourceListTag)\n"
    return rv

def omitTag(tagName):
    rv = False
    if "oompStatCount" in tagName:
        rv = True
    elif "oompStatPercent" in tagName:
        rv = True
    elif "oompID" in tagName:
        rv = True
    elif "name" in tagName:
        rv = True
    elif "oompStatCount" in tagName:
        rv = True
    return rv

def extraProcessing(tagName):
    rv = False
    if "sourceList" in tagName:
        rv = True
    elif "oplList" in tagName:
        rv = True
    return rv        

def singleProcessing(tagName):
    rv = False
    if "oompBbls" in tagName:
        rv = True
    elif "oompDiag" in tagName:
        rv = True
    elif "oompIden" in tagName:
        rv = True
    elif "oompSchem" in tagName:
        rv = True
    elif "oompSimp" in tagName:
        rv = True
    return rv
        
        
    



    

def getPythonStringFromXML(name, xml):
    return getPythonStringFromXMLCustom("newPart", name, xml)
        
def getPythonStringFromXMLCustom(typ, name, xml):
    tagName = getXMLTagName(xml)
    if tagName != "":
        tagValue = getXMLValue(xml)
        pythonString = typ + ".addTag(\"" + name + "\", \"" + tagValue + "\")"
        return pythonString
    else:
        return ""

def getPythonStringFromXMLList(typ, name, xml):
    tagName = getXMLTagName(xml)
    if tagName != "":
        tagValue = getXMLValue(xml)
        pythonString = typ + ".append(OOMP.oompTag(\"" + name + "\", \"" + tagValue + "\"))"
        return pythonString
    else:
        return ""

def getXMLValue(xml):
    if "<" in xml:
        start=">"
        end="<"
        result = re.search(start + "(.*?)" + end, xml)
        if result is not None:
##            print("Tag name: " + str(result.group(1)))
            return str(result.group(1))
        else:
            return ""
    else:
        return ""
        

def getXMLTagName(xml):
    if "<" in xml:
        start="<"
        end=">"
        result = re.search(start + "(.*?)" + end, xml)
##        print("Tag name: " + str(result.group(1)))
        return str(result.group(1))
    else:
        return ""
    
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
##        addPartFromDir(str(x))
        addPartFromXML(str(x))

##addPartFromDir("HEAD-I01-X-PI03-01")
##addPartFromXML("HEAD-I01-X-PI03-01")

"""
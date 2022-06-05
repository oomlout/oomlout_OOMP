import OOMP
import os
import subprocess
import re
import time


def generateAll():
    for x in OOMP.parts:
        generateAllItem(x)

def generateAllItem(item):
    generateLabel(item)

def generateLabels():
    for x in OOMP.parts:
        generateLabel(x)

def generateLabel(item):
    print("    Generating Labels for " + str(item))
    if "TEMPLATE" not in item.getTag("oompType").value:
        oompID = item.getTag("oompID")
        #inventory label
        template = "templates\\label\\OOMP-label-inventory.tmpl.svg"
        outputDirectory = "parts\\" + oompID.value
        output = outputDirectory + "\\label-inventory.svg" 
        outputPDF = outputDirectory + "\\label-inventory.pdf" 
        if not os.path.isdir(outputDirectory):
            os.makedirs(outputDirectory)
        oompSearchAndReplace(template, output, item)
        oompMakePDF(output,outputPDF)
        #front label
        template = "templates\\label\\OOMP-label-front.tmpl.svg"
        outputDirectory = "parts\\" + oompID.value
        output = outputDirectory + "\\label-front.svg" 
        outputPDF = outputDirectory + "\\label-front.pdf" 
        if not os.path.isdir(outputDirectory):
            os.makedirs(outputDirectory)
        oompSearchAndReplace(template, output, item)
        oompMakePDF(output,outputPDF)
        #spec label
        template = "templates\\label\\OOMP-label-spec.tmpl.svg"
        outputDirectory = "parts\\" + oompID.value
        output = outputDirectory + "\\label-spec.svg" 
        outputPDF = outputDirectory + "\\label-spec.pdf" 
        if not os.path.isdir(outputDirectory):
            os.makedirs(outputDirectory)
        oompSearchAndReplace(template, output, item)
        oompMakePDF(output,outputPDF)
    



def oompSearchAndReplace(inFile,outFile,item):
    oompID = item.getTag("oompID")
    
    f = open(inFile, "r")
    template = f.read()
    f.close()

    template = template.replace("%%ID%%", oompID.value)

    
    splitters = ["@1","@@"]
    for y in splitters:
        delim = y
        ##matches = re.findall(r'@1.+?@1',template)
        matches = re.findall(delim + '.+?' + delim,template)

        ##  CODE
        ##  @@@1%%ID%%,oompPart.oompID,oompDesc@1,oompDesc.code,name@@

        ##  PART DETAIL
        ##  @@%%ID%%,oompPart.oompID,name@@

        for x in matches:
##            print(x)
            #remove deliminator
            orig = x
            x = x.replace(delim,"")
            #split replace
            splitTag = x.split(",")
            if len(splitTag) > 1:
                style = splitTag[1]
                tag = splitTag[2]
                if "oompPart" in style:
                    part = OOMP.getPartByID(str(splitTag[0]))
                    ##print(part)
                    replaceValue = part.getTag(tag).value
##                    print("        Replacing: " + x + " with -- " + replaceValue )
                    template = template.replace(orig,replaceValue)
                else: ##detail
                    cat = ""
                    if "oompType" in style:
                        cat = "type"
                    elif "oompSize" in style:
                        cat = "size"
                    elif "oompColor" in style:
                        cat = "color"
                    elif "oompDesc" in style:
                        cat = "desc"
                    elif "oompIndex" in style:
                        cat = "index"
                    
                    replaceValue = OOMP.getDetailByCode(cat,splitTag[0]).name
##                    print("        Replacing: " + x + " in " + cat + " with -- " + replaceValue )
                    template = template.replace(orig,replaceValue)
                
    
    f = open(outFile, "w+")
    f.write(template)
    f.close

def oompMakePDF(inFile,outFile):
    executeString = "inkscape.exe --export-filename=\"" + outFile + "\" \"" + inFile + "\""
    print("                Converting to PDF: " + inFile)
    subprocess.call(executeString)
    


####Test One Label Generation
##part = OOMP.parts[256]
##print(part)
##generateLabel(part)



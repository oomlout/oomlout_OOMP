from oomBase import *
import OOMP

def harvestParts(item,overwrite = False):
    eagleParts = item.getFilename("eagleParts")
    partsPython = item.getFilename("pythonParts")
    if overwrite or not os.path.exists(partsPython): 
        print("Harvesting Parts For: " + str(item))
        parts = oomReadFileToString(eagleParts)
        lines = parts.splitlines()    
        process = False
        parts = []
        oompParts = []
        multiplier = 1
        for line in lines:
            line = line.replace("µ","u").replace("�","").replace('"',"").replace("'","")
            ######  skip"'" until getting to part line
            if process:
                parts.append(line.split())
            if "Part " in line:
                process = True  
                if "(inch)" in line:
                    multiplier = 25.4              
        for part in parts:
            ######missing value
            if len(part) == 6:
                part = [part[0],"",part[1],part[2],part[3],part[4],part[5]]
            if len(part) > 4:
                try:
                    ##### oompID, part, x, y, rotation
                    oompID = matchPart(item,part)
                    partName = part[0]
                    x = part[4].replace("(","")
                    y = part[5].replace(")","")
                    rotation = part[6].replace("R","")

                    oompParts.append([oompID,partName,float(x)*multiplier,float(y)*multiplier,rotation])
                except:
                    oompParts.append(["ERROR",part[0] + " " + part[1] + " " + part[2],0,0,0])


        if len(oompParts) > 0:
            makePartsFile(item,oompParts,parts)

        #oomDelay(30)        

def makePartsFile(item,oompParts,rawParts):
    partsFile = item.getFilename("pythonParts")
    projectID = item.getTag("oompID").value
    contents = ""

    contents = contents + "import OOMP" + "\n"
    contents = contents + 'newPart = OOMP.getPartByID("' + projectID + '")\n'
    
    contents = contents + "" + "\n"

    for part in oompParts:
        partString = str(part).replace("[","",).replace("]","",).replace("'","",)

        contents = contents + 'newPart.addTag("oompPart","' +partString + '")' + "\n"

    for part in rawParts:
        if partString != "":
            partString = str(part).replace("[","",).replace("]","",).replace("'","",)

            contents = contents + 'newPart.addTag("rawPart","' + partString + '")' + "\n"


    oomWriteToFile(partsFile,contents,utf=False)

def matchPart(project,part):

    PART = 0
    VALUE = 1
    PACKAGE = 2
    LIBRARY = 3

    oompType = "UNMATCHED"
    oompSize = "UNMATCHED"
    oompColor = "UNMATCHED"
    oompDesc = "UNMATCHED"
    oompIndex = "UNMATCHED"                

    oompColor = "X"
    oompIndex= "01"


    partLetter = "".join([i for i in part[PART] if not i.isdigit()])
    partNumber = "".join([i for i in part[PART] if not i.isalpha()])
    valueLetter = "".join([i for i in part[VALUE] if not i.isdigit()])
    valueNumber = "".join([i for i in part[VALUE] if not i.isalpha()])
    packageLetter = "".join([i for i in part[PACKAGE] if not i.isdigit()]).replace("-","")
    packageNumber = "".join([i for i in part[PACKAGE] if not i.isalpha()]).replace("-","")

    ###### TYPE

    if partLetter == "C":
        if float(valueNumber) < 20:
            oompType = "CAPC"
        else:
            oompType = "CAPE"
    if partLetter == "R":
        oompType = "RESE"

    if partLetter == "FID":
        oompType = "SKIP"
    if partLetter == "U$":
        oompType = "SKIP"


    ######  SIZE

    if packageNumber == "0805":
        oompSize = "0805"
    if packageNumber == "0402":
        oompSize = "0402"
    if packageNumber == "0603":
        oompSize = "0603"


    ###### common capacitor values
    if part[VALUE] == "0.01uF":
        oompDesc = "NF10"
    if part[VALUE] == "0.1uF":
        oompDesc = "NF100"
    if part[VALUE] == "100nF":
        oompDesc = "NF100"
    if part[VALUE] == "10uF":
        oompDesc = "UF10"
    if part[VALUE] == "22pF":
        oompDesc = "PF22"
    if part[VALUE] == "100pF":
        oompDesc = "PF100"
    if part[VALUE] == "10pF":
        oompDesc = "PF10"


    oompID = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex

    if oompType == "CAPC" and oompDesc == "NF100":
        oompIndex = "V50"
    if oompType == "CAPC" and oompDesc == "UF10":
        oompIndex = "V25"


    ###### common resistor values
    if part[VALUE] == "10K":
        oompDesc = "O103"
    if part[VALUE] == "1K":
        oompDesc = "O102"
    if part[VALUE] == "100K":
        oompDesc = "O104"
    if part[VALUE] == "22K":
        oompDesc = "O223"
    if part[VALUE] == "2.2K":
        oompDesc = "O222"
    if part[VALUE] == "1M":
        oompDesc = "O105"
    if part[VALUE] == "220":
        oompDesc = "O221"
    if part[VALUE] == "330":
        oompDesc = "O331"



    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    return rv



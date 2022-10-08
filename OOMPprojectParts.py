from oomBase import *
import OOMP




def replaceOddChars(line):
    rv = line
    rv = rv.replace("µ","u")
    rv = rv.replace("±","+/-")
    rv = rv.replace("Ω","ohm")
    rv = rv.replace("Ω","ohm") ##ohm
    rv = rv.replace(";",",")
    rv = rv.replace("'","")
    return rv

def harvestParts(item,overwrite=False):
    ###### Try eagle File
    oompFile = "eagleBOM"

    if item.ifFileExists(oompFile):
        parts = oomReadFileToString(item.getFilename(oompFile))
        parts = parts.split("\n")

        ###### remove tags before starting
        for c in range(0,10):
            item.removeTag("rawParts")

        for part in parts:
            if '"Part";"Value"' in part or part == '':
                pass #skip title line
            else:
                value = part
                item.addTag("rawParts",value.replace("'","").replace(";",",").replace('"','')) ##switch from semi colons to commas and remove apostrophes
    else:
        oompFile = "kicadBOM"
        test = item.getTag("oompSize").value
        if test == "SOPA":
            pass
        if item.ifFileExists(oompFile):
            parts = oomReadFileToString(item.getFilename(oompFile))
            parts = parts.split("\n")

            ###### remove tags before starting
            for c in range(0,10):
                item.removeTag("rawParts")

            for part in parts:
                if '"Id";"Designator"' in part or part == '':
                    pass #skip title line
                else:
                    value = part
                    values = value.split(";")
                    identifiers = values[1].replace('"',"").split(",")
                    for identifier in identifiers:
                        partString = identifier + "," +  values[4].replace('"',"") +  "," +  values[2].replace('"',"") + "," + values[2].replace('"',"") + ",,,,"
                        item.addTag("rawParts",partString) ##switch from semi colons to commas and remove apostrophes
    item.exportTags("detailspartsRaw",["rawParts"])




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
        partString = str(part).replace("[","",).replace("]","",).replace("'","",)

        contents = contents + 'newPart.addTag("rawPart","' + partString + '")' + "\n"


    oomWriteToFile(partsFile,contents,utf=False)


def loadInstances(project):
    oompID = project.getID()
    parts = project.getTags("oompParts")
    if len(parts) > 0:
        for part in parts:
            deets = part.value.split(",")
            p = {}
            p["PROJECT"] = oompID
            p["ID"] = deets[0]
            oompPart = OOMP.getPartByID(deets[1])
            partID = oompPart.getID()
            if partID != "----":
                oompPart.addTag("oompInstances",p)
            else:
                if not "UNMATCHED" in deets[1] :
                    print("SKIPPING: " + deets[1])


def matchFootprintsR(project,overwrite=False):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM
    ###### remove tags before starting
    for c in range(0,100):
        project.removeTag("footprintEagle")
        project.removeTag("footprintKicad")        
        project.removeTag("symbolKicad")        
        project.removeTag("symbolEagle")
    parts = project.getTags("allParts")
    for part in parts:
        p = part.value.split(",")
        dict = {
            "IDENTIFIER" : p[0],
            "OOMPID" : p[1],
            "VALUE" : p[3],
            "DESC" : p[4],
            "PACKAGE" : p[5],
            "INFO" : p[6],
            "OWNER" : project.getTag("oompSize").value
        }        
        oompPart = OOMP.getPartByID(dict["OOMPID"])
        matchFootprint(project,oompPart,dict)

def matchFootprint(part):
    for c in range(0,100):
        part.removeTag("footprintEagle")
        part.removeTag("footprintKicad")        
        part.removeTag("symbolKicad")        
        part.removeTag("symbolEagle")
    dict = {}
    #projectID = project.getID()
    oompID = part.getID()
    oompType = part.getTag("oompType").value
    oompSize = part.getTag("oompSize").value
    oompColor = part.getTag("oompColor").value
    oompDesc = part.getTag("oompDesc").value
    oompIndex = part.getTag("oompIndex").value
    print("Matching Footprint for: " + "  " + oompID)
    if oompID != "----":
        if oompType == "HEAD":
            addHEADSymbols(part,dict)        
        if "HEAD-I01" in oompID and oompIndex == "01":
            addHEAD01(part,dict)
        if "HEAD-I01" in oompID and oompIndex =="SHRO":
            addHEAD01SHRO(part,dict)
        if "HEAD-JSTXH" in oompID and oompIndex == "01":
            addHEADJSTXH(part,dict)
        if "HEAD-JSTSH" in oompID and oompIndex == "SM":
            addHEADJSTSH(part,dict)
        if "HEAD-JSTSHR" in oompID and oompIndex == "RS":
            addHEADJSTSH(part,dict)
        if oompSize == "0805":
            add0805(part,dict)
        if oompType == "TERS":
            addTERSSymbols(part,dict)
        if "TERS-35D-" in oompID:
            addTERS35D(part,dict)

    else:
        "    SKIPPING"

#part.addTag("footprintEagle", "")
#part.addTag("footprintKicad", "")
def add(part,dict):
    oompType = part.getTag("oompType").value
    tags = []
    tags.append(["footprintEagle", ""])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)
    tags = []
    tags.append(["footprintKicad", ""])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)



def add0805(part,dict):
    oompType = part.getTag("oompType").value
    tags = []
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1W"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1R"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AW"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-085CS_1AR"])
    if "RES" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805-ARV"])
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Resistors-0805"])
    if "CAP" in oompType:
        tags.append(["footprintEagle", "FOOTPRINT-eagle-SparkFun-Eagle-Libraries-SparkFun-Capacitors-0805"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805_SENSE"])
    tags.append(["footprintEagle", "FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-rc-0805"])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)
    tags = []
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric"])
    tags.append(["footprintKicad", "FOOTPRINT-kicad-kicad-footprints-Capacitor_SMD-C_0805_2012Metric_Pad1.18x1.45mm_HandSolder"])
    for tag in tags:
        part.addTag(tag[0],tag[1],noDuplicate=True)



def addHEADSymbols(part,dict):
    newPart = part
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI2X","")
    pinss = pinss.replace("PI","")
    if pinss.isnumeric():
        if "PI2X" in oompDesc:
                ###### FOOTPRINTS
                symbols = []
                symbols.append("SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + pinss*2 + "_Male")
                symbols.append("SYMBOL-kicad-kicad-symbols-Connector-DIN41612_02x" + pinss + "_AB")
                base = "SYMBOL-kicad-kicad-symbols-Connector-Conn_02x" + pinss
                symbols.append(base  + "_Row_Letter_First")
                symbols.append(base  + "_Row_Letter_Last")
                symbols.append(base  + "_Counter_Clockwise")
                symbols.append(base  + "_Odd_Even")
                symbols.append(base  + "_Top_Bottom")
                for symbol in symbols:
                    ###### TODO add a check for existance
                    newPart.addTag("symbolKicad",symbol)
        else:
            newPart.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Connector-Conn_01x" + pinss + "_Male")
            newPart.addTag("symbolKicad","SYMBOL-kicad-kicad-symbols-Connector_Generic-Conn_01x" + pinss + "")



def addHEAD01(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        ###### FOOTPRINTS
        ##newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        ######  Sparkfun footprints
        sparkfunStyles = ["", "_BIG", "_LOCK", "_LOCK_LONGPADS", "_NO_SILK", "_PP_HOLES_ONLY"]
        for style in sparkfunStyles: 
            imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style + "/image.png"
            #print("Image File: " + imageFile)
            if os.path.isfile(imageFile):
                newPart.addTag("footprintEagle","FOOTPRINT-eagle-SparkFun-Eagle-Libraries-Sparkfun-Connectors-1X" + pinss + style)
        
        
        adafruitStyles = ["", "-CLEANBIG", "-BIGLOCK", "-CLEAN", "-LOCK", "-CB"]
        for style in adafruitStyles: 
            imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Adafruit-Eagle-Library/adafruit/1X" + pinss + style + "/image.png"
            #print("Image File: " + imageFile)
            if os.path.isfile(imageFile):
                newPart.addTag("footprintEagle","FOOTPRINT-eagle-Adafruit-Eagle-Library-adafruit-1X" + pinss + style)
        
        
        pimoroniStyles = ["","-0.1&quot;-CASTELLATED-BCREAM", "-0.1&quot;-CASTELLATED-BIGGER-ROUNDED", "-0.1&quot;-CASTELLATED-BIGGER", "-0.1&quot;-CASTELLATED", "-LOCK-MALE", "-CB","_LONGPADS"]
        for style in pimoroniStyles: 
            imageFile = "oomlout_OOMP_eda/FOOTPRINT/eagle/Pimoroni-Eagle-Library/pimoroni-headers/1X" + pinss.replace("0","") + style + "/image.png"
            #print("Image File: " + imageFile)
            if os.path.isfile(imageFile):
                newPart.addTag("footprintEagle","FOOTPRINT-eagle-Pimoroni-Eagle-Library-pimoroni-headers-1" + pinss + style)
        
        newPart.addTag("footprintKicad","FOOTPRINT-kicad-kicad-footprints-Connector_PinHeader_2.54mm-PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        

def addHEAD01SHRO(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI2X","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_IDC-IDC-Header_2x" + pinss
        footprints.append(base + "_P2.54mm_Horizontal")
        footprints.append(base + "_P2.54mm_Vertical")


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTSH(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        #JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_BM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Vertical"
        footprints.append(base)


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTSHR(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM04B-SRSS-TB_1x04-1MP_P1.00mm_Horizontal
        
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_SH_SM" + pinss + "B-SRSS-TB_1x" + pinss + "-1MP_P1.00mm_Horizontal"
        footprints.append(base)


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)

def addHEADJSTXH(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        #FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B10B-XH-AM_1x10_P2.50mm_Vertical
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-AM_1x" + pinss
        footprints.append(base + "_P2.50mm_Vertical")
        base = "FOOTPRINT-kicad-kicad-footprints-Connector_JST-JST_XH_B" + str(int(pinss)) + "B-XH-A_1x" + pinss
        footprints.append(base + "_P2.50mm_Vertical")


        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)


def addTERSSymbols(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        ###### FOOTPRINTS
        symbols = []
        base = "SYMBOL-kicad-kicad-symbols-Connector-Screw_Terminal_01x" + pinss
        symbols.append(base)
        for symbol in symbols:
            ###### TODO add a check for existance
            newPart.addTag("symbolKicad",symbol)

def addTERS35D(part,dict):
    oompDesc = part.getTag("oompDesc").value
    pinss = oompDesc.replace("PI","")
    newPart = part
    if pinss.isnumeric():
        footprints = []
        base = "FOOTPRINT-kicad-kicad-footprints-TerminalBlock_4Ucon-TerminalBlock_4Ucon_1x" + pinss
        footprints.append(base + "_P3.50mm_Vertical")
    
        for footprint in footprints:
            newPart.addTag("footprintKicad",footprint)  
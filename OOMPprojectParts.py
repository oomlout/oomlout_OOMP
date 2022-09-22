from oomBase import *
import OOMP
import re




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


def matchParts(project):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM
    ###### remove tags before starting
    for c in range(0,10):
        project.removeTag("oompParts")
    parts = project.getTags("rawParts")
    for part in parts:
        part = part.value.split(",")
        oompPart = matchPart(project,part)
        if not "SKIP-" in oompPart:
            project.addTag("oompParts", part[PART] + "," + oompPart)

    project.exportTags("detailsPartsOomp",["oompParts"])    



def matchPart(project,part):
    for x in range(0,len(part)):
        part[x] = part[x].replace('"','')


    oompType = matchType(project,part)
    oompSize = matchSize(project,part,oompType=oompType)
    oompColor = matchColor(project,part,oompType=oompType,oompSize=oompSize)
    oompDesc = matchDesc(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor)
    oompIndex = matchIndex(project,part,oompType=oompType,oompSize=oompSize,oompColor=oompColor,oompDesc=oompDesc)  


    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    return rv

PART = 0
VALUE = 1
DEVICE = 2
PACKAGE = 3
DESC = 4
BOM = 5



def getUseful(part,name):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = ""
    if name == "partLetter":
        rv = re.sub(r'\d+', '', part[PART])
    if name == "packageNumber":
        rv = re.sub(r'\D+', '', part[PACKAGE])
    if name == "valueNumber":
        rv = re.sub(r'[a-zA-Z]+', '', part[VALUE])    ######  Maintains full stop for decimal

    return rv

def loadPartDict(part,project):
    global PART, VALUE, DEVICE, PACAKAGE, DESC, BOM
    rv = {}
    part[VALUE] = part[VALUE].replace("Ã\x82Âµ","U") ###### unicode micro fix
    rv["PART"] = part[PART]
    rv["PARTLETTER"] = getUseful(part,"partLetter")
    rv["VALUE"] = part[VALUE]
    rv["VALUENUMBER"] = getUseful(part,"valueNumber")
    rv["DEVICE"] = part[DEVICE]
    rv["PACKAGE"] = part[PACKAGE]    
    rv["PACKAGENUMBER"] = getUseful(part,"packageNumber")
    rv["DESC"] = part[DESC]
    rv["BOM"] = part[BOM]
    rv["OWNER"] = project.getTag("oompSize").value

    if rv["PART"] == "C13":
        pass

    return rv

def loadProjectDict(project):
    rv = {}
    rv["OWNER"] = project.getTag("oompSize").value
    rv["INDEX"] = project.getTag("oompColor").value
    

    return rv


def matchType(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    partDict = loadPartDict(part,project)    
    rv= "UNMATCHED"

    ###### Getting useful items
    partLetter = getUseful(part,"partLetter")
    #partNumber = re.sub(r'\d+', '', part[PART])


    ###### BUTTONS
    tests = ["KMR2","EVQ-Q2"]
    for test in tests:
        if test in partDict["PACKAGE"].upper():
            rv = "BUTA"


    ###### Capacitor
    if partDict["PARTLETTER"] == "C" or "UF" in partDict["VALUE"].upper() :
        rv = "CAPX"
        ###### CAPC test
        tests = ["0805","0603","0402","1206"]
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPC"
        tests = ["EIA3216"]
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPT"
        tests = ["PANASONIC_B","PANASONIC_C","PANASONIC_D","PANASONIC_D8","PANASONIC_E","PANASONIC_F","PANASONIC_G"]                
        for test in tests:
            if test in partDict["PACKAGE"]:
                rv = "CAPE"
    ###### DCJACK
    tests = ["POWER_JACK"]
    for test in tests:
        if test in partDict["VALUE"].upper():
            rv = "DCJP"

    ###### DIODE
    if partDict["PARTLETTER"] == "D":
        if "APA102" in partDict["VALUE"] or "LED" in partDict["PACKAGE"]:
            return "LEDS"
        rv = "DIOD"

    ###### FERITE BEAD
    if partDict["PARTLETTER"] == "FB":
        rv = "FERB"

    ###### HEADER
    if "HEADER" in partDict["DEVICE"].upper():
        rv = "HEAD"
    if "HEADER" in partDict["DESC"].upper():
        rv = "HEAD"
    if partDict["PARTLETTER"].upper() == "JP":
        if "1X" in partDict["PACKAGE"].upper():
            rv = "HEAD"
    if "STEMMA_I2C" in partDict["VALUE"].upper():
        rv = "HEAD"
    if "QWIIC_CONNECTOR" in partDict["VALUE"].upper() or "QWIIC RIGHT" in partDict["VALUE"].upper():
        rv = "HEAD"        

    ###### LED
    if partDict["DEVICE"].startswith("LED") or partDict["PART"].startswith("LED"):
        rv = "LEDS"


    ###### MOSFETS
    if "N-CHANNEL MOSFET" in partDict["DESC"].upper():
        rv = "MOSN"
    if "P-CHANNEL MOSFET" in partDict["DESC"].upper():
        rv = "MOSP"

    ###### PTC
    if "PTCSMD" in partDict["DEVICE"]:
        return "REFU"

    ###### Terminal Strip
    list = []
    list.append(["SCREWTERMINAL","TERS"])
    list.append(["-3.5MM","TERS"])
    for l in list:
        if l[0] in partDict["PACKAGE"].upper():
            return l[1]

    ######Resistor
    if partDict["PARTLETTER"] == "R" or partDict["PART"] == "R-PROG2":
        if "RESPACK_4X0603" in partDict["PACKAGE"]:
            return "RESA"
        else:
            return "RESE"



    ######  Voltage Regulators
    options = []
    options.append("MIC5225")
    options.append("MIC5205")
    options.append("LP298XS")
    options.append("AP2112K")
    for option in options:
        if option in partDict["VALUE"] or option in partDict["DEVICE"]:
            return "VREG"


    ###### SKIP
    ###### BOM
    list = []
    list.append("EXCLUDE")
    for l in list:
        if l in partDict["BOM"]:
            rv = "SKIP"

    ###### VALUE
    list = []
    list.append("ALLIGATOR")
    list.append("CREATIVE")
    list.append("ELAST")
    list.append("FIDUCIAL")
    list.append("FRAME")
    list.append("GATOR")
    list.append("JUMPER-SMT")
    list.append("LOGO")
    list.append("M01SNAP") 
    list.append("MOUSE-BITE")  
    list.append("MOUNTINGHOLE")    
    list.append("PERFHOLE")
    list.append("PAD")
    list.append("REVISION")
    list.append("SINGLE_PAD")
    list.append("STAND-OFF")
    list.append("STANDOFF")
    list.append("SOLDERJUMPER")
    list.append("SOLDER_PAD")
    list.append("DNP")
    list.append("SEWTAP")
    list.append("TAB_GATOR")
    list.append("TESTPOINT")
    list.append("TEST-POINT")
    list.append("TPTP20R")
    list.append("TP_")
    for l in list:
        if l in partDict["VALUE"]:
            rv = "SKIP"
    ###### DEVICE
    list = []
    list.append("JUMPER-PAD")
    list.append("SOLDERJUMPER")
    list.append("TESTPOINT")
    for l in list:
        if l in partDict["DEVICE"]:
            rv = "SKIP"            
        

    

    return rv

def matchSize(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    partDict = loadPartDict(part,project)    
    rv= "UNMATCHED"

    ######direct replacments
    tests = ["0805","0603","0402","1206"]
    for test in tests:
        if partDict["PACKAGENUMBER"] == test:
            rv = test



    ###### CAPACITORS
    if oompType == "CAPE":
        list = []
        list.append(["PANASONIC_B","PANB"])
        list.append(["PANASONIC_C","PANC"])
        list.append(["PANASONIC_D","PAND"])
        list.append(["PANASONIC_D8","PAD8G"])
        list.append(["PANASONIC_E","PANE"])
        list.append(["PANASONIC_F","PANF"])
        list.append(["PANASONIC_G","PANG"])
        for l in list:
            if l[0] in partDict["PACKAGE"]:
                return l[1]

    ######  DC JACK
    if oompType == "DCJP":
        rv = "21D"
        if "JACKSMD" in partDict["DEVICE"]:
            return "S21D"


    ######headers
    if oompType == "HEAD":
        ###### not 0.1"
        exclusions = ["MM"]
        for exclusion in exclusions:
            if exclusion in partDict["PACKAGE"]:
                return "UNMATCHED"
        if "STEMMA_I2C" in partDict["VALUE"].upper():
            rv = "01"
        if "QWIIC_CONNECTOR" in partDict["VALUE"].upper() or "QWIIC RIGHT" in partDict["VALUE"].upper():
            rv = "01"                
        return "I01"



    ###### Screw Terminals
    if oompType == "TERS":
        if "3.5MM" in partDict["PACKAGE"]:
            return "35D"

    ######Pairs        
    ######  PACKAGE
    pairs = []
    pairs.append(["DO214","D214"])
    pairs.append(["EIA3216","3216"])
    pairs.append(["EIA3528","3528"])
    pairs.append(["EIA6032","6032"])
    pairs.append(["EIA7343","7343"])
    pairs.append(["SOD-123","S123"])
    pairs.append(["SOD-323","S323"])
    pairs.append(["SOT23-5","SO235"])
    pairs.append(["SOT23","SO23"])
    pairs.append(["SOT363","SO363"])
    pairs.append(["SOT23-5L","SO235"])
    pairs.append(["2121","2121"])
    pairs.append(["2020","2020"])
    pairs.append(["3535","3535"])
    pairs.append(["4.6X2.8","4628"])
    pairs.append(["5050","5050"])
    pairs.append(["EVQ-Q2","6060"])
    pairs.append(["RESPACK_4X0603","06038"])
    for pair in pairs:
        if pair[0] in partDict["PACKAGE"]:
            return pair[1]
    ######  DEVICE
    pairs = []
    pairs.append(["5050","5050"])
    for pair in pairs:
        if pair[0] in partDict["DEVICE"]:
            return pair[1]
    

    return rv

def matchColor(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    partDict = loadPartDict(part,project)   
    projectDict = loadProjectDict(project)

    rv= "X"

    if oompType == "LEDS":
        rv = "G"
        if "RGB" in partDict["VALUE"] or "2812" in partDict["VALUE"] or "2811" in partDict["VALUE"]:
            return "RGB"
        if "APA102" in partDict["PACKAGE"]:
            return "RGB"
        if projectDict["OWNER"] == "ADAF":
            if projectDict["INDEX"] == "3467":
                return "L"
            if projectDict["INDEX"] == "3134":
                return "R"
            if projectDict["INDEX"] == "2946":
                return "W"
        list = []
        list.append(["RED","R"])
        list.append(["ORANGE","O"])
        list.append(["YELLOW","Y"])
        list.append(["GREEN","G"])
        list.append(["BLUE","L"])
        list.append(["PINK","P"])

        for l in list:
            if l[0] in partDict["VALUE"].upper():
                return l[1]

    ######  SCREW TERMINAL
    if oompType == "TERS":        
        list = []
        list.append(["SCREWTERMINAL-3.5MM-","L"])
        list.append(["3.5MM","L"])

        for l in list:
            if l[0] in partDict["PACKAGE"].upper():
                return l[1]


    return rv

def matchDesc(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    partDict = loadPartDict(part,project)   
    rv= "UNMATCHED"


    ######  BUTTONS
    if oompType == "BUTA":
        rv = "STAN"

    if oompType.startswith("CAP"):
        ######  Capacitors
        if "UF" in partDict["VALUE"].upper() or partDict["VALUE"].upper().endswith("U"):
            ###### full uf
            for x in range(1,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    if x == 10:
                        return "UF" + str(int(x/10))            
                    return "UF" + str(x) + "D"            
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "UF" + str(x)
        if "PF" in partDict["VALUE"].upper():
            ###### full uf
            for x in range(1,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x) + "D"
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x)
        if "NF" in partDict["VALUE"].upper():
            for x in range(1,99):
                test = str(x/10)
                if test == partDict["VALUENUMBER"]:
                    return "PF" + str(x) + "D"        
            ###### full uf
            for x in range(1,999):
                test = str(x)
                if test == partDict["VALUENUMBER"]:
                    return "NF" + str(x)
        list = []
        list.append([".1UF","NF100"])
        list.append([".1U","NF100"])
        list.append(["0.1UF","NF100"])
        list.append([".22UF","NF220"])
        list.append(["0.22UF","NF220"])
        list.append(["47UF","UF47"])



        for l in list:
            if l[0] in partDict["VALUE"].upper():    
                return l[1]
        
        ###### 0. uf
        for x in range(100,999):
            test = "0." + str(x)
            if test.startswith(partDict["VALUENUMBER"]):
                return "NF" + str(x)

    ################### DEBUG
    if partDict["PART"] == "PC1":
        pass    

    ######  DC JACKS
    if oompType == "DCJP":
        rv = "STAN"


    ######  Headers
    if oompType == "HEAD":
        exclusions = ["ZZZZZZZ"]
        for exclusion in exclusions:
            if exclusion in partDict["PACKAGE"]:
                return "UNMATCHED"
        for x in range(1,40):
            if "1X" + str(x).zfill(2) in partDict["PACKAGE"]:
                return "PI" + str(x).zfill(2)
            if "2X" + str(x).zfill(2) in partDict["PACKAGE"]:    
                return "PI2X" + str(x).zfill(2)
        if partDict["PART"]== "ICSP":                
            pass

        list = []
        list.append(["STEMMA_I2C","PI04"])
        list.append(["QWIIC_CONNECTOR","PI04"])
        list.append(["3X2","PI2X03"])
        for l in list:
            if partDict["VALUE"].upper() == l[0]:
                return l[1] + extra

    ######  Headers
    if oompType == "LEDS":
        rv = "STAN"

    ######  Resistors
    if oompType == "RESE" or oompType == "RESA":
        extra = ""
        if oompType == "RESA":
            if "4X" in partDict["PACKAGE"]:
                extra = "X4"
        for x in range(1,999):
            if partDict["VALUE"] == str(x):
                if x < 100:
                    twoDig = int(x)
                    return "O" + str(twoDig) + "0" + extra
                else:
                    twoDig = int(x/10)
                    return "O" + str(twoDig) + "1"  + extra
            if partDict["VALUE"].upper() == str(x) + "K":
                if x < 10:
                    twoDig = int(x*10)
                    return "O" + str(twoDig) + "2"  + extra
                elif x < 1000: 
                    twoDig = int(x)
                    return "O" + str(twoDig) + "3" + extra
                else:
                    twoDig = int(x/10)
                    return "O" + str(twoDig) + "4"     + extra
            if partDict["VALUE"].upper() == str(x) + "M":
                if x < 10:
                    twoDig = int(x*10)
                    return "O" + str(twoDig) + "5"     + extra
                else:
                    twoDig = int(x)
                    return "O" + str(twoDig) + "6"    + extra
        list = []
        list.append(["1.0K","O102"])
        list.append(["2.2K","O222"])
        list.append(["3.9K","O392"])
        list.append(["4.7K","O472"])
        list.append(["5.1K","O472"])
        for l in list:
            if partDict["VALUE"].upper() == l[0]:
                return l[1] + extra


    ######Pairs   
    # ####### VALUE     
    pairs = []
    pairs.append(["1N4148","K4148"])
    pairs.append(["2811","K2811"])
    pairs.append(["2812","K2812"])
    pairs.append(["MBR120","KMBR120"])
    pairs.append(["BSS138","KBSS138"])
    pairs.append(["IRLML6401","K6401"])
    pairs.append(["MIC5225","KMIC5225"])
    pairs.append(["MIC5205","KMIC5205"])
    pairs.append(["LP298XS","KLP298XS"])
    pairs.append(["AP2112K","KAP2112K"])
    pairs.append(["MMZ1608B121C","O121"])
    
    for pair in pairs:
        if pair[0].upper() in partDict["VALUE"].upper():        
            return pair[1]
        if oompType == "VREG":
            if pair[0].upper() in partDict["DEVICE"].upper():        
                return pair[1]
    # ####### PACKAGE     
    pairs = []
    pairs.append(["1X2-3.5MM","PI02"])
    pairs.append(["1X3-3.5MM","PI03"])
    pairs.append(["1X4-3.5MM","PI04"])
    pairs.append(["1X5-3.5MM","PI05"])
    pairs.append(["1X6-3.5MM","PI06"])
    pairs.append(["1X7-3.5MM","PI07"])
    pairs.append(["1X8-3.5MM","PI08"])
    pairs.append(["SCREWTERMINAL-3.5MM-2","PI02"])
    pairs.append(["SCREWTERMINAL-3.5MM-3","PI03"])
    pairs.append(["SCREWTERMINAL-3.5MM-4","PI04"])
    pairs.append(["SCREWTERMINAL-3.5MM-8","PI08"])
    pairs.append(["APA102","K102"])
    for pair in pairs:
        if pair[0].upper() in partDict["PACKAGE"].upper():        
            return pair[1]

                
    return rv

def matchIndex(project,part,oompType="",oompSize="",oompColor="",oompDesc="",oompIndex=""):
    global PART, VALUE, DEVICE, PACAKGE, DESC, BOM    
    rv= "01"
    partID = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc
    partDict = loadPartDict(part,project)   

    ######  Cap\acitor Voltage matching
    ###### V50
    list = []
    v = "CA"
    list.append(["LEDS-2121-RGB-STAN",v])
    v = "RS"
    list.append(["HEAD-01-X-PI04",v])
    
    v = "V33D"
    list.append(["VREG-SO235-X-KAP2112K",v])
    list.append(["VREG-SO235-X-KLP298XS",v])
    list.append(["VREG-SO235-X-KMIC5225",v])
    v = "V10"
    list.append(["CAPC-0805-X-UF10",v])
    v = "V50"
    list.append(["CAPC-0603-X-NF100",v])
    list.append(["CAPC-0805-X-NF100",v])    
    for l in list:
        if l[0] == partID:
            return l[1]
       

    list = []
    list.append(["MIC52055V","V5"])
    
    for l in list:
        if l[0] == partDict["VALUE"]:
            return l[1]

    if oompType.startswith("CAP"):
        list = []
        list.append(["25V","V25"])
        list.append(["6.3V","V63D"])        
                
        for l in list:
            if l[0] in partDict["VALUE"]:
                return l[1]

        ################### DEBUG
    if partDict["PART"] == "PC1":
        pass    


    return rv        








##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

def matchPartOld(project,part):

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

    valueNumber = valueNumber.replace("+","")

    ###### TYPE

    if partLetter == "C":
        try:
            if float(valueNumber) < 20:
                oompType = "CAPC"
            else:
                oompType = "CAPE"    
        except:
            c=0

    if partLetter == "R":
        oompType = "RESE"

    ####### skip test

    skipList = [
        ["fid","SKIP"],
        ["mountinghole","SKIP"],
        ["fiducial","SKIP"],
        ["gator","SKIP"],
        ["wpj","SKIP"],
        ["test","SKIP"],
        ["solder","SKIP"],
        ["pad-jumper","SKIP"],
        ["sewtap","SKIP"],
        ["sewingtap","SKIP"],
        ["tp","SKIP"],
        ["sj","SKIP"]
    ]

    for skip in skipList:
        if skip[0] in part[PART].lower() :
            oompType = skip[1]
        if skip[0] in part[PACKAGE].lower() :
            oompType = skip[1]
    

    ######  SIZE

    sizeList = [
        ["0805","0805"],
        ["805","0805"], 
        ["0805-","0805"],
        ["_0805","0805"],
        ["0603","0603"],
        ["603","0603"], 
        ["0603-","0603"],
        ["_0603","0603"],
        ["0402","0402"],
        ["402","0402"], 
        ["0402-","0402"],
        ["_0402","0402"],
        ["1210","1210"]
    ]

    for swap in sizeList:
        if part[PACKAGE].lower() == swap[0]:
            oompSize = swap[1]
        if packageNumber.lower() == swap[0]:
            oompSize = swap[1]    

    ###### headerss

    headIncludeList =[["1x","HEAD" ]
    ]

    headExcludeList =["mm","jst", "fiducial", "mil", "screw"]


    package = part[PACKAGE].lower()
    value = part[VALUE].lower()
    name = part[PART].lower()


    if "jp" in name:
        for swap in headIncludeList:
            if swap[0] in package or swap[0] in name:
                include = True
                for skip in headExcludeList:
                    if skip in package or skip in name:
                        include =False
                    if include:
                        oompType = "HEAD"
                        oompSize = "I01"
                        packageSan = packageNumber.replace("_76","").replace("_70","").replace("-","").replace("_","")
                        oompDesc = "PI" + packageSan.zfill(2)[1:]


    ###### LEDs

    ledList =[["led","LEDS" ]
            ]
    if part[PART].lower() == "l":
        oompType = "LEDS"

    for swap in ledList:

        if part[PART].lower() == swap[0]:
            oompType = swap[1]
            if "2812" in part[PACKAGE] or "APA" in part[PACKAGE] or  "2811" in part[PACKAGE] or  "RGB" in part[PACKAGE]:
                oompColor = "RGB"
            elif "red" in part[VALUE].lower():
                oompColor = "R"
            elif "green" in part[VALUE].lower():
                oompColor = "G"
            elif "blue" in part[VALUE].lower():
                oompColor = "L"
            elif "white" in part[VALUE].lower():
                oompColor = "W"
            elif "yellow" in part[VALUE].lower():
                oompColor = "Y"
            else:
                oompColor = "G"
    ###### common capacitor values

    descList = [["0.01uf","NF10" ],
                ["2.2pf","PF22D" ],
                ["1000pf","NF1" ],
                ["2.2nf","NF22D" ],
                ["2200pf","NF22D" ],
                [".47uf","NF470" ],
                [".01uf","NF10" ],
                [".01uf","NF10" ],
                ["0.01uf","NF10" ],
                ["0.1uf","NF100" ],
                ["0.1u","NF100" ],
                ["0.22uf","NF220" ],
                [".22uf","NF220" ],
                ["0.33uf","NF330" ],
                [".33uf","NF330" ],
                ["0.39uf","NF390" ],
                [".39uf","NF390" ],
                ["0.47uf","NF470" ],
                [".47uf","NF470" ],
                ["0.5uf","NF500" ],
                [".5uf","NF500" ],
                ["0.68uf","NF680" ],
                [".68uf","NF680" ],
                ["0.75uf","NF750" ],
                [".75uf","NF750" ],
                ["0.8uf","NF800" ],
                [".8uf","NF800" ],
                ["2.2uf","UF22D" ],
                ["1000uf","UF1000"],
                ["100/6vuf","UF100"],
    ]

    values  = ["p","n","u"]
    steps = 999
    for value in values:
        for step in range(steps):
            descList.append([str(step) + value,value.upper() + "F" + str(step) ])
            descList.append([str(step) + "f" + value,value.upper() + "F" + str(step) ])
            descList.append([str(round(step,1)) + "f" + value,value.upper() + "F" + str(step) ])



    for swap in descList:
        if part[VALUE].replace("+","").replace("/10V","").replace("/16V","").replace("-25V","").replace("/50V","").replace("/2kV","").lower() == swap[0]:
            oompDesc = swap[1]


    oompID = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex

    if oompType == "CAPC" and oompDesc == "NF100":
        oompIndex = "V50"
    ###### default to v50 for small 0603 value caps    
    if oompType == "CAPC" and oompSize == "0603" and ("NF" in oompDesc or "PF" in oompDesc)  :
        oompIndex = "V50"        
    if oompType == "CAPC" and oompDesc == "UF10":
        oompIndex = "V25"


    ###### common resistor values
    if oompType == "RESE":
        descList = [
            ["10K","O103"],
            ["1K","O102"],
            ["2K","O202"],
            ["3K","O302"],
            ["4K","O402"],
            ["5K","O502"],
            ["6K","O602"],
            ["7K","O702"],
            ["8K","O802"],            
            ["9K","O902"],
            ["100K","O104"],
            ["22K","O223"],
            ["2.2K","O222"],
            ["1M","O105"],
            ["2M","O205"],
            ["3M","O305"],
            ["4M","O405"],
            ["5M","O505"],
            ["6M","O605"],
            ["7M","O705"],
            ["8M","O805"],
            ["9M","O905"],
            ["220","O221"],
            ["330","O331"]
        ]

        first = 99
        zeros=6
        for zero in range(3,zeros):
            for num in range(10,first):
                if zero < 2:
                    test = num * pow(10,zero)
                elif zero < 5:
                    test = str(round(num * pow(10,zero-3),1)) + "k"
                else:
                    test = str(round(num * pow(10,zero-6),1)) + "M"   
                result = "O" + str(num) + str(zero)
                descList.append([test , result])

        for swap in descList:
            if part[VALUE].replace("+","").replace("/10V","").replace("/16V","").replace("-25V","").replace("/50V","").replace("/2kV","").lower() == swap[0]:
                oompDesc = swap[1]
            if valueNumber == swap[0]:
                oompDesc = swap[1]

    rv = oompType + "-" + oompSize + "-" + oompColor + "-" + oompDesc + "-" + oompIndex
    return rv


def harvestPartsOld(item,overwrite = False):
    print("#############################################################")
    print("#############################################################")
    print("#############################################################")
    print("#############################################################")
    print("######  SHOULDN'T BE BEING USED ANYMORE  #######")
    print("######  harvestPartsOld(item,overwrite = False):  #######")
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
            line = line.replace("µ","u").replace("�","").replace('"',"").replace("'","").replace("±","+/-").replace("�","")
            ######  skip"'" until getting to part line
            if process:
                if line != "":
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

                    ##### oompID, part, x, y, rotation
                oompID = matchPart(item,part)
                try:                    
                    partName = part[0]
                    x = part[4].replace("(","")
                    y = part[5].replace(")","")
                    rotation = part[6].replace("R","")

                    oompParts.append([oompID,partName,float(x)*multiplier,float(y)*multiplier,rotation])
                except:
                    print("harvest parts error " + str(part))
                    oompParts.append(["ERROR",part[0] + " " + part[1] + " " + part[2],0,0,0])


        if len(oompParts) > 0:
            makePartsFile(item,oompParts,parts)

        #oomDelay(30)        

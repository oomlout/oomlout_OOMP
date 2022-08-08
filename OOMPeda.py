from oomBase import *
import OOMP
import os
import shutil

###### kicad mousepoints
X = 0
Y = 0
kicadActive =[515,14]
kicadFootprintFilter =[145,114]
kicadFootprintFirstResult = [145,185]
kicadFootprintMiddle = [945,545] 
kicadFootprintMiddlePlus = [950,550] 
kicadFootprintTopLeft = [365,86] 
kicadSymbolMiddle = [1105,555] 
kicadSymbolMiddlePlus = [1110,560] 

kicadFile = [80,35]
kicad3dView = [145,35]


kicadLibraryTop = [210,115]


eagleFootprintFilter = [200,680]
eagleFootprintFirstResult = [130,90]
eagleFootprintAddOk = [828,720]
eagleFootprintMiddle = [970,600]
eagleFootprintMiddlePlus = [eagleFootprintMiddle[0]+5,eagleFootprintMiddle[1]+5] 
eagleCloseText = [1100,260]
#eagleCrop = [820,180,800,800]
eagleCrop = [555,200,800,800]


###### need to remove to avoid name coNAMEnflicts
def harvestEagleLibraries(footprint=True,files=True, single=False, overwrite=False):
 


    ###### PROCESS
        ###### Adarfuit             finished    2022-07-17
        ###### Sparkfun             finished    2022-07-17    
        ###### Eagle     
        #           Tier one        finshed    2022-07-17       
        #           Tier two        finshed    2022-07-17       


    ######  Defaults
        ######  Pinhead
    #owner = "eagle-default"
    #libraryName="pinhead"     
    #library="C:/EAGLE 9.6.2/cache/lbr/" + libraryName +".lbr"    
    


    #owner = "eagle-default"
    #libraryName="pinhead"     

    directory="C:/EAGLE 9.6.2/cache/lbr/"
    owner = "eagle-default"
    
    if False:
    #if True:
        all = True
        filters= [""]
        ## Connectors
        #filters = ["con-"] 
        ## massive package
        #filters = ["ref-packages"] 
        #tier one
        #filters = ["pinhead","diode","holes","led"] 
        #tier 2
        #filters = ["19inch","40xx","41xx","45xx","74ac-logic","allegro","altera"]
        #tier 3
        #filters = ["74ttl-din","altera-cyclone-II","altera-stratix-iv","am29-memory","battery","burr-brown","busbar","buzzer"] 
        #tier 4 including all connectors
        #filters = ["74xx-eu","atmel","capacitor-wima","chipcard-siemens","cirrus-logic","con-"]
        #tier 5
        #filters = ["amd-mach"] 
        #tier 6
        #filters = ["analog-devices"] 
        #tier
        #filters = ["avago"] 
        #tier
        #filters = [""] 
        #tier
        #filters = [""] 

        for subdir, dirs, files in os.walk(directory):
                for file in files:
                        print("testing Library: " + file)
                        if ".lbr" in file:
                            for filter in filters or all:
                                if filter in file:
                                #if filter + ".lbr" == file:
                                    library="C:/EAGLE 9.6.2/cache/lbr/" + file 
                                    libraryName = file.replace(".lbr","")   
                                    c=0                
                                    #if not single:
                                    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    


    sourceDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_eda/sourceFiles/"

    filters= [""]

    ######  Adafruit
    owner = "Adafruit-Eagle-Library"
    libraryName="adafruit"     
    library=sourceDir + owner + "/"  + libraryName +".lbr"       
    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    
    
    ######  Dangerous Prototypes
    owner = "DangerousPrototypes-Eagle-Library"
    libraryName="dp_devices.v6"     
    library=sourceDir + owner + "/"  + libraryName +".lbr"       
    #harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    

    ######  SEEED OPL
    owner = "OPL_Eagle_Library"
    directory=sourceDir + owner + "/Seeed_Fusion_PCBA_OPL_Component_Library_for_Eagle/"
    if single:
        for subdir, dirs, files in os.walk(directory):
                for file in files:
                        print("testing Library: " + file)
                        if ".lbr" in file:
                            for filter in filters or all:
                                if filter in file:
                                #if filter + ".lbr" == file:
                                    libraryName = file.replace(".lbr","")   
                                    library= directory + "/" + libraryName +".lbr"                                        
                                    c=0                
                                    #if not single:
                                    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    

    ######  Pimoroni
    owner = "Pimoroni-Eagle-Library"
    directory=sourceDir + owner + "/lbr/"
    if single:
        for subdir, dirs, files in os.walk(directory):
                for file in files:
                        print("testing Library: " + file)
                        if ".lbr" in file:
                            for filter in filters or all:
                                if filter in file:
                                #if filter + ".lbr" == file:
                                    libraryName = file.replace(".lbr","")   
                                    library=directory + "/" + libraryName +".lbr"                                        
                                    c=0                
                                    #if not single:
                                    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    


    ######  Sparkfun
    owner = "SparkFun-Eagle-Libraries"
    directory=sourceDir + owner + "/"
    if single:
        for subdir, dirs, files in os.walk(directory):
                for file in files:
                        print("testing Library: " + file)
                        if ".lbr" in file:
                            for filter in filters or all:
                                if filter in file:
                                #if filter + ".lbr" == file:
                                    libraryName = file.replace(".lbr","")   
                                    library=directory + "/" + libraryName +".lbr"                                        
                                    c=0                
                                    #if not single:
                                    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    


    ######  Watterot
    owner = "Watterot-Eagle-Libraries"
    directory=sourceDir + owner + "/"
    if single:
        for subdir, dirs, files in os.walk(directory):
                for file in files:
                        print("testing Library: " + file)
                        if ".lbr" in file:
                            for filter in filters or all:
                                if filter in file:
                                #if filter + ".lbr" == file:
                                    libraryName = file.replace(".lbr","")   
                                    library=sourceDir + owner + "/" + libraryName +".lbr"                                        
                                    c=0                
                                    #if not single:
                                    harvestEagleFootprint(library,libraryName, owner, footprint=footprint, files=files, overwrite=overwrite)    



def harvestKicadLibraries():    
    owner = "kicad-footprints"
    harvestKicadFootprintImages(owner)    
    owner = "CE_KiCadLib"
    harvestKicadFootprintImages(owner)



def harvestKicadFootprintFiles(owner):
    
    filterDir = ""
    footprints = getKicadFootprintNames(owner)
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")
        ######  Generate other files
    
    for footprint in footprints:
        if filterDir in footprint[1]:
            print("Making Files for: " + footprint[0] + "  -  " + footprint[1])
            copyKicadSourceFile(footprint,owner)
            makeKicadOompFile(footprint,owner)
            #delay(300)



### open footprint editor
def harvestKicadFootprintImages(owner):
    filterDir = ""
    footprints = getKicadFootprintNames(owner)
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")

    for footprint in footprints:
        if filterDir in footprint[1]:
            captureKicadFootprint(footprint,owner)
            copyKicadSourceFile(footprint,owner)
            makeKicadOompFile(footprint,owner)

#open symbol editor
def harvestKicadSymbolImages(owner):
    filterDir = ""
    symbols = getKicadSymbolNames(owner)
    numSymbols = len(symbols)
    print("Found " + str(numSymbols) + " symbols")
    ######  ScreenCapture
    for symbol in symbols:
        print("Symbol 1: " + symbol[1])
        if filterDir in symbol[1]:
            print(symbol)
            captureKicadSymbol(symbol,owner)


#open new PCB    
def harvestEagleFootprint(libraryFile,libraryName, owner, overwrite=False, footprint=True, files=True):
    footprints = getEagleFootprintNames(libraryFile,libraryName)
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")
    #delay(1)    
    for footprint in footprints:
        #skip asterisk files for the time being
        if not "*" in footprint[0]:  
            if footprint:
                captureEagleFootprint(footprint,owner,overwrite=overwrite,libraryName=libraryName)
            if files:
                copyEagleSourceFile(footprint,owner,libraryFile,overwrite=overwrite)
                makeEagleOompFile(footprint,owner,overwrite=overwrite)
    

def eagleResetLibrary():
    shortDelay=2
    ##focus window
    oomMouseClick(pos=kicadActive)
    oomDelay(shortDelay)    
    oomSendAltKey("l")
    delay(shortDelay)
    oomSend("m")
    oomDelay(60)
    oomSendRight(1)
    oomDelay(shortDelay)
    oomSendTab(2)
    oomDelay(shortDelay)
    oomSendControl("a")
    oomDelay(1)
    oomSendEnter()
    oomDelay(3)
    ## for long delays    
    oomDelay(120)
    oomSendEsc()

currentLibrary = ""

def eagleSetLibrary(libraryName):
    shortDelay=2
    ##focus window
    oomMouseClick(pos=kicadActive)
    oomDelay(shortDelay)    
    
    oomSendAltKey("l")
    delay(shortDelay)
    oomSend("m")
    delay(shortDelay)
    ###Select Available     
    oomSendRight(2)
    delay(120)
    oomSendRight(2)
    delay(shortDelay)
    #library search box
    #oomSendTab(4)
    oomSendTab(3)
    delay(shortDelay)
    #sendlibraryName
    oomSend(libraryName,delay=3)
    oomSendEnter(delay=3)
    #back to library window
    oomMouseClick(pos=kicadLibraryTop)
    oomDelay(shortDelay)    
    oomSendEnter(delay=3)
    ### for large libraries
    oomSendEnter(delay=120)
    oomSendEsc()
    delay(5)


######  KICAD


def makeKicadOompFile(footprint, owner):
    fileName = getKicadFootprintFolder(footprint,owner) + "details.py"
    f = open(fileName,"w")
    hexID=""
    type="FOOTPRINT"
    size="kicad"
    color=owner
    desc=footprint[1].replace(".pretty","")
    index=footprint[0]
    name = owner + "/" + footprint[1].replace(".pretty","") + "/" + footprint[0]
    f.write(OOMP.getFileOpening(hexID,type,size,color,desc,index,name))
    ###### Get details from kicad_mod file
    footprintFileName = getKicadFootprintFolder(footprint,owner) + "footprint.kicad_mod"
    with open(footprintFileName, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            if '(descr "' in line:
                #print("    Adding description")
                f.write(OOMP.getAddTagLine("description",line.replace('(descr "',"").replace('")',"").strip()))
            testLine = '(tags "'
            if testLine in line:           
                #print("    Adding tags")
                f.write(OOMP.getAddTagLine("tags",line.replace(testLine,"").replace('")',"").strip()))            
            if '(attr ' in line:
                #print("    Adding attr")
                f.write(OOMP.getAddTagLine("attribute",line.replace('(attr ',"").replace(')',"").strip())) 
            testLine = '(model "'                 
            if testLine in line:
                #print("    Adding attr")
                f.write(OOMP.getAddTagLine("3dmodel",line.replace(testLine,"").replace('"',"").strip()))    
                
    

    f.write("\n")
    f.write(OOMP.getFileEnding())
    f.close()
    
def makeEagleOompFile(footprint, owner, overwrite=False):
    
    filename = getEagleFootprintFolder(footprint,owner) + "details.py"
    if not os.path.isfile(filename) or overwrite:
        print("OOMP file for " + footprint[0])    
        f = open(filename,"w", encoding="utf-8")
        hexID=""
        type="FOOTPRINT"
        size="eagle"
        color=owner
        desc=footprint[1].replace(".pretty","")
        index=footprint[0]
        name = owner + "/" + footprint[1].replace(".pretty","") + "/" + footprint[0]
        f.write(OOMP.getFileOpening(hexID,type,size,color,desc,index,name))
        ###### Get details from kicad_mod file
        
        footprintFileName = getEagleFootprintFolder(footprint,owner) + "eagleFootprint.xml"
        with open(footprintFileName, "r", encoding="utf-8") as a_file:
            content = a_file.read()
            xmlType = 'description'
            tagType = 'description'
            line = stringBetweenLines(content,"<"+xmlType+">","</"+xmlType+">")
            line = line.replace('"',"&quot;")
            if line != "":           
                f.write(OOMP.getAddTagLine(tagType,line,quotes="triple").encode("ascii", "ignore").decode())            

        variablesLine = ",hexID='" + hexID + "',oompType='" + type + "',oompSize='" + size + "',oompColor='" + color + "',oompDesc='" + desc + "',oompIndex='" + index + "'"
        oompID = type +"-" + size + "-" + color + "-" + desc + "-" + index
        line = '\nnewPart = OOMPtags.addTags(newPart,"' + oompID + '"' + variablesLine + ')\n'

        f.write(line)

        f.write("\n")
        f.write(OOMP.getFileEnding())
        f.close()
    

def copyKicadSourceFile(footprint, owner):
    sourceFile = "sourceFiles/" + owner + "/" + footprint[1] + "/" +footprint[0] + ".kicad_mod"
    destFile = getKicadFootprintFolder(footprint,owner) + "footprint.kicad_mod"
    Path(getKicadFootprintFolder(footprint,owner)).mkdir(parents=True, exist_ok=True)    

    if os.path.isfile(destFile):
        print("    Deleting: " + destFile)
        os.remove(destFile)
    
    shutil.copyfile(sourceFile, destFile)

def copyEagleSourceFile(footprint, owner,libraryFile,overwrite=False):
    destFile = getEagleFootprintFolder(footprint,owner) + "eagleFootprint.xml"
    Path(getEagleFootprintFolder(footprint,owner)).mkdir(parents=True, exist_ok=True)    

    if not os.path.isfile(destFile) or overwrite:
        f = open(libraryFile, encoding='utf-8',mode="r")
        fileContents = f.read()
        f.close()

        start= '<package name="' + footprint[0] 
        end = "</package>"

        print("Start: " + start)

        fp =  start + stringBetweenLines(fileContents,start,end) + end + "\n"

        

        print("Destination: " + destFile)
        f = open(destFile,"w", encoding="utf-8")
        xmlStart = """<?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE eagle SYSTEM "eagle.dtd">
    <eagle version="6.6.0">
    <library>
    <packages>"""
        xmlEnd = """</packages>
        </library>
        </xml>"""
        #f.write(xmlStart)
        f.write(fp)
        #f.write(xmlEnd)
        f.close()



def getKicadFootprintFolder(footprint,owner):
    return"oomlout_OOMP_eda/footprints/kicad/" + owner + "/" +  footprint[1].replace(".pretty","") + "/"  + footprint[0].replace("/","-") + "/"

def getEagleFootprintFolder(footprint,owner):
    return"oomlout_OOMP_eda/footprints/eagle/" + owner + "/" +  footprint[1].replace(".pretty","") + "/"  + footprint[0].replace("/","-").replace(":","-") + "/"

def captureKicadFootprint(footprint, owner, overwrite = False):
    oompDirectory = OOMP.getDir("eda") + "/footprints/kicad/" + owner + "/" +  footprint[1].replace(".pretty","") + "/" 
    oompDirectoryZ = oompDirectory + "zoom/"

    oompFileNameZ1 = oompDirectory + "" + footprint[0].replace("/","-")+ "/zoom/imageZ1.png"
    oompFileNameZ2 = oompDirectory + "" + footprint[0].replace("/","-")+ "/zoom/imageZ2.png"
    oompFileNameZ3 = oompDirectory + "" + footprint[0].replace("/","-")+ "/zoom/imageZ3.png"
    oompFileNameZ4 = oompDirectory + "" + footprint[0].replace("/","-")+ "/zoom/imageZ4.png"
    oompFileNameZ5 = oompDirectory + "" + footprint[0].replace("/","-")+ "/zoom/imageZ5.png"

    oompFileName = oompDirectory + "" + footprint[0].replace("/","-")+ "/image.png"

    screenNames = [oompFileName,oompFileNameZ1,oompFileNameZ2,oompFileNameZ3,oompFileNameZ4,oompFileNameZ5]

    partDirectory = oompDirectory + "" + footprint[0].replace("/","-")
    kicadFileName = "sourceFiles/kicad-footprints/" + footprint[1] + "/" + footprint[0] + ".png"
    oomMakeDir(oompDirectory)   
    oomMakeDir(partDirectory)   
    oomMakeDir(partDirectory + "/zoom/")   
    oomMakeDir(oompDirectoryZ)   

    if overwrite or not os.path.isfile(oompFileName) :
        shortDelay = 1
        longDelay = 3
        footprintName = footprint[0]
        footprintDir = footprint[1].replace(".pretty","")
        print("Capturing :" + str(footprint))
        oomMouseClick(pos=kicadActive)
        oomDelay(shortDelay)
        ##apply filter
        oomMouseClick(pos=kicadFootprintFilter)
        oomDelay(shortDelay)
        oomSendCtrl("a")
        oomDelay(shortDelay)
        oomSend(footprintName + " " + footprintDir)
        oomDelay(longDelay)
        oomMouseDoubleClick(pos=kicadFootprintFirstResult)
        oomDelay(longDelay)
        #### Discard Changes
        oomSendRight()
        oomDelay(shortDelay)
        oomSendEnter()
        oomDelay(longDelay)
        ##zoomback a little
        oomMouseMove(pos=kicadFootprintMiddle)
        oomDelay(shortDelay) 
        oomMouseMove(pos=kicadFootprintMiddlePlus)
        oomDelay(shortDelay)
        oomMakeDir(oompDirectory)
        kicadCut = [420,90,850,850]
        for file in screenNames:
            oomMouseMove(pos=kicadFootprintTopLeft)
            oomDelay(shortDelay)
            oomScreenCapture(file,crop=kicadCut)  
            oomMouseMove(pos=kicadFootprintMiddle)      
            oomSendAltKey("v")
            oomSendDown()
            oomSendDown()
            oomSendDown()
            oomSendEnter()
            oomDelay(shortDelay)    
                        
        oomDelay(longDelay)    

        oomDelay(5)

def captureKicadSymbol(footprint, owner, overwrite = False):
        oompDirectory = "oomlout_OOMP_eda/symbols/kicad/" + owner + "/"  +  footprint[1] + "/" 
        oompFileName = oompDirectory + footprint[0] + ".png"
        if overwrite or not os.path.isfile(oompFileName) :
            shortDelay = 1
            longDelay = 3
            footprintName = footprint[0]
            footprintDir = footprint[1]
            print("Capturing Symbol:" + str(footprint))
            oomMouseClick(pos=kicadActive)
            oomDelay(shortDelay)
            ##apply filter
            oomMouseClick(pos=kicadFootprintFilter)
            oomDelay(shortDelay)
            oomSendCtrl("a")
            oomDelay(shortDelay)
            oomSend(footprintName + " " + footprintDir)
            oomDelay(longDelay)
            oomMouseDoubleClick(pos=kicadFootprintFirstResult)
            oomDelay(longDelay)
            #### Discard Changes
            oomSendRight()
            oomDelay(shortDelay)
            oomSendEnter()
            oomDelay(longDelay)
            ##zoomback a little
            oomMouseMove(pos=kicadSymbolMiddle)
            oomDelay(shortDelay) 
            oomMouseMove(pos=kicadSymbolMiddlePlus)
            oomDelay(shortDelay)   
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)   
            oomMouseScrollWheel(movement=-50)
            oomDelay(longDelay)    
            ###### Saving
            kicadDir = "sourceFiles/kicad-symbols/" + footprint[1] + "/"
            kicadFileName = kicadDir + footprint[0] + ".png"
            #oompDirectory = "eda/footprint/kicad/" +  footprint[1].replace(".pretty","") + "/" 
            #oompFileName = oompDirectory + footprint[0] + ".png"
            oomMakeDir(oompDirectory)
            oomMakeDir(kicadDir)
            oomScreenCapture(kicadFileName,crop=[560,105,900,900])
            oomScreenCapture(oompFileName,crop=[560,105,900,900])
            oomDelay(5)

## needs grid set to finest
## Add locally (if doing a default one then need to switch name tab to 9 from 8)
def captureEagleFootprint(footprint, owner, overwrite=False,libraryName=""):
    if True: 
        oompDirectory = "oomlout_OOMP_eda/footprints/eagle/" + owner + "/"  +  footprint[1] + "/" 
        oompFileNameZ1 = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";") + "/zoom/imageZ1.png"
        oompFileNameZ2 = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";") + "/zoom/imageZ2.png"
        oompFileNameZ3 = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";") + "/zoom/imageZ3.png"
        oompFileNameZ4 = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";") + "/zoom/imageZ4.png"

        oompFileName = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";") + "/image.png"


        partDirectory = oompDirectory + "" + footprint[0].replace("/","-").replace(":",";")

        oomMakeDir(oompDirectory)   
        oomMakeDir(partDirectory)   
        oomMakeDir(partDirectory + "/zoom/")   


        if overwrite or not os.path.isfile(oompFileName) :
            print("making :" + str(footprint))
            global currentLibrary
            if currentLibrary != libraryName:
                eagleResetLibrary()
                eagleSetLibrary(libraryName)
                currentLibrary = libraryName
        
            shortDelay = 1
            longDelay = 3
            footprintName = footprint[0]
            footprintDir = footprint[1]
            print("Capturing Symbol:" + str(footprint))
            ##focus window
            oomMouseClick(pos=kicadActive)
            oomDelay(shortDelay)
            ## add component window
            oomSendControlShiftKey("a")
            oomDelay(shortDelay)
            oomMouseClick(pos=eagleFootprintFilter)
            oomDelay(shortDelay)
            oomSendControl("a")
            oomDelay(shortDelay)
            oomSend(footprintName)
            oomDelay(shortDelay)
            oomSend("     ")
            oomDelay(shortDelay)
            oomSendEnter()
            oomDelay(longDelay)
            oomDelay(longDelay)
            oomDelay(longDelay)
            ######  Issue when more than one component in search so click is required
            oomMouseClick(pos=eagleFootprintFirstResult)
            oomDelay(shortDelay)
            oomSendShiftTab(3)
            oomDelay(shortDelay)
            oomSendEnter()
            oomDelay(longDelay)
            
            #oomMouseMove(pos=eagleFootprintAddOk)
            #oomDelay(shortDelay)
            #oomMouseClick()
            #oomDelay(shortDelay)
            ## Click component down
            oomMouseMove(pos=eagleFootprintMiddle)
            oomDelay(shortDelay)
            oomMouseMove(pos=eagleFootprintMiddlePlus)
            oomDelay(shortDelay)        
            oomMouseClick(pos=eagleFootprintMiddle)
            oomDelay(shortDelay)
            oomSendEsc()
            oomDelay(shortDelay)
            oomSendEsc()
            oomDelay(shortDelay)
            ## Set name and value
            oomMouseMove(pos=eagleFootprintMiddlePlus)
            oomDelay(shortDelay)
            oomMouseMove(pos=eagleFootprintMiddle)
            oomDelay(shortDelay)
            oomMouseRight()
            oomDelay(shortDelay)
            oomSendUp()
            oomDelay(shortDelay)
            oomSendEnter()
            oomDelay(shortDelay)
            oomSendTab(3)
            oomDelay(shortDelay)
            oomSend("NAME")
            oomDelay(shortDelay)
            oomSendTab(8)
            #oomSendTab(9)
            oomDelay(shortDelay)
            oomSend("VALUE")
            oomDelay(shortDelay)
            oomSendEnter()
            oomDelay(shortDelay)
            ## Set Zoom

            oomSendAltKey("f2")
            oomDelay(shortDelay)
            oomSendAltKey("f2")
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ1,crop=eagleCrop)
            oomSend("{F4}")
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ2,crop=eagleCrop)        
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileName,crop=eagleCrop)
            oomSend("{F4}")
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ3,crop=eagleCrop)        
            oomSend("{F4}")
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ4,crop=eagleCrop)        
            oomDelay(shortDelay)
            ## Delete everything
            oomSendControl("a")
            oomDelay(shortDelay)    
            oomSendDelete()
            oomDelay(shortDelay)
            oomSend("{F4}")

            
            oomDelay(longDelay)




           

def getKicadFootprintNames(owner):
    directory = "C:/GH/oomlout_OOMP/sourceFiles/" + owner + "/"
    footprints = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if("kicad_mod" in file):
                #print(file)
                fileName = file.replace(".kicad_mod","")
                footprints.append([fileName,subdir.replace(directory,"")])
    return footprints
    

def getKicadSymbolNames(owner):
    directory = "C:/GH/oomlout_OOMP/sourceFiles/" + owner + "/"
    symbols = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if("kicad_sym" in file and not "RF" in file):
                #print("Working on File: "  + file)
                filename = subdir +"/" + file
                #print(filename)
                f = open(filename, "r")
                fileContents = f.read()
                lines = fileContents.splitlines()
                for line in lines:
                    if "(symbol" in line and runKicadSymbol(line):
                        #print("line: " + line)
                        symbol = stringBetween(line,'"','"')
                        #print(symbol)
                        symbols.append([symbol,file.replace(".kicad_sym","")])

                    #fileName = file.replace(".kicad_mod","")
                    #footprints.append([fileName,subdir.replace(directory,"")])
    return symbols

def runKicadSymbol(line):
    returnValue = True
    for x in range(9):
        for y in range(9):
            testString = "_" + str(x) + "_" + str(y)
            if testString in line:
                returnValue = False
    return returnValue

def getEagleFootprintNames(libraryFile,libraryName):
    footprints = []
    f = open(libraryFile, encoding='utf-8',mode="r")
    fileContents = f.read()
    lines = fileContents.splitlines()
    for line in lines:
        if "<package name=" in line:
            footprint = stringBetween(line,'<package name="','"').replace('"',"")
            footprints.append([footprint,libraryName])
    return footprints



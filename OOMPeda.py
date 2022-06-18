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
kicadSymbolMiddle = [1105,555] 
kicadSymbolMiddlePlus = [1110,560] 

eagleFootprintFilter = [200,680]
eagleFootprintFirstResult = [130,90]
eagleFootprintAddOk = [828,720]
eagleFootprintMiddle = [970,600]
eagleFootprintMiddlePlus = [eagleFootprintMiddle[0]+5,eagleFootprintMiddle[1]+5] 
#eagleCrop = [820,180,800,800]
eagleCrop = [555,200,800,800]


###### need to remove to avoid name coNAMEnflicts
def harvestEagleLibraries():
    ######  Adafruit
    owner = "Adafruit-Eagle-Library"
    libraryName="adafruit"     
    library="C:/GH/oomlout_OOMP/sourceFiles/" + owner + "/"  + libraryName +".lbr"       
    harvestEagleFootprint(library,libraryName, owner)    
    
    ######  Defaults
        ######  Pinhead
    owner = "eagle-default"
    libraryName="pinhead"     
    library="C:/EAGLE 9.6.2/cache/lbr/" + libraryName +".lbr"    
    #harvestEagleFootprint(library,libraryName, owner)

    ######  Sparkfun
    owner = "SparkFun-Eagle-Libraries"
    libraryName="Sparkfun-Connectors"     
    library="C:/GH/oomlout_OOMP/sourceFiles/SparkFun-Eagle-Libraries/" + libraryName +".lbr"    
    #harvestEagleFootprint(library,libraryName,owner)
    

def harvestKicadLibraries():    
    owner = "kicad-footprints"
    #harvestKicadFootprintImages(owner)
    harvestKicadFootprintFiles(owner)



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
def harvestEagleFootprint(libraryFile,libraryName, owner):
    filterDir = "Connector_PinHeader_2.54mm"
    footprints = getEagleFootprintNames(libraryFile,libraryName)
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")
    for footprint in footprints:
        captureEagleFootprint(footprint,owner)



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
                f.write(OOMP.getAddTagLine("kicadDesc",line.replace('(descr "',"").replace('")',"").strip()))
            testLine = '(tags "'
            if testLine in line:           
                #print("    Adding tags")
                f.write(OOMP.getAddTagLine("kicadTags",line.replace(testLine,"").replace('")',"").strip()))            
            if '(attr ' in line:
                #print("    Adding attr")
                f.write(OOMP.getAddTagLine("kicadAttr",line.replace('(attr ',"").replace(')',"").strip())) 
            testLine = '(model "'                 
            if testLine in line:
                #print("    Adding attr")
                f.write(OOMP.getAddTagLine("kicad3DModel",line.replace(testLine,"").replace('"',"").strip()))    
                
    

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



def getKicadFootprintFolder(footprint,owner):
    return"oomlout_OOMP_eda/footprints/kicad/" + owner + "/" +  footprint[1].replace(".pretty","") + "/"  + footprint[0].replace("/","-") .replace(".","_")+ "/"

def captureKicadFootprint(footprint, owner, overwrite = False):
    oompDirectory = "oomlout_OOMP_eda/footprints/kicad/" + owner + "/" +  footprint[1].replace(".pretty","") + "/" 
    oompFileNameOld = oompDirectory + footprint[0] + ".png"    
    oompDirectoryZ = oompDirectory + "zoom/"
    oompFileNameZ1Old = oompDirectoryZ +footprint[0].replace("/","-") .replace(".","_")+ "z1.png"
    oompFileNameZ2Old = oompDirectoryZ +footprint[0].replace("/","-") .replace(".","_")+ "z2.png"
    oompFileNameZ3Old = oompDirectoryZ +footprint[0].replace("/","-") .replace(".","_")+ "z3.png"
    oompFileNameZ4Old = oompDirectoryZ +footprint[0].replace("/","-") .replace(".","_")+ "z4.png"
    oompFileNameZ5Old = oompDirectoryZ +footprint[0].replace("/","-") .replace(".","_")+ "z5.png"

    oompFileNameZ1 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ1.png"
    oompFileNameZ2 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ2.png"
    oompFileNameZ3 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ3.png"
    oompFileNameZ4 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ4.png"
    oompFileNameZ5 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ5.png"
    oompFileNameZ6 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ6.png"
    oompFileNameZ7 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ7.png"
    oompFileNameZ8 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ8.png"
    oompFileNameZ9 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ9.png"
    oompFileNameZ10 = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/zoom/imageZ10.png"

    oompFileName = oompDirectory + "" + footprint[0].replace("/","-") .replace(".","_")+ "/image.png"


    partDirectory = oompDirectory + "" + footprint[0].replace("/","-")
    kicadFileName = "sourceFiles/kicad-footprints/" + footprint[1] + "/" + footprint[0] + ".png"
    oomMakeDir(oompDirectory)   
    oomMakeDir(partDirectory)   
    oomMakeDir(partDirectory + "/zoom/")   
    oomMakeDir(oompDirectoryZ)   

    if os.path.isfile(oompFileNameOld):
        filesOld = [oompFileNameOld,oompFileNameZ1Old,oompFileNameZ2Old,oompFileNameZ3Old,oompFileNameZ4Old,oompFileNameZ5Old]
        filesNew = [oompFileName,oompFileNameZ1,oompFileNameZ2,oompFileNameZ3,oompFileNameZ4,oompFileNameZ5]
        index=0
        for file in filesOld:
            if os.path.isfile(filesOld[index]):
                os.rename(filesOld[index],filesNew[index])
                print("Moving: " + str(filesOld[index]) + " to " + str(filesNew[index]))
            index = index + 1  
        oomDelay(0)  
    else:
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

            kicadCut = [675,105,900,900]

            oomScreenCapture(oompFileNameZ1,crop=kicadCut)        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ2,crop=kicadCut)                    
            oomScreenCapture(oompFileName,crop=kicadCut) 
            oomScreenCapture(kicadFileName,crop=kicadCut)           
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ3,crop=kicadCut)            
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ4,crop=kicadCut)        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ5,crop=kicadCut)        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ6,crop=kicadCut)        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ7,crop=kicadCut)        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ8,crop=kicadCut)  
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ9,crop=kicadCut)  
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ10,crop=kicadCut)        

            
            oomDelay(longDelay)    
            ###### Saving
            
            #oompDirectory = "eda/footprint/kicad/" +  footprint[1].replace(".pretty","") + "/" 
            #oompFileName = oompDirectory + footprint[0] + ".png"
            oomMakeDir(oompDirectory)
            
            #oomScreenCapture(oompFileName,crop=[560,105,900,900])
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
def captureEagleFootprint(footprint, owner, overwrite=False):
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
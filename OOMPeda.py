from oomBase import *
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
eagleFootprintMiddle = [1220,600]
eagleFootprintMiddlePlus = [1210,590] 

###### need to remove to avoid name conflicts
def harvestEagleLibraries():
    ######  Defaults
        ######  Pinhead
    owner = "eagle-default"
    libraryName="pinhead"     
    library="C:/EAGLE 9.6.2/cache/lbr/" + libraryName +".lbr"    
    #harvestEagleFootprint(library,libraryName, owner)

    ######  Sparkfun
    owner = "SparkFun-Eagle-Libraries"
    libraryName="Sparkfun-Connectors"     
    library="C:/GH/oomlout-OOMP/sourceFiles/SparkFun-Eagle-Libraries/" + libraryName +".lbr"    
    harvestEagleFootprint(library,libraryName,owner)
    

### open footprint editor
def harvestKicadFootprintImages():
    owner = "kicad-footprints"
    filterDir = "LED"
    footprints = getKicadFootprintNames()
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")
    for footprint in footprints:
        if filterDir in footprint[1]:
            captureKicadFootprint(footprint,owner)
#open symbol editor
def harvestKicadSymbolImages():
    owner = "kicad-Sympols"
    filterDir = ""
    symbols = getKicadSymbolNames()
    numSymbols = len(symbols)
    print("Found " + str(numSymbols) + " symbols")
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


def captureKicadFootprint(footprint, owner, overwrite = False):
    oompDirectory = "oomlout_OOMP_eda/footprints/kicad/" + owner + "/" +  footprint[1].replace(".pretty","") + "/" 
    oompFileNameOld = oompDirectory + footprint[0] + ".png"    
    oompDirectoryZ = oompDirectory + "zoom/"
    oompFileNameZ1Old = oompDirectoryZ +footprint[0].replace("/","-") + "z1.png"
    oompFileNameZ2Old = oompDirectoryZ +footprint[0].replace("/","-") + "z2.png"
    oompFileNameZ3Old = oompDirectoryZ +footprint[0].replace("/","-") + "z3.png"
    oompFileNameZ4Old = oompDirectoryZ +footprint[0].replace("/","-") + "z4.png"
    oompFileNameZ5Old = oompDirectoryZ +footprint[0].replace("/","-") + "z5.png"

    oompFileNameZ1 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ1.png"
    oompFileNameZ2 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ2.png"
    oompFileNameZ3 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ3.png"
    oompFileNameZ4 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ4.png"
    oompFileNameZ5 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ5.png"
    oompFileNameZ6 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ6.png"
    oompFileNameZ7 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ7.png"
    oompFileNameZ8 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ8.png"
    oompFileNameZ9 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ9.png"
    oompFileNameZ10 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ10.png"

    oompFileName = oompDirectory + "" + footprint[0].replace("/","-") + "/image.png"


    partDirectory = oompDirectory + "" + footprint[0].replace("/","-")

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

            oomScreenCapture(oompFileNameZ1,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ2,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ3,crop=[560,105,900,900])            
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ4,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomMakeDir(oompDirectory)
            oomScreenCapture(oompFileNameZ5,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ6,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ7,crop=[560,105,900,900])        
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ8,crop=[560,105,900,900])  
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ9,crop=[560,105,900,900])  
            oomMouseScrollWheel(movement=-50)
            oomDelay(shortDelay)    
            oomScreenCapture(oompFileNameZ10,crop=[560,105,900,900])        

            
            oomDelay(longDelay)    
            ###### Saving
            kicadFileName = "sourceFiles/kicad-footprints/" + footprint[1] + "/" + footprint[0] + ".png"
            #oompDirectory = "eda/footprint/kicad/" +  footprint[1].replace(".pretty","") + "/" 
            #oompFileName = oompDirectory + footprint[0] + ".png"
            oomMakeDir(oompDirectory)
            oomScreenCapture(kicadFileName,crop=[560,105,900,900])
            oomScreenCapture(oompFileName,crop=[560,105,900,900])
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
def captureEagleFootprint(footprint, owner, overwrite=False):
    oompDirectory = "oomlout_OOMP_eda/footprints/eagle/" + owner + "/"  +  footprint[1] + "/" 
    oompFileNameZ1 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ1.png"
    oompFileNameZ2 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ2.png"
    oompFileNameZ3 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ3.png"
    oompFileNameZ4 = oompDirectory + "" + footprint[0].replace("/","-") + "/zoom/imageZ4.png"

    oompFileName = oompDirectory + "" + footprint[0].replace("/","-") + "/image.png"


    partDirectory = oompDirectory + "" + footprint[0].replace("/","-")

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
        oomSendTab(9)
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
        oomScreenCapture(oompFileNameZ1,crop=[820,180,800,800])
        oomSend("{F4}")
        oomDelay(shortDelay)
        oomMakeDir(oompDirectory)
        oomScreenCapture(oompFileNameZ2,crop=[820,180,800,800])        
        oomMakeDir(oompDirectory)
        oomScreenCapture(oompFileName,crop=[820,180,800,800])
        oomSend("{F4}")
        oomDelay(shortDelay)
        oomMakeDir(oompDirectory)
        oomScreenCapture(oompFileNameZ3,crop=[820,180,800,800])        
        oomSend("{F4}")
        oomDelay(shortDelay)
        oomMakeDir(oompDirectory)
        oomScreenCapture(oompFileNameZ4,crop=[820,180,800,800])        
        oomDelay(shortDelay)
        ## Delete everything
        oomSendControl("a")
        oomDelay(shortDelay)    
        oomSendDelete()
        oomDelay(longDelay)




           

def getKicadFootprintNames():
    directory = "C:/GH/oomlout-OOMP/sourceFiles/kicad-footprints/"
    footprints = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if("kicad_mod" in file):
                #print(file)
                fileName = file.replace(".kicad_mod","")
                footprints.append([fileName,subdir.replace(directory,"")])
    return footprints
    

def getKicadSymbolNames():
    directory = "C:/GH/oomlout-OOMP/sourceFiles/kicad-symbols/"
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
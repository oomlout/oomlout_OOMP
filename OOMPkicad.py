from oomBase import *
import os

###### kicad mousepoints
X = 0
Y = 0
kicadActive =[515,14]
kicadFootprintFilter =[145,114]
kicadFootprintFirstResult = [145,185]
kicadFootprintMiddle = [945,545] 
kicadFootprintMiddlePlus = [950,550] 

def harvestFootprintImages():
    filterDir = "Connector_PinHeader_2.54mm"
    footprints = getFootprintNames()
    numFootprints = len(footprints)
    print("Found " + str(numFootprints) + " footprints")
    for footprint in footprints:
        if filterDir in footprint[1]:
            captureFootprint(footprint)

    
def captureFootprint(footprint, overwrite = False):
    oompDirectory = "eda/footprint/kicad/" +  footprint[1].replace(".pretty","") + "/" 
    oompFileName = oompDirectory + footprint[0] + ".png"
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
        oomMouseScrollWheel(movement=-50)
        oomDelay(shortDelay)    
        oomMouseScrollWheel(movement=-50)
        oomDelay(shortDelay)    
        oomMouseScrollWheel(movement=-50)
        oomDelay(shortDelay)    
        oomMouseScrollWheel(movement=-50)
        oomDelay(shortDelay)    
        oomMouseScrollWheel(movement=-50)
        oomDelay(longDelay)    
        ###### Saving
        kicadFileName = "sourceFiles/kicad-footprints/" + footprint[1] + "/" + footprint[0] + ".png"
        #oompDirectory = "eda/footprint/kicad/" +  footprint[1].replace(".pretty","") + "/" 
        #oompFileName = oompDirectory + footprint[0] + ".png"
        oomMakeDir(oompDirectory)
        oomScreenCapture(kicadFileName,crop=[560,105,900,900])
        oomScreenCapture(oompFileName,crop=[560,105,900,900])
        oomDelay(5)


def getFootprintNames():
    directory = "C:/Program Files/KiCad/6.0/share/kicad/footprints/"
    footprints = []
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if("kicad_mod" in file):
                #print(file)
                fileName = file.replace(".kicad_mod","")
                footprints.append([fileName,subdir.replace(directory,"")])
    return footprints
    

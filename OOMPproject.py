from oomBase import *
from OOMPeda import *
import OOMP
import os
import shutil

##################
######  Adafruit Section

def harvestProjectsAdafruit():
    srcDir = "oomlout_OOMP_projects\sourceFiles/adafruit/"
    print("Harvesting Adafruit!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirAdafruit(srcDir + dir + "/")
            

def processProjectDirAdafruit(directory):
    hardwareDir = directory 
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0
    ############ Finding Files
    ###### Test if it has a hardware path
    if os.path.isdir(hardwareDir):
        files = [f for f in os.listdir(directory)]
        #print(files)
        for file in files:
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("-"," ").replace("/","").replace("\\","")
            if file.lower() == "license.txt":
                #print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                #print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,'href="http://www.adafruit.com/products/','">')
                if not index.isnumeric():                    
                    ###### for debugging skipped repositories
                    c=0    
                
                #print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            #print(file)
            if ".brd" in file.lower():                
                #print("        Found Board")
                boardFile = hardwareDir+file
            if ".sch" in file.lower():
                #print("        Found Schematic")
                schematicFile = hardwareDir+file

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "ADAF"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRA" + index   
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/adafruit/" + name.replace(" ","-") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","http://www.adafruit.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
    #delay(1)
                            
                                
##################
######  Arduino Section
def harvestProjectsArduino():

    arduinoProjects = []

    oompID = ""
    eagleFiles = ""
    drawing = ""
    datasheet =""
    ###uno
    oompID = "PROJ-ARDU-UNO-REV3-01"
    eagleFiles = "https://content.arduino.cc/assets/UNO-TH_Rev3e-reference.zip"
    drawing = "http://arduino.cc/documents/ArduinoUno.dxf"
    datasheet ="https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf"
    source = "https://store.arduino.cc/collections/boards/products/arduino-uno-rev3"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])
    ###uno smd
    oompID = "PROJ-ARDU-UNO-REV3-SM"
    eagleFiles = "https://content.arduino.cc/assets/UNOSMD_V3.zip"
    drawing = "http://arduino.cc/documents/ArduinoUno.dxf"
    datasheet ="https://docs.arduino.cc/resources/datasheets/A000066-datasheet.pdf"
    source = "https://store.arduino.cc/collections/boards/products/arduino-uno-rev3-smd"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])
    ###leo
    oompID = "PROJ-ARDU-LEO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Leonardo-reference.zip"
    drawing = ""
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-leonardo-with-headers"
    #arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source])

    ###due
    oompID = "PROJ-ARDU-DUE-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/ArduinoDUE_v02g.zip"
    drawing = "https://content.arduino.cc/assets/Arduino_Due_Technical_Drawing.pdf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-due"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Due%20%28Rev2b%29.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])
    ###mega
    oompID = "PROJ-ARDU-MEGA-2560-01"
    eagleFiles = "https://content.arduino.cc/assets/MEGA2560_Rev3e-reference.zip"
    drawing = "http://arduino.cc/documents/dimensioniMega.dxf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-mega-2560-rev3"
    fritzing = ""
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])

    ###nano
    oompID = "PROJ-ARDU-NANO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Nano-reference.zip"
    drawing = "https://content.arduino.cc/assets/arduino_nano_size.pdf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-nano"
    fritzing = ""
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])

    ###micro ((files not in right location need to be moved brd and sch))
    oompID = "PROJ-ARDU-MICRO-STAN-01"
    eagleFiles = "https://content.arduino.cc/assets/Micro-reference-Eagle.zip"
    drawing = "http://arduino.cc/documents/dimensioniMicro.dxf"
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-micro"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Micro%20%28Rev3%29.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])
    ###nano0 every
    oompID = "PROJ-ARDU-NANO-EVERY-01"
    eagleFiles = "https://content.arduino.cc/assets/NanoEveryV30.zip"
    drawing = ""
    datasheet =""
    source = "https://store.arduino.cc/collections/boards/products/arduino-nano-every-with-headers"
    fritzing = "https://content.arduino.cc/assets/Arduino%20Nano%20Every.fzpz"
    arduinoProjects.append([oompID,eagleFiles,drawing,datasheet,source,fritzing])


    for projectDetails in arduinoProjects:
        downloadArduinoProject(projectDetails)

def downloadArduinoProject(projectDetails):
    oompID = projectDetails[0]
    eagleFiles = projectDetails[1]
    drawing = projectDetails[2]
    datasheet = projectDetails[3]
    source = projectDetails[4]
    if len(projectDetails) > 5:
        fritzing = projectDetails[5]
    directory = "oomlout_OOMP_projects/" + oompID + "/"
    oomMakeDir(directory)
    tempDir = "oomlout_OOMP_projects/sourceFiles/tempT/"
    oomMakeDir(tempDir)
    ######  unzip board files
    url = eagleFiles
    saveFile = tempDir + "board.zip"
    oomSaveUrl(url,saveFile)
    filename = saveFile
    dirName = tempDir
    oomUnzip(filename,dirName,deleteZip=True)
    boardFile = ""
    schematicFile = ""
    files = [f for f in os.listdir(tempDir)]   
    for file in files:
        print(file)
        if ".brd" in file.lower():                
            print("        Found Board")
            boardFile = tempDir+file
        if ".sch" in file.lower():
            print("        Found Schematic")
            schematicFile = tempDir+file
    ###### datasheet
    if datasheet != "":
        url = datasheet
        saveFile = directory + "datasheet.pdf"
        oomSaveUrl(url,saveFile)
    ###### drawing        
    if drawing != "":
        url = drawing
        saveFile = ""
        if ".dxf" in url:
            saveFile = directory + "diagram.dxf"
        else:
            saveFile = directory + "diagram.pdf"    
        oomSaveUrl(url,saveFile)
    ###### fritzing        
    if fritzing != "":
        url = fritzing
        saveFile = directory + "fritzing.fzpz"
        oomSaveUrl(url,saveFile)
    ######  copy files        
    if boardFile != "":
        oomCopyFile(boardFile, directory + "boardEagle.brd")
    if schematicFile != "":            
        oomCopyFile(schematicFile, directory + "schematicEagle.sch")

    ############ Making OOMP file
    oomp = oompID.split("-")
    oompType = oomp[0]
    oompSize = oomp[1]
    oompColor = oomp[2]
    oompDesc = oomp[3]
    oompIndex = oomp[4] 
    hexID = "PRAR" + oompDesc   
    directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
    oomMakeDir(directory)  

    fileName = directory + "details.py"
    f = open(fileName,"w")
    f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex))
    ###### extra details
    f.write(OOMP.getAddTagLine("sources","All source files from " + source))
    f.write(OOMP.getAddTagLine("linkBuyPage",source))

    f.write("\n")
    f.write(OOMP.getFileEnding())
    f.close()



    oomDeleteDirectory(tempDir, safety=False)        


##################
######  Sparkfun Section

def harvestProjectsSparkfun():
    srcDir = "oomlout_OOMP_projects\sourceFiles/sparkfun/"
    print("Harvesting Sparkfun!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirSparkfun(srcDir + dir + "/")
            

def processProjectDirSparkfun(directory):
    hardwareDir = directory + "Hardware/"
    hardwareDir2 = directory + "Hardware/Qwiic Micro/"
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0
    ############ Finding Files
    ###### Test if it has a hardware path
    if os.path.isdir(hardwareDir):
        files = [f for f in os.listdir(directory)]
        #print(files)
        for file in files:
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("_"," ").replace("/","").replace("\\","")
            if file.lower() == "license.md":
                print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,"https://www.sparkfun.com/products/",")")
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    ###### for debugging skipped repositories
                    c=0    
                
                print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            print(file)
            if ".brd" in file.lower():                
                print("        Found Board")
                boardFile = hardwareDir+file
            if ".sch" in file.lower():
                print("        Found Schematic")
                schematicFile = hardwareDir+file
        ###### test for qwiic nested files   
        if index == "20170":
            c=0
        if os.path.isdir(hardwareDir2) and boardFile == "":
            files = [f for f in os.listdir(hardwareDir2)]   
            for file in files:
                print(file)
                if ".brd" in file.lower():                
                    print("        Found Board")
                    boardFile = hardwareDir2+file
                if ".sch" in file.lower():
                    print("        Found Schematic")
                    schematicFile = hardwareDir2+file                   

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "SPAR"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRS" + index   
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/sparkfun/" + name.replace(" ","_") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","https://www.sparkfun.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
            #delay(1)
                            
    ##################
    ######  Projects Harvesting Stuff

def harvestProjectFiles():
    directory = "oomlout_OOMP_Projects/"
    files = os.listdir(directory)
    for file in files:
        if os.path.isdir(directory + file):
            harvestProject(directory + file)

def harvestProject(directory,overwrite=False):
    baseDir = "oomlout_OOMP_Projects/"                
    oompID = directory.replace(baseDir,"")
    files = os.listdir(directory)
    for file in files:
        if file.lower() == "boardeagle.brd":
            #harvestKicadBoardFile(directory + "/" + file,directory + "/",overwrite=overwrite)
            harvestEagleBoardToKicad(directory + "/" + file,directory + "/",overwrite=overwrite)
            #harvestEagleBoardFile(directory + "/" + file,directory + "/",overwrite=overwrite)

def harvestEagleBoardToKicad(file,directory,overwrite=False):
    ######  open kicad launch window and place in topleft corner 
    # need a blank project loaded 
    dirKicad =   OOMP.baseDir + directory + "kicad/"
    oomMakeDir(dirKicad)
    boardKicad = dirKicad + "boardKicad.kicad_pcb"
    if overwrite or not os.path.exists(boardKicad):
        oomMouseClick(pos=kicadActive,delay=5)       
        oomMouseClick(pos=kicadFile,delay=5)       
        #oomSendAltTab(1,delay=3)
        #oomSendAltTab(1,delay=3)


        #oomMouseMove(pos=kicadFootprintMiddle,delay=2)         
        #oomMouseClick(pos=kicadActive,delay=2)       
        #oomMouseMove(pos=kicadFootprintMiddle,delay=2)         
        #oomSendAltKey("v",10)
        #oomSendLeft(1,delay=2)
        oomSendDown(8,delay=2)
        oomSendRight(1,delay=2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=2)
        ###### filedialog box o-pen
        filename = (OOMP.baseDir + file).replace("/","\\")
        oomSend(filename,5)
        oomSendEnter(10)
        ######  set temp folder
        tempDir = OOMP.baseDir + "oomlout_OOMP_projects/sourceFiles/tempR/"
        
        oomDeleteDirectory(tempDir + "boardEagle.pretty/", safety=False)
        oomDeleteDirectory(tempDir + "boardEagle-backups/", safety=False)        
        oomDeleteDirectory(tempDir, safety=False)
        oomMakeDir(tempDir)
        oomSend(tempDir.replace("/","\\"),2)
        oomSendEnter(2)
        oomSendEnter(10)
        ######  match layers dialog
        oomSendTab(6,5)
        oomSendEnter(2)
        oomSendTab(1,2)
        oomSendEnter(10)
        oomMouseMove(pos=kicadFootprintMiddle,delay=2)
        ######  save board
        oomSendAltKey("f",2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=5)
        oomSend(boardKicad.replace("/","\\"),2)
        oomSendEnter(delay=10)
        oomSendEnter(delay=2)
        ###### close project
        kicadClosePcb(False)

def kicadClosePcb(noSave=True):
    oomSendAltKey("f",2)
    oomSendUp(delay=2)
    oomSendEnter(delay=2)
    if noSave:
        oomSendRight(delay=2)
    oomSendEnter(delay=20)


def harvestKicadBoardFile(file,directory,overwrite=False):
    dirKicad =   OOMP.baseDir + directory + "kicad/"
    boardKicad = dirKicad + "boardKicad.kicad_pcb"
    if os.path.isfile(boardKicad) and (overwrite or True):
        if overwrite or not os.path.isfile(directory + "kicadPcb3d.png"):
            oomLaunchPopen("pcbnew.exe " + boardKicad,10)
            oomMouseClick(pos=kicadActive,delay=5)    
            filename = OOMP.baseDir + directory + "kicad/"
            kicadExport(filename,"bom",overwrite=overwrite)
            kicadExport(filename,"pos",overwrite=overwrite)
            kicadExport(filename,"svg",overwrite=overwrite)
            kicadExport(filename,"wrl",overwrite=overwrite)
            kicadExport(filename,"step",overwrite=overwrite)
            filename = OOMP.baseDir + directory
            kicadExport(filename,"3dRender",overwrite=overwrite)
        

            kicadClosePcb()

def harvestEagleBoardFile(file,directory,overwrite=False):
    dxfFile = OOMP.baseDir + directory + "eagleImage.dxf"
    if overwrite or not os.path.exists(dxfFile):
        oomMouseClick(pos=kicadActive,delay=5)            
        oomSendControl("o",delay=5)
        fullFile = OOMP.baseDir + file
        oomSend(fullFile.replace("/","\\"),delay=3)
        oomSendEnter(2)
        oomSend("n",10)
        #maybe close warning window
        oomMouseClick(pos=eagleCloseText,delay=5)            
        

        ###### Part List
        filename = OOMP.baseDir + directory + "eagleParts.txt"
        eagleExport(filename,1,overwrite=overwrite)
        ###### Net List
        filename = OOMP.baseDir + directory + "eagleNetlist.txt"
        eagleExport(filename,0,overwrite=overwrite)
        ###### Pin List
        filename = OOMP.baseDir + directory + "eaglePinlist.txt"
        eagleExport(filename,2,overwrite=overwrite)
        ###### image
        ###### set export to 1200
        filename = OOMP.baseDir + directory + "eagleImage.png"
        eagleExport(filename,3,overwrite=overwrite)
        ######  CAM files
        testFile = directory + "eagleGerber/CAMOutputs/GerberFiles/copper_bottom.gbr"
        if overwrite or not os.path.exists(testFile):
            camDir = OOMP.baseDir + directory + "eagleGerber/"
            oomMakeDir(camDir)
            oomSendAltKey("f",2)
            oomSend("m",2)
            oomSendTab(16)
            oomDelay(2)
            oomSendEnter(2)
            oomSend(camDir.replace("/","\\"),2)
            oomSendEnter(2)
            oomSendEnter(2)
            oomSend("y",2)
            oomSendEnter(2)
            oomSendEsc()
            oomDelay(2)

        ###### dxf
        filename = dxfFile
        eagleExport(filename,4,overwrite=overwrite)

def kicadExport(filename,type,overwrite=False):
    if type.lower() == "bom":
        bomFile = filename + "boardKicadBom.csv"
        if overwrite or not os.path.isfile(bomFile):
            print("    Making bom file")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("f",2)
            oomSend("b",2)
            oomSend(bomFile.replace("/","\\"),5)
            oomSendEnter(2)
            oomSend("y",2)
    if type.lower() == "pos":
        bomFile = filename + "boardKicad.pos"
        if overwrite or not os.path.isfile(bomFile):
            print("    Making bom file")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("f",2)
            oomSend("c",2)
            oomSend(filename.replace("/","\\"),5)
            oomSendShiftTab(2)
            oomSendEnter(2)   
            oomSendEsc(2)         
    if type.lower() == "svg":
        if overwrite or not os.path.isfile(filename + "boardKicad-B_Cu.svg"):
            print("    Making svg files")
            #oomSendAltKey("f",2)
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("ss",2)
            oomSendEnter(delay=2)
            oomSend(filename,5)
            oomSendShiftTab(2,delay=2)
            oomSendEnter(delay=10)
            oomSendEsc(5)
    if type.lower() == "wrl":
        if overwrite or not os.path.isfile(filename + "boardKicad.wrl"):
            print("    Making wrl file")
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("v",5)
            oomSendShiftTab(2,delay=2)
            oomSendEnter(delay=2)
            oomSend("y",8)
            oomSendEsc(5)
    if type.lower() == "step":
        if overwrite or not os.path.isfile(filename + "boardKicad.step"):
            print("    Making step file")
            oomMouseClick(pos=kicadFile,delay=5)       
            oomSend("e",2)
            oomSend("s",5)
            oomSendEnter(delay=2)
            oomSendShiftTab(4,delay=2)
            oomSendEnter(delay=10)
            oomSendAltKey('f4',5)
            oomSendEsc(5)
    if type.lower() == "3drender":
        if overwrite or not os.path.isfile(filename + "kicadPcb3d.png"):

            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomSendAltKey("3",5)
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=0.5)
            oomSend("z")
            oomSendEnter(delay=1)
            ######  front
            currentFile = filename + "kicadPcb3dFront.png"
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ######  back
            currentFile = filename + "kicadPcb3dBack.png"
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseRight(1)
            oomSend("vv",0.5)
            oomSendEnter(2)

            
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=0.5)
            oomSend("z")
            oomSendEnter(delay=1)
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ######  ortho
            oomMouseMove(pos=kicadFootprintMiddle,delay=2)
            oomMouseRight(1)
            oomSend("v",0.5)
            oomSendEnter(2)
            ###### zoom
            oomMouseClick(pos=kicad3dView,delay=0.5)
            oomSend("z")
            oomSendEnter(delay=1)            
            #yaxis
            times = 3
            for x in range(times):
                oomMouseClick(pos=kicad3dView,delay=0.5)
                oomSend("rr")
                oomSendEnter(delay=1)
            #zaxis    
            times = 2
            for x in range(times):
                oomMouseClick(pos=kicad3dView,delay=0.5)
                oomSend("rrrrrrr")
                oomSendEnter(delay=1)

            currentFile = filename + "kicadPcb3d.png"
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("e",2)
            oomSendEnter(delay=2)
            oomSend(currentFile.replace("/","\\"),2)
            oomSendEnter(delay=2)
            oomSend("y",2)
            ###### close
            oomMouseClick(pos=kicadFile,delay=5) 
            oomSend("c",2)

            


def eagleExport(filename,downs,overwrite=False):
    if overwrite or not os.path.exists(filename):
        oomSendAltKey("f",2)
        oomSend("e",2)
        oomSendDown(downs,2)
        oomSendEnter(5)
        oomSend(filename.replace("/","\\"),2)
        oomSendEnter(5)
        if ".dxf" in filename:
            oomSendRight()
            oomDelay(2)
            oomSendEnter(delay=5)
        oomSend("y",5)






                                
from oomBase import *
from OOMPeda import *
import OOMP
import OOMPprojectHarvest
import OOMPprojectParts
import os
import shutil
import subprocess

    ##################
    ######  Projects Harvesting Stuff

def doTasks(overwrite =False,filter="projects",eagleToKicad=False,kicadProcess=False,eagleProcess=False,interactiveBom=False,partsHarvest=False):
    for project in OOMP.getItems(filter):
        doTask(project,overwrite,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,partsHarvest=partsHarvest)
"""
    overwrite = overwrite
    kicadProcess = False        #kicad launcher open
    eagleToKicad = True        #kicad launcher open
    eagleProcess= False          #eagle pcb open
    interactiveBom = False
"""
def doTask(project,overwrite=False,eagleToKicad=False,kicadProcess=False,eagleProcess=False,interactiveBom=False,partsHarvest=False):
    projectDir = project.getFolder()
    eagleBoardFile = project.getFilename("boardeagle")
    kicadBoardFile = project.getFilename("boardkicad")

    if kicadProcess: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(kicadBoardFile):
            harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite)
    if eagleToKicad: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(eagleBoardFile):
            harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    if eagleProcess: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(eagleBoardFile):
            harvestEagleBoardFile(eagleBoardFile,projectDir,overwrite=overwrite)

    if interactiveBom:
        makeInteractiveHtmlBom(project,overwrite)

    if partsHarvest: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(eagleBoardFile):
            OOMPprojectParts.harvestParts(project,overwrite=overwrite)

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
        tempDir = OOMP.baseDir + "oomlout_OOMP_projects/sourceFiles/tempU/"
        
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
        oomSendEsc(2)
        oomSendEsc(2)
        oomSendEsc(2)
        oomDelay(15)
        oomMouseClick(pos=kicadFootprintMiddle,delay=2)
        ######  save board
        oomSendAltKey("f",2)
        oomSendDown(1,delay=2)
        oomSendEnter(delay=5)
        oomSend(boardKicad.replace("/","\\").replace("\\\\","\\"),2)
        oomSendEnter(delay=10)
        oomSend("y",2)
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




#### 285 seconds per (12 an hour) (1000 in 80 hours) (33 days for 10000)
def harvestKicadBoardFile(file="",directory="",part="",overwrite=False):
    boardKicad = ""
    dirKicad = ""
    if part != "":
        boardKicad = part.getFilename("boardKicad")
        dirKicad = part.getFilename("dirKicad")
        directory = part.getDir()
    else:
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
    pngFile = OOMP.baseDir + directory + "eagleImage.png"
    partFile = OOMP.baseDir + directory + "eagleParts.txt"
    #if overwrite or not os.path.exists(dxfFile):
    #if overwrite or not os.path.exists(pngFile):
    if overwrite or not os.path.exists(partFile):
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
"""        
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
            oomDelay(15)

        ###### dxf
        filename = dxfFile
        eagleExport(filename,4,overwrite=overwrite)
"""
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

def makeInteractiveHtmlBom(project,overwrite=False):
    kicadPython = "C:/Program Files/KiCad/6.0/bin/python.exe"
    interactiveBom = '"C:/GH/oomlout_OOMP/sourceFiles/InteractiveHtmlBom/InteractiveHtmlBom/generate_interactive_bom.py" --no-browser'
    projectFile = project.getFilename("boardkicad",relative = "full")
    bomFile = project.getFilename("bomInteractive",relative="full")
    if os.path.isfile(projectFile): 
        if overwrite or not os.path.isfile(bomFile):
            launchString = '"' + kicadPython + '" ' + interactiveBom + ' "' + projectFile + '"'
            launchString = launchString.replace("/","\\")
            print("Generating Interactive BOM: " + projectFile)
            process = subprocess.Popen(launchString, shell=True, stdout=subprocess.PIPE)
            process.wait()
            print("    Result: " + str(process.returncode))
                                    
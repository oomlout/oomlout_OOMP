from oomBase import *
from OOMPproject import *
from OOMPprojectHarvest import *
from OOMPprojectParts import *
import OOMP

def doTasks(overwrite =False,filter="projects",eagleToKicad=False,kicadProcess=False,eagleProcess=False,interactiveBom=False,partsHarvest=False,matchParts=False):
    for project in OOMP.getItems(filter):
        doTask(project,overwrite,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,partsHarvest=partsHarvest,matchParts=matchParts,filter=filter)
"""
    overwrite = overwrite
    kicadProcess = False        #kicad launcher open
    eagleToKicad = True        #kicad launcher open
    eagleProcess= False          #eagle pcb open
    interactiveBom = False
"""
def doTask(project,overwrite=False,eagleToKicad=False,kicadProcess=False,eagleProcess=False,interactiveBom=False,partsHarvest=False,matchParts=False,filter="projects"):
    projectDir = project.getFolder()
    eagleBoardFile = project.getFilename("boardeagle")
    kicadBoardFile = project.getFilename("boardkicad")

    if kicadProcess: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(kicadBoardFile):
            harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite,filter=filter)
    if eagleToKicad: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(eagleBoardFile):
            harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    if eagleProcess: #open board in kicad and export things like 3d render and bom
        if os.path.isfile(eagleBoardFile):
            harvestEagleBoardFile(eagleBoardFile,projectDir,overwrite=overwrite)
            harvestEagleSchematicFile(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)

    if interactiveBom:
        makeInteractiveHtmlBom(project,overwrite)

    if partsHarvest: #open board in kicad and export things like 3d render and bom
        if overwrite or project.ifFileExists("detailsPartsRaw"):
            OOMPprojectParts.harvestParts(project,overwrite=overwrite)

    if matchParts:
        if overwrite or project.ifFileExists("detailsPartsOomp"):
            OOMPprojectParts.matchParts(project)


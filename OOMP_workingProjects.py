import OOMP
import OOMPprojectLaunch
from oomBase import *


OOMP.loadParts("pickle")

print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

#OOMPprojectLaunch.doTasks("projects")
overwrite= True
eagleProcess= False          #eagle pcb open
eagleToKicad = False        #kicad launcher open
kicadProcess = False        #kicad launcher open
interactiveBom = False
interactiveBomImages = True
partsHarvest = False
matchParts = True

filter="projects"
#filter="projects"
OOMPprojectLaunch.doTasks(overwrite=overwrite,filter=filter,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,interactiveBomImages=interactiveBomImages,partsHarvest=partsHarvest,matchParts=matchParts)

overwrite=True
project =OOMP.getPartByID("PROJ-ADAF-1032-STAN-01")
project =OOMP.getPartByID("PROJ-ADAF-3382-STAN-01")
#project =OOMP.getPartByID("PROJ-SPAR-10103-STAN-01")
#project =OOMP.getPartByID("PROJ-SPAR-10616-STAN-01")
#OOMPprojectLaunch.doTask(project=project,overwrite=overwrite,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,interactiveBomImages=interactiveBomImages,partsHarvest=partsHarvest,matchParts=matchParts)

#print(project.fullString())

import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
import OOMPproject
from oomBase import *
import json


#OOMP.loadParts("all")
#OOMP.loadParts("projects")
#OOMP.exportPickle()

OOMP.loadParts("pickle")


print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+ 
str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

#OOMP.printParts()
OOMP.setBaseDir("C:/GH/oomlout_OOMP/")


#OOMPproject.doTasks("proje
# cts")
overwrite=False
kicadProcess = True        #kicad launcher open
eagleToKicad = False        #kicad launcher open
eagleProcess= False          #eagle pcb open
interactiveBom = False
partsHarvest = False
#filter="footprints"
filter="projects"
OOMPproject.doTasks(overwrite=overwrite,filter=filter,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,partsHarvest=partsHarvest)



overwrite=True
project =OOMP.getPartByID("PROJ-ADAF-2019-STAN-01")
#OOMPproject.doTask(project=project,overwrite=overwrite,eagleToKicad=eagleToKicad,kicadProcess=kicadProcess,eagleProcess=eagleProcess,interactiveBom=interactiveBom,partsHarvest=partsHarvest)
print(project.fullString())

######  Download and harvest arduino files
#
# OOMPprojectHarvest.harvestProjectsArduino() 

